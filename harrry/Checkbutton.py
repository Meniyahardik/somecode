from tkinter import *


root = Tk()
def getvals():
   print("Submitting form")
   
   print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get()}")
   with open("records.txt", "a") as f:
       f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get()}\n")
root.geometry("644x344")
Label(root, text="Wellcome to Harry Travals", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="gender")
emergency = Label(root, text="emergency")
paymentmode = Label(root, text="payment mode")

name.grid(row=1, column=2)
phone.grid(row=2,column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)


foodservice = Checkbutton(text="want to prebook you meals?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

Button(text="Submit to Harry Travals", command=getvals).grid(row=7, column=3)

root.mainloop() 
