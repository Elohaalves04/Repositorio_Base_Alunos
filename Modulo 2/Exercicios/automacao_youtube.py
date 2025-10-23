import pyautogui as pg
from time import sleep 

pg.press('win')
pg.write('chrome')
pg.press('enter')
pg.write('www.youtube.com')
pg.press('enter')
pg.moveTo(715,167, duration=2)
pg.click()
pg.write('marisa monte')
pg.press('enter')

# pg.mouseInfo()