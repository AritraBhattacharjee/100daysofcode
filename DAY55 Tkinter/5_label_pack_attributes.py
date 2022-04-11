# other attributes of label and pack

import tkinter
root = tkinter.Tk()
root.title("Attributes of Label and pack")
root.minsize(500,300)

# Important Label Options
# text = adds the text
# bd = Background
# fg = foreground 
# font = sets the font
# padx : x padding 
# pady: y padding 
# relied : border styling-SUNKEN,RAISED,GROOVE,RIDGE

mylabel = tkinter.Label(text="My name is Aritra Bhattacharjee. \nI am a 2nd year undergrand under the branch Computer Science and engineering at JIS University.", bg="lightblue",fg="white",padx=23,pady=55,font=("comicsansms",18,"bold","italic"),borderwidth=3,relief=tkinter.SUNKEN)

# Important Pack Options
# anchor = nw 
# side = top,bottom,left,right
# mylabel.pack(anchor="se")
# fill
# padx
# pady
mylabel.pack(fill=tkinter.X)
# mylabel.pack(fill=tkinter.Y)
root.mainloop()