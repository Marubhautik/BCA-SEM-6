from tkinter import *

parent = Tk()
redbutton = Button(parent,text="Red",fg="red")
redbutton.pack(side=LEFT)
greenbutton = Button(parent,text="Green",fg="green")
greenbutton.pack(side=RIGHT)
bluebutton = Button(parent,text="blue",fg="blue")
bluebutton.pack(side=TOP)
blackbutton = Button(parent,text="black",fg="black")
blackbutton.pack(side=BOTTOM)
parent.mainloop()