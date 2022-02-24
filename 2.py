from tkinter import *

#make root (for some reason Tk is very case sensitive and i dont like it lol)
root = Tk()

#making multiple labels on root
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="John Doe")

#putting labels on a grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

#loop event (basic thing lol)
root.mainloop()


