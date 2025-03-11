from time import sleep

import pyautogui
while True:
    pos = pyautogui.position()
    print(f"当前鼠标位置: {pos}")  # 输出 (x, y)
    sleep(.5)