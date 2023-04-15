import pyautogui
import time
import random

x, y = 1780, 160
pyautogui.moveTo(x, y)
pyautogui.FAILSAFE = False

clics_realizados = 0

while True:
    for i in range(3):
        pyautogui.click(button='left')
        clics_realizados += 1
        time.sleep(random.uniform(10, 20)) 
        print("Se ha realizado el clic número", clics_realizados)
