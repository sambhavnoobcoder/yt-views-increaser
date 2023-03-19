import pyautogui
import urllib.request
import webbrowser
import time
import random

views=0

while views<5:
    webbrowser.open("https://www.youtube.com/watch?v=myy-mxOn-T8")
    # no= random.randint(3,6)
    time.sleep(5)
    pyautogui.hotkey('command','w')
    views=views+1

