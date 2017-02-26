from tkinter import *

class Building(Canvas):
    def drawSquare(self):
        print ("Drawing a square")

    def createButtons(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "build"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        self.slider1 = Scale(self, from_=0, to=200, orient=HORIZONTAL)
        self.slider1.pack()

    def __init__(self, master=None):
        Canvas.__init__(self)
        self.pack()
        self.createButtons()

root = Tk()
bldg = Building(master=root)
bldg.mainloop()
root.destroy()
