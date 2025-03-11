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

def connect_bus():
    logger.info('连接游戏窗口中...')
    try:
        app = Application(backend='win32').connect(process=14228)
        # limbus_window = app.window(title="LimbusCompany", class_name="UnityWndClass")
        limbus_window = app.window(title="Unity Hub 3.3.3-c2")

        logger.info('成功连接至游戏窗口')
        return limbus_window
    except Exception as e:
        logger.error(f'无法连接游戏窗口:{e} 请检查游戏是否正常运行！')
        logger.warning('程序将在5s后自动关闭')
        sleep(5)
        quit()


def get_window_rect(window):
    """ 使用 pyautogui 获取屏幕坐标 """
    # 获取窗口的坐标和大小
    if window.is_minimized():  # 如果窗口是最小化的
        logger.info('检测到窗口被最小化，正在恢复...')
        window.restore()
        sleep(.5)
    if not window.is_maximized():
        logger.debug('正在最大化窗口')
        window.maximize()
        sleep(.5)
    if not window.is_active():
        logger.debug('将窗口设置为前台活动窗口')
        window.set_focus()

    rect = window.rectangle()  # 使用 rectangle() 获取窗口的坐标
    return (rect.left, rect.top, rect.right, rect.bottom)


def find_image(window, template_path):
    """ 仅对窗口区域截屏，并查找 UI 位置 """
    rect = get_window_rect(window)  # 获取窗口坐标
    screenshot = ImageGrab.grab(bbox=rect)  # 仅截取窗口区域
    # screenshot.show()
    screenshot = np.array(screenshot)  # 转换为 NumPy 数组
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # 颜色格式转换

    template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)  # 读取目标图片
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(result)  # 获取匹配结果

    if max_val > 0.9:  # 设定匹配阈值
        x, y = max_loc
        logger.debug(f'记录坐标为{x},{y}')
        return x, y  # 转换为屏幕坐标
    return None


def MAKELONG(low, high):
    """ 合并两个 16 位数值为 32 位 """
    return (high << 16) | (low & 0xFFFF)


# ---- 3. 发送 Win32 API 鼠标点击 ----
def send_click(hwnd, x, y):
    """ 发送后台点击消息 """
    lParam = MAKELONG(x, y)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)
    logger.debug(f'已向{x},{y}发送PostMessage点击信息')


def click_img(image_path,window):

    hwnd = connect_bus().handle  # 连接窗口
    if hwnd:
        logger.debug(f"找到窗口句柄: {hwnd}")
        # 查找 UI 位置
        pos = find_image(window, image_path)
        if pos:
            x, y = pos
            logger.debug(f"读取到元素位置: {x}, {y}")

            # 发送后台点击
            send_click(hwnd, x, y)
        else:
            logger.warning(f"无法找到元素位置")
    else:
        logger.warning("未找到窗口")
