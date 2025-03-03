from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face")
#variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_dob=StringVar()
        self.var_std_id=StringVar()
        self.var_semester=StringVar()   
        self.var_std_name=StringVar()  
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

    #1st image 
        img=Image.open(r"images\14.jpg")
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
        img2=Image.open(r"images\15.jpg")
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
        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM SOFTWARE",font=("times new roman", 35, "bold"), bg="white", fg="DARKGREEN")
        title_lbl.place(x=0,y=0,width=1530,height=45)
#frame  
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

#left label Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="white")
        Left_frame.place(x=10,y=10,width=730,height=585)

        imgleft_img=Image.open(r"images\16.jpg")
        imgleft_img=imgleft_img.resize((720,130),Image.BICUBIC)
        self.photoimgleft_img=ImageTk.PhotoImage(imgleft_img)

        f_lbl=Label(Left_frame,image=self.photoimgleft_img)
        f_lbl.place(x=0,y=0,width=720,height=130) 
#current course 
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current course information ",font=("times new roman",12,"bold"),bg="white")
        current_course_frame.place(x=5,y=135,width=720,height=150)
#Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
#Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
#year 
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2022-2023","2023-2024","2024-2025","2025-2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
#Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="read only",width=20)
        Semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
#class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student information ",font=("times new roman",12,"bold"),bg="white")
        class_student_frame.place(x=5,y=280,width=720,height=280) 
#studentid
        studentid_label=Label(class_student_frame,text="Student ID",font=("times new roman",13,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)   

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))       
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W)
#student name
        
#classdivision
        classdiv_label=Label(class_student_frame,text="Class Division",font=("times new roman",13,"bold"),bg="white")
        classdiv_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)   

        classdiv_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="read only",width=20)
        classdiv_combo["values"]=("Select Division","A","B","C")
        classdiv_combo.current(0)
        classdiv_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
#roll number
        rollno_label=Label(class_student_frame,text="Roll Number",font=("times new roman",13,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)   

        rollno_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))       
        rollno_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)
#gender
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)   

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="read only",width=20)
        gender_combo["values"]=("Select Gender","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
#dob
        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)   

        dob_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))       
        dob_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)
#email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)   

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))       
        email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)
#Phone Number
        Phone_numbber_label=Label(class_student_frame,text="Phone number",font=("times new roman",13,"bold"),bg="white")
        Phone_numbber_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)   

        Phone_numbber_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))       
        Phone_numbber_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)
#address
        address_label=Label(class_student_frame,text="Address",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)   

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))       
        address_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)
#Teacher
        Teacher_label=Label(class_student_frame,text="Teacher",font=("times new roman",13,"bold"),bg="white")
        Teacher_label.grid(row=4,column=2,padx=10,pady=10,sticky=W)   

        Teacher_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))       
        Teacher_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)
#radiobtn
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0)

        self.var_radio2=StringVar()
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio2,text="No Photo Sample",value="No")
        radionbtn2.grid(row=5,column=1)
#btn frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=225,width=715,height=90)
#save btn
        save_btn=Button(btn_frame,bd=2,text="Save",relief=RIDGE,command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=10)
        save_btn.grid(row=0,column=0)
#update btn
        update_btn=Button(btn_frame,bd=2,text="Update",relief=RIDGE,command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=11)
        update_btn.grid(row=0,column=1)
#delete btn
        delete_btn=Button(btn_frame,bd=2,text="Delete",relief=RIDGE,command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=11)
        delete_btn.grid(row=0,column=2)
#reset btn
        reset_btn=Button(btn_frame,bd=2,text="Reset",relief=RIDGE,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=11)
        reset_btn.grid(row=0,column=3)
#take photo btn
        Take_photo_btn=Button(btn_frame,bd=2,text="Take Photo",relief=RIDGE,command=self.generate_dataset,font=("times new roman",13,"bold"),bg="blue",fg="white",width=11)
        Take_photo_btn.grid(row=0,column=4)
#update photo btn
        update_photo_btn=Button(btn_frame,bd=2,text="Update Photo",relief=RIDGE,font=("times new roman",13,"bold"),bg="blue",fg="white",width=11)
        update_photo_btn.grid(row=0,column=5)

#right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="white")
        Right_frame.place(x=750,y=10,width=720,height=580)   

#right label image 
        imgright_img=Image.open(r"images\16.jpg")
        imgright_img=imgright_img.resize((720,130),Image.BICUBIC)
        self.photoimgright_img=ImageTk.PhotoImage(imgright_img)

        f_lbl=Label(Right_frame,image=self.photoimgright_img)
        f_lbl.place(x=5,y=0,width=720,height=130) 
#search frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)
#search label
        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)   
#search entry
        self.search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",13,"bold"))       
        self.search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)
#search combobox
        self.search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="read only",width=20)
        self.search_combo["values"]=("Select","Roll Number","Phone number")
        self.search_combo.current(0)
        self.search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
