# Main entry of the application
from tkinter import *
from screenshot import takeBoundedScreenShot
class Application():
    def __init__(self, master):
        # coodinates for screen selection
        self.master = master
        self.rect = None
        self.x = self.y = 0
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None

        # menu GUI setup
        root.title('SDT')
        root.geometry('250x400')
        self.menu_frame = Frame(master, bg="white")
        self.menu_frame.pack(fill=BOTH, expand=YES)
        root.resizable(False, True)

        # button frame
        self.buttonBar = Frame(self.menu_frame,bg="white")
        self.buttonBar.pack(fill=BOTH,expand=YES)
        self.snipButton = Button(self.buttonBar, width=10, command=self.createScreenCanvas, text='截取出牌区域')
        self.snipButton.pack(expand=YES)

        # canvas setup
        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "blue")
        self.picture_frame = Frame(self.master_screen, background = "blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

    def createScreenCanvas(self):
        # hide gui and show canvas
        self.master_screen.deiconify()
        root.withdraw()
        self.screenCanvas = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.screenCanvas.pack(fill=BOTH, expand=YES)
        self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
        self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
        self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        self.recPosition()
        self.exitScreenshotMode()
        return event

    def exitScreenshotMode(self):
        # Destory canvas, show gui again
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        root.deiconify()

    def exit_application(self):
        root.quit()

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.screenCanvas.canvasx(event.x)
        self.start_y = self.screenCanvas.canvasy(event.y)
        self.rect = self.screenCanvas.create_rectangle(self.x, self.y, 1, 1, outline='yellow', width=3, fill="blue")

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.screenCanvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)

    def recPosition(self):
        print(self.start_x)
        print(self.start_y)
        print(self.curX)
        print(self.curY)

        # get coordinates from 4 various drag directions, srsly just drag left down bruh
        x1 = y1 = x2 = y2 = 0
        if self.start_x <= self.curX and self.start_y <= self.curY:
            print("right down")
            x1 = self.start_x
            y1 = self.start_y
            x2 = self.curX - self.start_x
            y2 = self.curY - self.start_y
        elif self.start_x >= self.curX and self.start_y <= self.curY:
            print("left down")
            x1 = self.curX
            y1 = self.start_y
            x2 = self.start_x - self.curX
            y2 = self.curY - self.start_y
        elif self.start_x <= self.curX and self.start_y >= self.curY:
            print("right up")
            x1 = self.start_x
            y1 = self.curY
            x2 = self.curX - self.start_x
            y2 = self.start_y - self.curY
        elif self.start_x >= self.curX and self.start_y >= self.curY:
            print("left up")
            x1 = self.curX
            y1 = self.curY
            x2 = self.start_x - self.curX
            y2 = self.start_y - self.curY
        print("actual coordinates: %d %d %d %d" , x1, y1, x2, y2)
        takeBoundedScreenShot(x1, y1, x2, y2)
        # set opacity, destroy button and create data table and record textarea
        root.attributes('-alpha', 0.7)
        self.buttonBar.destroy()
        self.createDataTable()
        self.createRecordTextarea()
        
    def createDataTable(self):
        # create data table frame 
        self.dataTable = Frame(self.menu_frame,bg="")
        self.dataTable.pack(fill=BOTH,expand=YES)

        titles=['牌名','剩余']
        data = [ ["val1", 0],
                ["asd1", 0],
                ["bbb1", 0],
                ["ccc1", 0],
                ["ddd1", 0],
                ["eee1", 0] ]

        e=Entry(self.dataTable, font=('Consolas 8 bold'),bg='light blue',justify='center')
        e.grid(column=0, row=0)
        e.insert(0,titles[0])
        e=Entry(self.dataTable, font=('Consolas 8 bold'),bg='light blue',justify='center')
        e.grid(column=1, row=0)
        e.insert(0,titles[1])

        for y in range(len(data)):
            for x in range(len(titles)):
                if y%2==0:
                    e=Entry(self.dataTable, font=('Consolas 8 bold'),bg='light yellow',justify='center')
                    e.grid(column=x, row=y+1)
                    e.insert(0,data[y][x])
                else:
                    e=Entry(self.dataTable, font=('Consolas 8 bold'),bg='light blue',justify='center')
                    e.grid(column=x, row=y+1)
                    e.insert(0,data[y][x])

    def createRecordTextarea(self):
        # create data table frame 
        self.textarea = Text(self.menu_frame, height=4, width=50)
        self.textarea.pack(fill=BOTH,expand=YES)

        self.textarea.insert(END, "Welcome to SDT")

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.attributes('-topmost', True)
    root.mainloop()