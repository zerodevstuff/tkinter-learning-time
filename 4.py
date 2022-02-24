from tkinter import *

#make root (for some reason Tk is very case sensitive and i dont like it lol)
root = Tk()

#making entry widget with a width of 50 
entry = Entry(root, width=50)
entry.pack()
entry.insert(0, "enter text")
#making a function for myButton
def test():
	myLabel = Label(root, text=entry.get())
	myLabel.pack()

#making a button with blue text and padding that executes a function 
myButton = Button(root, text="enter text", padx=50, pady=50, command=test, fg="blue")

#packing
myButton.pack()

#loop event (basic thing lol)
root.mainloop()


