from tkinter import *

#make root (for some reason Tk is very case sensitive and i dont like it lol)
root = Tk()

#making a function for myButton
def test():
	myLabel = Label(root, text="i clicked this")
	myLabel.pack()

#making a button with blue text and padding that executes a function 
myButton = Button(root, text="click me!", padx=50, pady=50, command=test, fg="blue")

#packing
myButton.pack()

#loop event (basic thing lol)
root.mainloop()


