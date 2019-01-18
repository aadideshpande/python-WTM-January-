import pyautogui
import time
import sys

print(pyautogui.size()) #print size of the screen

time.sleep(5)
pyautogui.click() # press mouse button to continue with the program




# for automated scrolling, a loop is created

for i in range(1000):          #   any large value can be given in range --> to create infinite scrolling
    pyautogui.scroll(-300)
    time.sleep(10)
    pyautogui.FAILSAFE = True   # if mouse is taken to upper-left corner during the process , the process of auto scrolling is terminated





