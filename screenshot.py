
import pyautogui
import datetime
import threading
import ocr
class ScreenShot:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.x4 = 0

    def recPosition(self, start_x, start_y, curX, curY):
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
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        set_interval(self.takeBoundedScreenShot, 1) # taking screenshot every 1s

    def takeBoundedScreenShot(self):
        im = pyautogui.screenshot(region=(self.x1, self.y1, self.x2, self.y2))
        x = datetime.datetime.now()
        fileName = x.strftime("%f") + ".png" 
        # print("Running takeBoundedScreenShot: ", fileName)
        im.save(fileName)
        ocr.imageToText(fileName)

# Extended Function for set interval
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

