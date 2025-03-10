import ctypes
import time

# 定义输入结构体
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("mi", MOUSEINPUT)]

# 常量
INPUT_MOUSE = 0
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

def send_click():
    # 按下鼠标左键
    input_down = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(0, 0, 0, MOUSEEVENTF_LEFTDOWN, 0, None))
    print("left")
    # 释放鼠标左键
    input_up = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(0, 0, 0, MOUSEEVENTF_LEFTUP, 0, None))
    print("right")
    # 发送输入
    ctypes.windll.user32.SendInput(2, ctypes.byref(input_down), ctypes.sizeof(INPUT))
    ctypes.windll.user32.SendInput(2, ctypes.byref(input_up), ctypes.sizeof(INPUT))

# 直接点击，不移动鼠标

if __name__ == "__main__":
    send_click()