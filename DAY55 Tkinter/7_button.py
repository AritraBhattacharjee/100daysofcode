# buttons

import tkinter
root = tkinter.Tk()
root.geometry("655x444")
mylabel = tkinter.Label()
def hello():
    mylabel.config(text="Thanks for Clicking me")

frame = tkinter.Frame(root,borderwidth=6,bg='grey',relief=tkinter.SUNKEN)
frame.pack(anchor="nw",side=tkinter.LEFT)

btn1 = tkinter.Button(frame,fg="red",text="Click Me!",command=hello)
btn1.pack()
mylabel.pack()
root.mainloop()