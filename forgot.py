from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from Register import Register


class Forgot_Window:
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password ")
        else:
            conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="harsh",
        database="face_recognizer"
    )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)
                SecurityQ = Label(self.root2, text="Select Security Questions", font=("times now roman", 15, "bold"), bg="white")
                SecurityQ.place(x=50, y=240)
                self.combo_security_Q = ttk.Combobox(self.root2, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your First School", "Your 10th Pass Year", "Your Mother Name")
                self.combo_security_Q.place(x=50, y=270, width=250)
                self.combo_security_Q.current(0)

                
                SecurityA = Label(self.root2, text="Security Answer", font=("times now roman", 15, "bold"), bg="white")
                SecurityA.place(x=370, y=240)
                self.txtsecurityA = ttk.Entry(self.root2, textvariable=self.var_securityA,font=("times new roman", 15, "bold"))
                self.txtsecurityA.place(x=370, y=270, width=250)