from tkinter import *

#make root (for some reason Tk is very case sensitive and i dont like it lol)
root = Tk()

#making a label and getting used to noting my code lol (yknow cuz I like it being readable)
myLabel = Label(root, text="Hello World!")

#packing label on root (shouldnt do)
myLabel.pack()

#loop event (basic thing lol)
root.mainloop()