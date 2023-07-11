from tkinter import *


#Create object
root = Tk()
root.geometry('100x100')
btn = Button(root, text = 'Click me !', coommand = root.destroy)

# Set the position of button on the top of window
btn.pack(side = 'top')

root.mainloop()
