from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os 
from student2 import Student
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from deveplor import Developer
from tkinter import messagebox
from chatbot import ChatBot

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face")
#1st image 
        img=Image.open(r"images\1.jpg")
        img=img.resize((517,130),Image.BICUBIC)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=517,height=130)
#2nd image 
        img1=Image.open(r"images\2.jpg")
        img1=img1.resize((517,130),Image.BICUBIC)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=517,y=0,width=517,height=130)
#3rd image
        img2=Image.open(r"images\3.jpg")
        img2=img2.resize((517,130),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1034,y=0,width=517,height=130)
#background image 
        img3=Image.open(r"images\5.jpg")
        img3=img3.resize((1530,790),Image.BICUBIC)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
#title
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        self.time_label = Label(
            title_lbl, 
            font=('times new roman', 20, 'bold'), 
            background='white', 
            foreground='blue'
        )
        self.time_label.place(x=0,y=0,width=150,height=45)

        # Call the update_time method
        self.update_time()
#student button 
        img4=Image.open(r"images\6.jpg")
        img4=img4.resize((220,220),Image.BICUBIC)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
#Face Detect button
        img5=Image.open(r"images\7.jpg")
        img5=img5.resize((220,220),Image.BICUBIC)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_2.place(x=500,y=300,width=220,height=40)
#Attendance button
        img6=Image.open(r"images\8.jpg")
        img6=img6.resize((220,220),Image.BICUBIC)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_3.place(x=800,y=300,width=220,height=40)
#Help Desk button
        img7=Image.open(r"images\29.jpeg")
        img7=img7.resize((220,220),Image.BICUBIC)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b3.place(x=1100,y=100,width=220,height=220)

        b3_3=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_3.place(x=1100,y=300,width=220,height=40)
#Train Data button
        img8=Image.open(r"images\10.jpg")
        img8=img8.resize((220,220),Image.BICUBIC)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b3=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b3.place(x=200,y=400,width=220,height=220)

        b3_3=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_3.place(x=200,y=600,width=220,height=40)
#Photos Button
        img9=Image.open(r"images\11.jpg")
        img9=img9.resize((220,220),Image.BICUBIC)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b3=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b3.place(x=500,y=400,width=220,height=220)

        b3_3=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_3.place(x=500,y=600,width=220,height=40)
#Developer button
        img10=Image.open(r"images\12.jpg")
        img10=img10.resize((220,220),Image.BICUBIC)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b3=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Developer_data)
        b3.place(x=800,y=400,width=220,height=220)

        b3_3=Button(bg_img,text="Developer",cursor="hand2",command=self.Developer_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_3.place(x=800,y=600,width=220,height=40)
#Exit button
        img11=Image.open(r"images\13.jpg")
        img11=img11.resize((220,220),Image.BICUBIC)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b3=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit_application)
        b3.place(x=1100,y=400,width=220,height=220)

        b3_3=Button(bg_img,text="Exit",cursor="hand2",command=self.exit_application,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_3.place(x=1100,y=600,width=220,height=40)
    
    def open_img(self):
        os.startfile("data")

#Functions 
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)

    def exit_application(self):
        confirm = messagebox.askyesno(
                "Exit Application",
                "Are you sure you want to exit?"
        )
        if confirm:
                self.root.destroy()
    def update_time(self):
        # Fetch current time
        time_string = strftime('%H:%M:%S %p')
        # Update the label with the current time
        self.time_label.config(text=time_string)
        # Schedule the function to run again after 1000ms (1 second)
        self.time_label.after(1000, self.update_time)

            

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        