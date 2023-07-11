from tkinter import *
root = Tk()
root.geometry('100x100')
btn = Button(root, text = 'Click me !', bd = '5')
btn2 = Button(root, text = 'Reset me', bd = '5')
btn.pack(side = 'top')
btn2.pack(side = 'right')
root.mainloop()
