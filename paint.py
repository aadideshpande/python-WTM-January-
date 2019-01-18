import pyautogui, time
time.sleep(5)
pyautogui.click()    # click to put drawing program in focus
distance = 200


screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

pyautogui.dragRel(distance, 0, duration=0.2)   # move right
pyautogui.dragRel(0, distance, duration=0.2)   # move down
pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
pyautogui.dragRel(0, -distance, duration=0.2)  # move up

pyautogui.dragRel(distance/2,-distance/2,duration=0.5)  #forming the roof
pyautogui.dragRel(distance/2,distance/2,duration=0.5)   #forming the roof



pyautogui.moveRel(0,200)
pyautogui.moveRel(-70,0)
pyautogui.dragRel(0, -distance/3, duration=0.2)     # move up
pyautogui.dragRel(-60, 0, duration=0.2)             # move left
pyautogui.dragRel(0, distance/3, duration=0.2)      # move down