#search btn
        Search_btn=Button(search_frame,bd=2,text="Search",relief=RIDGE,command=self.search_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=8)
        Search_btn.grid(row=0,column=3,padx=2)
#showall btn
        showall_btn=Button(search_frame,bd=2,text="Show All",relief=RIDGE,command=self.show_all_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=8)
        showall_btn.grid(row=0,column=4,padx=2)
#table frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=210,width=710,height=300)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

# Treeview with Scrollbars
        self.student_table = ttk.Treeview(table_frame,columns=("dep", "course", "year","sem","id", "div",  "name", "roll","gender","dob", "email", "phone", "address", "teacher", "photo",),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)

# Attach Scrollbars to Treeview
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

# Set Scroll Commands
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

# Add Headings
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

# Set Column Widths
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        self.student_table.column("roll", width=100)

        self.fetch_data()
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        
    
    #function declaration  

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
          try:
    # Initialize the connection
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="harsh",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            
            # Execute the query
            my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),   
                self.var_std_id.get(),
                self.var_div.get(),
                self.var_std_name.get(),  
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
            ))
            
            # Commit changes
            conn.commit()
            self.fetch_data()
            
            # Close the connection
            conn.close()
            
            # Show success message
            messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
          except Exception as es:
            # Show error message
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
        #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="harsh",
        database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
        conn.commit()
        conn.close()    
#get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        if not data:
                return     
                self.var_dep.set(data[0]) ,
                self.var_course.set(data[1]) ,
                self.var_year.set(data[2]),
                self.var_semester.set(data[3]),  
                self.var_std_id.set(data[4]) ,
                self.var_div.set(data[5]),
                self.var_std_name.set(data[6]),
                self.var_roll.set(data[7]),
                self.var_gender.set(data[8]) ,
                self.var_dob.set(data[9]),
                self.var_email.set(data[10]),
                self.var_phone.set(data[11]),
                self.var_address.set(data[12]) ,
                self.var_teacher.set(data[13]) ,
                self.var_radio1.set(data[14])   
# update function 
    def update_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required for update.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="harsh",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()

                my_cursor.execute("""
                    UPDATE student 
                    SET Dep=%s, course=%s, year=%s, dob=%s, semester=%s, name=%s, division=%s, roll=%s, 
                        gender=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                    WHERE student_id=%s
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_dob.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()  # Ensure this corresponds to the primary key
                ))

                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Student details updated successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
# update function 
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required for update.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="harsh",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                sql="delete from student where Student_id=%s"
                val=(self.var_std_id.get(),)
                my_cursor.execute(sql,val)
                conn.commit()       
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted student details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)    
#reset
    def reset_data(self):
        self.var_dep.set("Select Department") ,
        self.var_course.set("Select Course") ,
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),  
        self.var_std_id.set("") ,
        self.var_div.set("Select Division"),
        self.var_std_name.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender") ,
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set("") ,
        self.var_teacher.set("") ,
        self.var_radio1.set("")
#generate data set 
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
        # Initialize the connection
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="harsh",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("""
                        UPDATE student 
                        SET Dep=%s, course=%s, year=%s, dob=%s, semester=%s, name=%s, division=%s, roll=%s, 
                            gender=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                        WHERE student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_dob.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1  # Ensure this corresponds to the primary key
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,225,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")    
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)  


    def search_data(self):
        if self.search_combo.get() == "Select":
                messagebox.showerror("Error", "Please select a valid search criteria", parent=self.root)
        elif self.search_entry.get() == "":
                messagebox.showerror("Error", "Please enter a search term", parent=self.root)
        else:
                try:
                        conn = mysql.connector.connect(
                                host="localhost",
                                username="root",
                                password="harsh",
                                database="face_recognizer"
                        )
                        my_cursor = conn.cursor()

                        # Query based on selected search criteria
                        if self.search_combo.get() == "Roll Number":
                                query = "SELECT * FROM student WHERE roll = %s"
                        elif self.search_combo.get() == "Phone number":
                                query = "SELECT * FROM student WHERE phone = %s"

                        my_cursor.execute(query, (self.search_entry.get(),))
                        data = my_cursor.fetchall()

                        # Clear current data in the table
                        self.student_table.delete(*self.student_table.get_children())

                        # Insert the search results
                        if len(data) != 0:
                                for i in data:
                                        self.student_table.insert("", END, values=i)
                        else:
                                messagebox.showinfo("Info", "No matching records found", parent=self.root)

                        conn.close()
                except Exception as es:
                        messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

# Show All Button Functionality
    def show_all_data(self):
        try:
                conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="harsh",
                database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                data = my_cursor.fetchall()

                # Clear current data in the table
                self.student_table.delete(*self.student_table.get_children())

                # Insert all records
                if len(data) != 0:
                        for i in data:
                                self.student_table.insert("", END, values=i)

                conn.close()
        except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




          



if __name__ == "__main__":

    root=Tk()
    obj=Student(root)
    root.mainloop()                