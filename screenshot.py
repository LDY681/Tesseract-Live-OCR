
import pyautogui
import datetime


def takeBoundedScreenShot(x1, y1, x2, y2):
    im = pyautogui.screenshot(region=(x1, y1, x2, y2))
    x = datetime.datetime.now()
    fileName = x.strftime("%f")
    im.save(fileName + ".png")

