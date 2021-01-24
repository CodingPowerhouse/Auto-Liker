import pyautogui
import time

numberOfLikes = 0

time.sleep(3)

while numberOfLikes <= 10:
    time.sleep(1)
    pyautogui.press('j')
    time.sleep(1)
    pyautogui.press('l')
    time.sleep(1)
    pyautogui.press('enter')
    numberOfLikes = numberOfLikes + 1