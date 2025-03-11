from time import sleep
import cv2
import numpy as np
import win32gui
import win32con
from PIL import ImageGrab
from pywinauto import Application
import logging
import warnings

warnings.simplefilter('ignore', category=UserWarning)
logger = logging.getLogger("app")

class GameManager:
    def __init__(self, title="LimbusCompany", class_name="UnityWndClass"):
        """
        初始化时指定游戏窗口的标题和类名，并设置必要的成员变量
        """
        self.title = title
        self.class_name = class_name
        self.logger = logger
        self.window = None
        self.hwnd = None

    def connect_bus(self):
        """
        连接游戏窗口，并保存窗口对象和句柄到成员变量
        """
        self.logger.info('连接游戏窗口中...')
        try:
            app = Application(backend='win32').connect(title=self.title, class_name=self.class_name)
            self.window = app.window(title=self.title, class_name=self.class_name)
            self.logger.info('成功连接至游戏窗口')
            self.hwnd = self.window.handle
            return self.window
        except Exception as e:
            self.logger.error(f'无法连接游戏窗口: {e} 请检查游戏是否正常运行！')
            self.logger.warning('程序将在5s后自动关闭')
            sleep(5)
            quit()

    def get_window_rect(self):
        """
        获取窗口坐标并确保窗口处于正常显示状态
        """
        if self.window.is_minimized():
            self.logger.info('检测到窗口被最小化，正在恢复...')
            self.window.restore()
            sleep(0.5)
        if not self.window.is_maximized():
            self.logger.debug('正在最大化窗口')
            self.window.maximize()
            sleep(0.5)
        if not self.window.is_active():
            self.logger.debug('将窗口设置为前台活动窗口')
            self.window.set_focus()

        rect = self.window.rectangle()
        self.logger.debug(f"窗口坐标: {rect}")
        return (rect.left, rect.top, rect.right, rect.bottom)

    @staticmethod
    def MAKELONG(low, high):
        """
        合并两个16位数值为32位
        """
        return (high << 16) | (low & 0xFFFF)

    def send_click(self, x, y):
        """
        向指定坐标发送后台点击消息
        """
        lParam = self.MAKELONG(x, y)
        win32gui.PostMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.PostMessage(self.hwnd, win32con.WM_LBUTTONUP, None, lParam)
        self.logger.debug(f'已向 {x},{y} 发送 PostMessage 点击信息')

    def find_image(self, template_path):
        """
        在窗口区域内截屏并查找模板图片的位置
        """
        rect = self.get_window_rect()
        screenshot = ImageGrab.grab(bbox=rect)
        screenshot.show()  # 可用于调试时预览截图
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.9:  # 设定匹配阈值
            x, y = max_loc
            self.logger.debug(f'记录坐标为 {x},{y}')
            return x, y
        return None

    def click_img(self, image_path):
        """
        查找图片位置后发送点击事件
        """
        # 如果未连接窗口，则先连接
        if self.hwnd is None:
            self.connect_bus()
        pos = self.find_image(image_path)
        if pos:
            x, y = pos
            self.logger.debug(f"读取到元素位置: {x}, {y}")
            self.send_click(x, y)
        else:
            self.logger.warning("无法找到元素位置")

    def auto_fighting(self):
        """
        自动战斗逻辑，根据不同的图片状态执行对应的点击和等待操作
        """
        while True:
            if self.find_image('./img/startTurn_yet.png') is not None:
                self.click_img('./img/P.png')
                sleep(1)
            if self.find_image('./img/startTurn.png') is not None:
                self.click_img('./img/startTurn.png')
                sleep(1)
            if self.find_image('./img/wait_fighting.png') is not None:
                sleep(30)
            if self.find_image('./img/dante_inMirror.png') is not None:
                return

# 示例：如何使用这个类
if __name__ == '__main__':
    gm = GameManager()
    gm.connect_bus()  # 连接游戏窗口
    gm.auto_fighting()
