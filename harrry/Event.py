from tkinter import * 

def harry(event):
    print(f"You clicked on the button  at {event.x}, {event.y}")
root = Tk()
root. title("event in Tkinter")
root. geometry("644x334")

widget = Button(root, text='click me please')
widget.pack()

widget.bind('<Button-1>', harry)

root.mainloop()