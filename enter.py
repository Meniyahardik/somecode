from tkinter import *
from tkinter.ttk import * 
root = Tk() 

def enter(event):
    print("Enter the Freame")
    # print('Button-2 pressed at x=%d, y = %d' %(event.x, event.y))
    
def exit_(event): 
    print("exit the frame")
    # print('Button-3 pressed at x=%d, y=%d' %(event.x, event.y))
root.geometry("200x100")
f = Frame(root, height=100, width=200)
f.bind('<Enter>', enter)
f.bind('<Leave>', exit_)
f.pack()
root.mainloop() 