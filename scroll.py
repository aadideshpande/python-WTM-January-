import pyautogui
import time

print(pyautogui.size()) #print size of the screen

time.sleep(5)
pyautogui.click() # press mouse button to continue with the program




# for automated scrolling, a loop is created

for i in range(5):          #    '5' will be replaced depending upon the length of the webpage
    pyautogui.scroll(-300)
    time.sleep(10)
    i=i+1

