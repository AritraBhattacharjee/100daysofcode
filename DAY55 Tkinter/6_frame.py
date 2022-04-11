import tkinter
root = tkinter.Tk()
root.title("Frames")
root.geometry("655x333")
f1 = tkinter.Frame(root,bg='grey',borderwidth=2,relief=tkinter.SUNKEN)
f1.pack(side=tkinter.LEFT)
f2 = tkinter.Frame(root,bg='grey',borderwidth=2,relief=tkinter.SUNKEN)
f2.pack(side=tkinter.TOP,fill="x")


l = tkinter.Label(f1,text = "Project Tkinter-Text editor")
l.pack(pady=25)
l = tkinter.Label(f2,text = "Project Tkinter-Text editor")
l.pack(pady=25)
root.mainloop()
