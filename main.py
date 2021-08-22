  
############## SDT Main Entry ###############
#
# Author: Dayu Liu
# Date: 8/12/21
# Description: Main entry for the application
# Tkinter GUI setup and so on
#

from tkinter import *
import screenshot
import cards
import sharedData

class Application():
    def __init__(self, master):
        self.master = master
        # menu GUI setup
        root.title('SDT')
        root.geometry('250x400')
        self.menu_frame = Frame(master, bg="white")
        self.menu_frame.pack(fill=BOTH, expand=YES)
        root.resizable(False, True)

        # screrenshot button frame
        self.buttonBar = Frame(self.menu_frame,bg="white")
        self.buttonBar.pack(fill=BOTH,expand=YES)
        self.snipButton = Button(self.buttonBar, width=10, command=self.createScreenCanvas, text='截取出牌区域')
        self.snipButton.pack(expand=YES)

        # coodinates for screenshot
        self.rect = None    # rectangle for screenshot area
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None

        # canvas setup
        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "blue")
        self.picture_frame = Frame(self.master_screen, background = "blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

    ## screen canvas
    # show canvas for screenshot and also hide app gui
    def createScreenCanvas(self):
        self.master_screen.deiconify()
        root.withdraw()
        self.screenCanvas = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.screenCanvas.pack(fill=BOTH, expand=YES)
        self.screenCanvas.bind("<ButtonPress-1>", self.on_canvas_button_press)
        self.screenCanvas.bind("<B1-Motion>", self.on_canvas_move_press)
        self.screenCanvas.bind("<ButtonRelease-1>", self.on_canvas_button_release)
        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    # on finishing screenshot, record position and exit
    def on_canvas_button_release(self, event):
        self.recPosition()
        self.exitCanvas()
        return event

    # on starting screenshot, record starting position
    def on_canvas_button_press(self, event):
        self.start_x = self.screenCanvas.canvasx(event.x)
        self.start_y = self.screenCanvas.canvasy(event.y)
        self.rect = self.screenCanvas.create_rectangle(0, 0, 1, 1, outline='yellow', width=3, fill="blue")

    # on dragging area on screenshot canvas
    def on_canvas_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.screenCanvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)

    def exitCanvas(self):
        # Destory canvas, show gui again
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        root.deiconify()

    def recPosition(self):
        print(self.start_x)
        print(self.start_y)
        print(self.curX)
        print(self.curY)
        myScreenshot = screenshot.ScreenShot()
        myScreenshot.recPosition(self.start_x, self.start_y, self.curX, self.curY)
        # set opacity, destroy button and create data table and record textarea
        root.attributes('-alpha', 0.7)
        self.buttonBar.destroy()
        self.createDataTable()
        self.createRecordTextarea()
        
    ## data table
    def createDataTable(self):
        # create data table frame 
        self.dataTable = Frame(self.menu_frame,bg="")
        self.dataTable.pack(fill=BOTH,expand=YES)
        
        myCards = cards.Cards()
        titles=['牌名','剩余']
        cardData = myCards.cardData

        e=Entry(self.dataTable, font=('Consolas 8 bold'),bg='light blue',justify='center')
        e.grid(column=0, row=0)
        e.insert(0,titles[0])
        e=Entry(self.dataTable, font=('Consolas 8 bold'),bg='light blue',justify='center')
        e.grid(column=1, row=0)
        e.insert(0,titles[1])

        for y in range(len(cardData)):
            for x in range(len(titles)):
                if y%2==0:
                    e=Entry(self.dataTable, font=('Consolas 8 bold'),bg='light yellow',justify='center')
                    e.grid(column=x, row=y+1)
                    e.insert(0,cardData[y][x])
                else:
                    e=Entry(self.dataTable, font=('Consolas 8 bold'),bg='light blue',justify='center')
                    e.grid(column=x, row=y+1)
                    e.insert(0,cardData[y][x])

    def countdown(self, root):
        self.addNewText()
        root.after(1000, self.countdown, root)  # repeat the call

    ## textarea
    def createRecordTextarea(self):
        # create data table frame 
        self.textarea = Text(self.menu_frame, height=4, width=50)
        self.textarea.pack(fill=BOTH,expand=YES)
        self.textarea.insert(END, "Welcome to SDT")
        root.after(0, self.countdown, root)  # show that we are alive
    
    def addNewText(self):
        self.textarea.delete('1.0', END)
        # print(sharedData.ocrResult)
        self.textarea.insert(END, '\n'.join("{0}".format(id) for id in sharedData.ocrResult))
        self.textarea.see("end")

    def exit_application(self):
        root.quit()

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.attributes('-topmost', True)
    root.mainloop()