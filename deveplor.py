from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face")

        # Title
        title_lbl = Label(
            self.root, 
            text="Developer", 
            font=("times new roman", 35, "bold"), 
            bg="white", 
            fg="darkblue"
        )
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # Background Image
        img3 = Image.open(r"images\20.jpg")
        img3 = img3.resize((1530, 710), Image.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=55, width=1530, height=710)  # Start below the title bar

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1020,y=0,width=500,height=700)

        img1 = Image.open(r"images\21.jpeg")
        img1 = img1.resize((200, 200), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        photo = Label(main_frame, image=self.photoimg1)
        photo.place(x=300, y=0, width=200, height=200)

        Left_frame=Label(main_frame,text="Hello I am Harsh",font=("times new roman",20,"bold"),bg="white",fg="red")
        Left_frame.place(x=0,y=5)

        Left_frame=Label(main_frame,text="I am Full Stack Developer",font=("times new roman",18,"bold"),bg="white",fg="red")
        Left_frame.place(x=0,y=60)

        img2 = Image.open(r"images\22.jpeg")
        img2 = img2.resize((500, 500), Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        photo = Label(main_frame, image=self.photoimg2)
        photo.place(x=0, y=200, width=500, height=500)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
