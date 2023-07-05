from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# Title 1 Position: x:548  y:580
# Title 2 Position: x:657  y:580
# Title 3 Position: x:763  y:580
# Title 4 Position: x:859  y:580


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # Isto pausa o script por 0.01 segundo
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(557, 580)[0] == 17:
        # [0] This checks the R  value of the pixel in 557 , 580
        # [0] = R (red)value
        # [1] = G (green) value
        # [2] = B (blue) value
        click(557, 580)
    if pyautogui.pixel(662, 580)[0] == 17:
        click(660, 580)
    if pyautogui.pixel(742, 580)[0] == 17:
        click(754, 580)
    if pyautogui.pixel(825, 580)[0] == 17:
        click(865, 580)


# http://pianotiles.org/

# https://pyautogui.readthedocs.io/en/latest/
