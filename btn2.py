from tkinter import *
from tkinter.ttk import *

#Create Root Object
root = Tk()

#Set Geometry(widthxheight)

root.geometry('500x500')

# Create style object
style = Style()

style.configure('TButton', font = ('calibri', 20, 'bold'), borderwidth = '4')

style.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active', 'black')])

#Button 1

btn1 = Button(root, text = 'Quit me !', command = root.destroy)
btn1.grid(row = 0, column = 3, padx = 100)

btn2 = Button(root, text = 'Click me !', commnd = None)
btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

root.mainloop()
