# Canvas widget : helpful in drawing shapes 
import tkinter

root = tkinter.Tk()
root.title("Canvas") 
canvas_width = 800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = tkinter.Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

can_widget.create_line(0,200,800,0,fill="red")
can_widget.create_rectangle(3,5,700,300)#top left, bottom right:coordinate order

can_widget.create_text(200,200,text="Tkinter")# center coordinate of the text

can_widget.create_oval(3,5,700,300)# coordinates of the rectangle inside which the oval is to be formed

root.mainloop()