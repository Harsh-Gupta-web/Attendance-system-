from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main2 import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
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

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=210,width=340,height=450)

        img4=Image.open(r"images\30.png")
        img4=img4.resize((100,100),Image.BICUBIC)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg1=Label(image=self.photoimg4,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=220,width=100,height=100)

#title
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        get_str=Label(frame,text="Get Started",font=("times now roman",15,"bold"),fg="white",bg="black")
        get_str.place(x=120,y=115)

        username=Label(frame,text="Username",font=("times now roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(frame,text="Password",font=("times now roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        img5=Image.open(r"images\30.png")
        img5=img5.resize((25,25),Image.BICUBIC)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg2=Label(image=self.photoimg5,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=363,width=25,height=25)

        img6=Image.open(r"images\31.png")
        img6=img6.resize((25,25),Image.BICUBIC)
        self.photoimg6=ImageTk.PhotoImage(img6)
        lblimg3=Label(image=self.photoimg6,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=430,width=25,height=25)

        Loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,command=self.login,fg="white",bg="red",activebackground="red",activeforeground="white")
        Loginbtn.place(x=110,y=300,width=120,height=35)

        Register=Button(frame,text="New User Register",font=("times new roman",10,"bold"),bd=3,command=self.register_window,borderwidth=0,relief=RIDGE,fg="white",bg="black",activebackground="black",activeforeground="white")
        Register.place(x=15,y=350,width=160)

        forgotbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),bd=3,borderwidth=0,relief=RIDGE,command=self.forgot_password_window,fg="white",bg="black",activebackground="black",activeforeground="white")
        forgotbtn.place(x=10,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Harsh Gupta" and self.txtpass.get() == "Skg1179@@":
            messagebox.showinfo("Success", "Successfully login")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="harsh",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                    self.txtuser.get(),
                    self.txtpass.get()
                ))
                row = my_cursor.fetchone()
                if row is None:  # If no matching record is found
                    messagebox.showerror("Error", "Invalid Username and Password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Database Error: {e}")


    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
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

            if row is None:
                messagebox.showerror("Error", "Please enter a valid email")
            else:
                conn.close()

                # New window for forgot password
                self.root2 = Toplevel(self.root)
                self.root2.title("Forgot Password")
                self.root2.geometry("400x450+610+170")

                l = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_q = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your First School", "Your 10th Pass Year", "Your Mother Name")
                self.combo_security_Q.place(x=50, y=110, width=300)
                self.combo_security_Q.current(0)

                securityA = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                securityA.place(x=50, y=150)

                self.txt_securityA = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_securityA.place(x=50, y=180, width=300)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_new_password = ttk.Entry(self.root2, font=("times new roman", 15, "bold"), show="*")
                self.txt_new_password.place(x=50, y=250, width=300)

                confirm_password = Label(self.root2, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
                confirm_password.place(x=50, y=290)

                self.txt_confirm_password = ttk.Entry(self.root2, font=("times new roman", 15,"bold"), show="*")
                self.txt_confirm_password.place(x=50, y=320, width=300)

                reset_btn = Button(self.root2, text="Reset",command=self.reset_password, font=("times new roman", 15, "bold"), bg="green", fg="white")
                reset_btn.place(x=150, y=380, width=100)


    def reset_password(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Please select a security question")
        elif self.txt_securityA.get() == "":
            messagebox.showerror("Error", "Please enter the security answer")
        elif self.txt_new_password.get() == "":
            messagebox.showerror("Error", "Please enter a new password")
        elif self.txt_confirm_password.get() == "":
            messagebox.showerror("Error", "Please confirm your new password")
        elif self.txt_new_password.get() != self.txt_confirm_password.get():
            messagebox.showerror("Error", "New Password and Confirm Password do not match")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="harsh",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_securityA.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Security question/answer is incorrect")
                else:
                    query = "UPDATE register SET password=%s, confpassword=%s WHERE email=%s"
                    value = (self.txt_new_password.get(), self.txt_confirm_password.get(), self.txtuser.get())
                    my_cursor.execute(query, value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Your password has been reset successfully")
                    self.root2.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"Database Error: {e}")




           
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
    main()