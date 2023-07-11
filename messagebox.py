from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('500x500')

x = messagebox.showinfo("Showinfo", "Iinformation" )
print(x)

x = messagebox.showwarning("showwarning", "Warning")
print(x) 
x = messagebox.showerror("showerror", "Error")
print(x) 
x = messagebox.askquestion("askquestion", "Are you sure")
print(x)
x = messagebox.askokcancel("askokcancel", "ok")
print(x)
x = messagebox.askyesno("askyesno", "find the value")
print(x)
x = messagebox.askretrycancel("aksretrycancel", "it ok")
print(x)


root.mainloop() 
