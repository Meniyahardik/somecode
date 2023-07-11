from tkinter import * 
root = Tk()

root.geometry("733x566")
root.title("Pycharm")

def myfunc():
    print("hello")
mymenu = Menu(root)
mymenu.add_command(label="file", command=myfunc)
root.mainloop()