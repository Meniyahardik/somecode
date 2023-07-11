from tkinter import * 

def sel(event): 
    selection = "value="+str(var.get())
    label.config(text=selection)
    # print(scale.get())
    # btn.config(width=str(var.get()))
app = Tk() 
var = DoubleVar()
scale = Scale(app, variable=var, from_=50, to=100, tickinterval=1, fg="RED", highlightbackground="BLUE", label="this is scale", length=500, orient="horizontal", resolution=0.5, sliderlength=100, command=sel )
scale.pack(anchor=CENTER)
btn = Button(app, text="Get Scale Value", command=sel)
btn.pack(anchor=CENTER)
label=Label(app)
label.pack()
app.mainloop()