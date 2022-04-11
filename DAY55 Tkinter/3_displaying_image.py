import tkinter
from PIL import Image,ImageTk
root = tkinter.Tk()
root.title("Displaying Image")
root.minsize(300,300)
path = r'D:\\Programming\\Python\\#100daysofcode\\DAY55 Tkinter\\images\\10.jpeg'

# photo = ImageTk.PhotoImage(file="2.png")
# photo = ImageTk.PhotoImage(file=path)
# displayPic = tkinter.Label(image=photo)
# displayPic.pack()

# method 2
# images = Image.open("1.jpg")
images = Image.open(path)
photo = ImageTk.PhotoImage(images)
label = tkinter.Label(image = photo)
label.pack()

root.mainloop()