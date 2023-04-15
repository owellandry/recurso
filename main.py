python3 -m pip install pyautogui &&
sudo apt-get install scrot -y &&
sudo apt-get install python3-tk -y &&
sudo apt-get install python3-dev -y

import pyautogui as pg

count = 0
while True:
    count=count+1
    pg.sleep(3)
    pg.click()
    pg.rightClick()
    pg.press("down")
    pg.press("enter")
    print(count)
    if count==80:
        break

#let div = document.querySelector('[data-id="42"]');
#div.click();
