# labels, geometry, maxsize and minsize
import tkinter

root=tkinter.Tk()
root.title("Labels, geometry") # setting the title of the Tkinter window
root.geometry("400x500") # width x Height
root.minsize(400,300)# width , height # cannot make the window smaller than the minsize parameters
root.maxsize(800,800)


mylabel = tkinter.Label(text="This is a label 1")
mylabel.pack()

root.mainloop()