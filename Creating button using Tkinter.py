from tkinter import *

root = Tk()
root.geometry('100x100')
#Creat a Button
btn = Button(root, text = 'Click me !', bd = '20', command = root.destroy)
btn.pack(side = 'bottom')
root.mainloop()
