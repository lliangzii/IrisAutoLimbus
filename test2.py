import time

from PIL import ImageGrab
from pywinauto import Application


# app = Application(backend='win32').connect(process=14228)
# window = app.window(title="Unity Hub 3.3.3-c2")
#
# window.set_focus()
# time.sleep(1)
# window.maximize()

screenshot = ImageGrab.grab()  # 仅截取窗口区域
screenshot.show()