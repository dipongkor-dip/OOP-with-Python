import pyautogui

# from time import sleep
# alternative
import time

pyautogui.write("sudo apt update", interval=0.25)

time.sleep(3) # 3s after run code

pyautogui.press("enter")
