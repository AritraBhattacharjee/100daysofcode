# checkboxes and entry widget
import tkinter

root = tkinter.Tk()

root.geometry("644x344")
tkinter.Label(root,text = "Welcome to Happy Travels",font="comicsansms 13 bold").grid(row = 0,column=0)

name = tkinter.Label(root,text = "Name: ")
phone = tkinter.Label(root,text = "Phone: ")
gender = tkinter.Label(root,text = "Gender: ")
emergency = tkinter.Label(root,text = "Emergency Contact: ")
paymentmode = tkinter.Label(root,text = "Payment Mode: ")

name.grid(row=1,column=1)
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)
emergency.grid(row=4,column=1)
paymentmode.grid(row=5,column=1)

namevalue = tkinter.StringVar()
phonevalue = tkinter.StringVar()
gendervalue = tkinter.StringVar()
emergencyvalue = tkinter.StringVar()
paymentmodevalue = tkinter.StringVar()
foodservicevalue = tkinter.IntVar()

nameentry = tkinter.Entry(root,textvariable=namevalue)
phoneentry = tkinter.Entry(root,textvariable=phonevalue)
genderentry = tkinter.Entry(root,textvariable=gendervalue)
emergencyentry = tkinter.Entry(root,textvariable=emergencyvalue)
paymentmodeentry = tkinter.Entry(root,textvariable=paymentmodevalue)
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# checkbox
foodservice = tkinter.Checkbutton(text="Want to prebook your meal?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)


def getvals():
    print("Submitting Form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n")
    
tkinter.Button(text="Submit your response",command=getvals).grid(row=7,column=3)
root.mainloop()