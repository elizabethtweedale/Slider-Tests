from tkinter import *

def drawRow(self,s1,s2):
    mySketch.create_rectangle(100,100, s1, s2, fill="grey")

def main():
    root = Tk()
    mySketch = Canvas(root, width=300, height=400)
    mySketch.pack()


    slider1 = Scale(root, from_=0, to=200)
    slider1.pack()
    slider2 = Scale(root, from_=0, to=200, orient=HORIZONTAL)
    slider2.pack()

    mySketch.bind("<ButtonPress-1>", drawRow(self, slider1.get(), slider2.get()))
    

 #   mySketch.create_rectangle(50, 25, (slider1.get()+5), 75, fill="blue")

    drawButton = Button(root, text='Draw Tower', command=drawBuilding(slider1.get(), slider2.get())).pack()
    
    root.mainloop()

def drawBuilding(s1,s2):
    print (s1,s2)

main()
