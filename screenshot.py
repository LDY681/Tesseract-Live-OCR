
import pyautogui
import datetime

def recPosition(start_x, start_y, curX, curY):
    # get coordinates from 4 various drag directions, srsly just drag left down bruh
    x1 = y1 = x2 = y2 = 0
    if start_x <= curX and start_y <= curY:
        print("right down")
        x1 = start_x
        y1 = start_y
        x2 = curX - start_x
        y2 = curY - start_y
    elif start_x >= curX and start_y <= curY:
        print("left down")
        x1 = curX
        y1 = start_y
        x2 = start_x - curX
        y2 = curY - start_y
    elif start_x <= curX and start_y >= curY:
        print("right up")
        x1 = start_x
        y1 = curY
        x2 = curX - start_x
        y2 = start_y - curY
    elif start_x >= curX and start_y >= curY:
        print("left up")
        x1 = curX
        y1 = curY
        x2 = start_x - curX
        y2 = start_y - curY
    print("actual coordinates: %d %d %d %d" , x1, y1, x2, y2)
    takeBoundedScreenShot(x1, y1, x2, y2)

def takeBoundedScreenShot(x1, y1, x2, y2):
    im = pyautogui.screenshot(region=(x1, y1, x2, y2))
    x = datetime.datetime.now()
    fileName = x.strftime("%f")
    im.save(fileName + ".png")

