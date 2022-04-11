from errno import EEXIST
from faulthandler import disable
from re import I
from tarfile import ExFileObject
import tkinter
import os
import time
from PIL import Image,ImageTk


i=0
root = tkinter.Tk()
root.title("Album")
root.minsize(300,300)
root.maxsize(800,800)
# root.geometry("800x800")
# root.mainloop()
path = "D:\Programming\Python\#100daysofcode\DAY55 Tkinter\images"
# path = "D:/Programming/Python/#100daysofcode/DAY55 Tkinter/images"
list_images = os.listdir(path)
print(list_images)
print_image=[]
for images in list_images:
    if (images.endswith('.jpg')) or (images.endswith('jpeg')) or (images.endswith('png')):
        # print(f"{os.path.join(path,images)}")
        originalPath = os.path.join(path,images)
        photo = Image.open(originalPath)
        # photo = Image.open(images)
        photos = ImageTk.PhotoImage(photo)
        print_image.append(photos)
        # label = tkinter.Label(image = photos)
        # label.pack()

# print(print_image)
label = tkinter.Label(image = print_image[0])
label.pack()
    
def Next():
    global i
    i = i + 1
    try:
        label.config(image = print_image[i])
    except:
        i = -1
        Next()



def Prev():
    global i
    i = i-1
    if i==0:
        button1.config(state=tkinter.DISABLED)
    
    try:
        label.config(image = print_image[i])

    except:
        i = i-1
        Next()

button1 = tkinter.Button(text="Click me",command=Prev)
button1.pack(side="left")
button2 = tkinter.Button(text="Click me",command=Next)
button2.pack(side="right")
root.mainloop()


        

