# https://www.humanbenchmark.com/tests/reactiontime
# 30 ms average

import pynput
import pyautogui
import time

time.sleep(1)
mouse = pynput.mouse.Controller()

i = 0
while i < 5:
    pix = pyautogui.pixel(155, 155)
    if pix == (41, 130, 202):
        mouse.click(pynput.mouse.Button.left, 1)
        time.sleep(0.1)
    if pix == (72, 211, 102):
        mouse.click(pynput.mouse.Button.left, 1)
        time.sleep(1)
        i += 1
