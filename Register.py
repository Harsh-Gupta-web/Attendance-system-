from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Registration")

        #variables 

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        img1 = Image.open(r"images/5.jpg").resize((1530, 900), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img1 = Label(self.root, image=self.photoimg1)
        bg_img1.place(x=0, y=0, width=1530, height=900)

        # Left-side Image
        img2 = Image.open(r"images/35.jpg").resize((470, 550), Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)  # Convert to PhotoImage
        left_lbl = Label(self.root, image=self.photoimg2)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # Main Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times now roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # First Name
        f_name = Label(frame, text="First Name", font=("times now roman", 15, "bold"), bg="white")
        f_name.place(x=50, y=100)
        self.txtfname = ttk.Entry(frame, textvariable=self.var_fname,font=("times new roman", 15, "bold"))
        self.txtfname.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(frame, text="Last Name", font=("times now roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)
        self.txtlname = ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman", 15, "bold"))
        self.txtlname.place(x=370, y=130, width=250)

        # Contact
        contact = Label(frame, text="Contact No.", font=("times now roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)
        self.txtcontact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txtcontact.place(x=50, y=200, width=250)

        # Email
        email = Label(frame, text="Email", font=("times now roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)
        self.txtemail = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txtemail.place(x=370, y=200, width=250)

        # Security Questions
        SecurityQ = Label(frame, text="Select Security Questions", font=("times now roman", 15, "bold"), bg="white")
        SecurityQ.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your First School", "Your 10th Pass Year", "Your Mother Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        # Security Answer
        SecurityA = Label(frame, text="Security Answer", font=("times now roman", 15, "bold"), bg="white")
        SecurityA.place(x=370, y=240)
        self.txtsecurityA = ttk.Entry(frame, textvariable=self.var_securityA,font=("times new roman", 15, "bold"))
        self.txtsecurityA.place(x=370, y=270, width=250)

        # Password
        Password = Label(frame, text="Password", font=("times now roman", 15, "bold"), bg="white")
        Password.place(x=50, y=310)
        self.txtPassword = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"), show="*")
        self.txtPassword.place(x=50, y=350, width=250)

        # Confirm Password
        cPassword = Label(frame, text="Confirm Password", font=("times now roman", 15, "bold"), bg="white")
        cPassword.place(x=370, y=310)
        self.txtcPassword = ttk.Entry(frame, textvariable=self.var_confpass,font=("times new roman", 15, "bold"), show="*")
        self.txtcPassword.place(x=370, y=350, width=250)

        # Terms & Conditions Checkbutton
        self.var_chk = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_chk,text="Yes, I agree to the terms and conditions",
                               font=("times now roman", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # Register Button
        img3=Image.open(r"images\33.jpg")
        img3=img3.resize((100,50),Image.BICUBIC)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b2=Button(frame,image=self.photoimg3,borderwidth=0,command=self.register_data,cursor="hand2",bg="white")
        b2.place(x=330,y=420,width=300)

        img2=Image.open(r"images\34.jpg")
        img2=img2.resize((100,50),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimg2,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=420,width=300)

        # Reset Button
        img5=Image.open(r"images\34.png")
        img5=img5.resize((100,50),Image.BICUBIC)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b3 = Button(frame, image=self.photoimg5, borderwidth=0, command=self.reset_data, cursor="hand2", bg="white")
        b3.place(x=10, y=470, width=300)

    def register_data(self):
        if self.var_fname.get() =="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same ")
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            try:
                conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="harsh",
        database="face_recognizer"
    )
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    my_cursor.execute(
                        "INSERT INTO register VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get(),
                            self.var_confpass.get(),
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Success", "Registered Successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Database Error: {e}")
            finally:
                conn.close()

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
                self.combo_security_Q = ttk.Combobox(self.root2, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your First School", "Your 10th Pass Year", "Your Mother Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                
                SecurityA = Label(self.root2, text="Security Answer", font=("times now roman", 15, "bold"), bg="white")
                SecurityA.place(x=370, y=240)
                self.txtsecurityA = ttk.Entry(self.root2, textvariable=self.var_securityA,font=("times new roman", 15, "bold"))
                self.txtsecurityA.place(x=370, y=180, width=250)

                Newpass= Label(self.root2, text="New Password", font=("times now roman", 15, "bold"), bg="white")
                Newpass.place(x=50, y=220)
                self.txtnewpass = ttk.Entry(self.root2, textvariable=self.var_securityA,font=("times new roman", 15, "bold"))
                self.txtnewpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
            

    def reset_data(self):
        self.txtfname.delete(0, END)
        self.txtlname.delete(0, END)
        self.txtcontact.delete(0, END)
        self.txtemail.delete(0, END)
        self.combo_security_Q.current(0)
        self.txtsecurityA.delete(0, END)
        self.txtPassword.delete(0, END)
        self.txtcPassword.delete(0, END)
        self.var_chk.set(0)


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
