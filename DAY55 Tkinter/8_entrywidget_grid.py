import tkinter

def getvals():
    print(uservalue.get())
    print(passvalue.get())
root = tkinter.Tk()
root.geometry("655x444")

user = tkinter.Label(root,text = "UserName")
password = tkinter.Label(root,text = "Password")
user.grid()
password.grid()

# Variable classes in tkinter
# BooleanVar, DoubleVar,IntVar,StringVar

uservalue = tkinter.StringVar()
passvalue = tkinter.StringVar()

userentry = tkinter.Entry(root,textvariable=uservalue)
passentry = tkinter.Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
btn = tkinter.Button(text="Submit",command=getvals).grid()
root.mainloop()