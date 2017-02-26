from tkinter import *

def main():
    root = Tk()
    myWindow = Scale(myWindow, from_=0, to=45)
    myWindow.pack()
    myWindow = Scale(root, from_=0, to=200, orient=HORIZONTAL)
    myWindow.pack()
    root.mainloop()

main()
