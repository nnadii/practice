from tkinter import *

root = Tk()


def do_something():
    print("Hurray, you clicked the button")


button1 = Button(root, text="click here", command=do_something)
button1.pack()

root.mainloop()
