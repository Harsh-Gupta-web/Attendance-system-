from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face")

        self.var_attendid=StringVar()
        self.var_attendroll=StringVar()
        self.var_attendname=StringVar()
        self.var_attenddep=StringVar()
        self.var_attendtime=StringVar()
        self.var_attenddate=StringVar()
        self.var_attendattendance=StringVar()


#1st image 
        img=Image.open(r"images\2.jpg")
        img=img.resize((800,200),Image.BICUBIC)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
#2nd image 
        img1=Image.open(r"images\15.jpg")
        img1=img1.resize((800,200),Image.BICUBIC)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

#background image 
        img3=Image.open(r"images\5.jpg")
        img3=img3.resize((1530,790),Image.BICUBIC)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710) 

#title
        title_lbl=Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman", 35, "bold"), bg="white", fg="DARKGREEN")
        title_lbl.place(x=0,y=0,width=1530,height=45)
#frame  
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=45,width=1480,height=600)

#left label Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information ",font=("times new roman",12,"bold"),bg="white",fg="red")
        Left_frame.place(x=10,y=10,width=730,height=530)

        imgleft_img=Image.open(r"images\16.jpg")
        imgleft_img=imgleft_img.resize((720,130),Image.BICUBIC)
        self.photoimgleft_img=ImageTk.PhotoImage(imgleft_img)

        f_lbl=Label(Left_frame,image=self.photoimgleft_img)
        f_lbl.place(x=0,y=0,width=720,height=130) 

        left_inside_frame=Frame(Left_frame,relief=RIDGE,bd=2,bg="white")
        left_inside_frame.place(x=0,y=132,width=722,height=372)
#Name
        Name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)   

        Name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendname,font=("times new roman",13,"bold"))       
        Name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
#attendance id 
        attendance_id_label=Label(left_inside_frame,text="Attendance id:",font=("times new roman",13,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)   

        attendance_id_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendid,font=("times new roman",13,"bold"))       
        attendance_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
#Roll 
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)   

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendroll,font=("times new roman",13,"bold"))       
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

#Department
        Department_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)   

        Department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attenddep,font=("times new roman",13,"bold"))       
        Department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
#Time
        Time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)   

        Time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendtime,font=("times new roman",13,"bold"))       
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
#Date        
        Date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)   

        Date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attenddate,font=("times new roman",13,"bold"))       
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
#attendance status
        attendance_status_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman",13,"bold"),bg="white")
        attendance_status_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)   

        attendance_status_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attendattendance,font=("times new roman",13,"bold"),state="read only",width=20)
        attendance_status_combo["values"]=("Select Status","Present","Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)


#btn frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=225,width=715,height=37)
#import csv btn
        save_btn=Button(btn_frame,bd=2,text="Import CSV",relief=RIDGE,command=self.importCsv,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)
#export csv btn
        update_btn=Button(btn_frame,bd=2,text="Export CSV",relief=RIDGE,command=self.exportCsv,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)
#update btn
        delete_btn=Button(btn_frame,bd=2,text="Update",relief=RIDGE,command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)
#reset btn
        reset_btn=Button(btn_frame,bd=2,text="Reset",relief=RIDGE,command=self.reset_entries,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)

#right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),bg="white")
        Right_frame.place(x=750,y=10,width=720,height=530)

#table frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        table_frame.place(x=0,y=2,width=713,height=500)
# Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

# Treeview
        self.attendance_report = ttk.Treeview(table_frame,columns=("name", "id","roll", "department", "time", "date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

# Attach Scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

# Configure Scroll Commands
        scroll_x.config(command=self.attendance_report.xview)
        scroll_y.config(command=self.attendance_report.yview)

# Add Treeview Headings)
        self.attendance_report.heading("name", text="Name")
        self.attendance_report.heading("id", text="Attendance ID")
        self.attendance_report.heading("roll", text="Roll Number")
        self.attendance_report.heading("department", text="Department")
        self.attendance_report.heading("time", text="Time")
        self.attendance_report.heading("date", text="Date")
        self.attendance_report.heading("attendance", text="Attendance")
        self.attendance_report["show"] = "headings"

# Set Column Widths
        self.attendance_report.column("id", width=100)
        self.attendance_report.column("roll", width=100)
        self.attendance_report.column("name", width=150)
        self.attendance_report.column("department", width=100)
        self.attendance_report.column("time", width=150)
        self.attendance_report.column("date", width=150)
        self.attendance_report.column("attendance", width=150)
        self.attendance_report.bind("<ButtonRelease>", self.get_cursor)


# Pack the Treeview
        self.attendance_report.pack(fill=BOTH, expand=1)

#fecth data 
    def fetchData(self,rows):
        self.attendance_report.delete(*self.attendance_report.get_children())
        for i in rows:
                self.attendance_report.insert("",END,values=i)
    def importCsv(self):
        try:
                # Prompt user to select a CSV file
                file_path = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),parent=self.root)
                if not file_path:  # If no file selected
                        messagebox.showwarning("Warning", "No file selected")
                        return

                # Read the CSV file
                with open(file_path, mode="r") as file:
                        csv_reader = csv.reader(file)
                        self.mydata = list(csv_reader)  # Store the data in an instance variable

                # Check if CSV contains a header and skip it if needed
                if self.mydata and self.mydata[0][0].lower() == "attendance id":
                        self.mydata = self.mydata[1:]  # Skip the header row

                # Populate Treeview with data
                self.fetchData(self.mydata)

        except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def exportCsv(self):
                try:
                        if not self.mydata:  # Check if there's data to export
                                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                                return

                        # Prompt user for save location
                        file_path = filedialog.asksaveasfilename(
                        initialdir=os.getcwd(),
                        title="Save CSV",
                        defaultextension=".csv",  # Ensure .csv extension
                        filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                        parent=self.root
                        )
                        if not file_path:  # Check if no file location was selected
                                return

                        # Write data to the CSV file
                        with open(file_path, mode="w", newline="") as myfile:
                                writer = csv.writer(myfile)
                                writer.writerow(["Attendance ID", "Roll Number", "Name", "Department", "Time", "Date", "Attendance"])
                                writer.writerows(self.mydata)

                        messagebox.showinfo("Data Export", f"Your data has been exported to {os.path.basename(file_path)} successfully.")
                except Exception as e:
                        messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
    def get_cursor(self, event=""):
    # Get the currently selected row in the Treeview
        cursor_focus = self.attendance_report.focus()  # Get the item ID of the selected row
        content = self.attendance_report.item(cursor_focus)  # Get the content of the selected row
        row = content["values"]  # Extract the row values as a list

        # Check if the row exists (to avoid errors when clicking on an empty area)
        if row:
                # Set the row values into the corresponding entry fields
                self.var_attendid.set(row[2])
                self.var_attendroll.set(row[0])
                self.var_attendname.set(row[1])
                self.var_attenddep.set(row[3])
                self.var_attendtime.set(row[4])
                self.var_attenddate.set(row[5])
                self.var_attendattendance.set(row[6])  

    def update_data(self):
        try:
                # Ensure all fields are filled
                if (self.var_attendid.get() == "" or self.var_attendroll.get() == "" or
                self.var_attendname.get() == "" or self.var_attenddep.get() == "" or
                self.var_attendtime.get() == "" or self.var_attenddate.get() == "" or
                self.var_attendattendance.get() == ""):
                        messagebox.showerror("Error", "All fields are required.", parent=self.root)
                        return

                # Get the currently selected row index in the Treeview
                selected_row = self.attendance_report.focus()
                content = self.attendance_report.item(selected_row)
                row_index = self.attendance_report.index(selected_row)

                # Update the Treeview row with new values
                updated_row = [
                self.var_attendid.get(),
                self.var_attendroll.get(),
                self.var_attendname.get(),
                self.var_attenddep.get(),
                self.var_attendtime.get(),
                self.var_attenddate.get(),
                self.var_attendattendance.get(),
                ]
                self.attendance_report.item(selected_row, values=updated_row)

                # Update the corresponding row in the CSV data (mydata list)
                self.mydata[row_index] = updated_row

                messagebox.showinfo("Success", "Attendance record updated successfully.", parent=self.root)

        except Exception as e:
                messagebox.showerror("Error", f"Failed to update data: {str(e)}", parent=self.root) 
    def reset_entries(self):
    
        try:
                self.var_attendid.set("")
                self.var_attendroll.set("")
                self.var_attendname.set("")
                self.var_attenddep.set("")
                self.var_attendtime.set("")
                self.var_attenddate.set("")
                self.var_attendattendance.set("Select Status")
                messagebox.showinfo("Reset", "All fields have been reset.", parent=self.root)
        except Exception as e:
                messagebox.showerror("Error", f"Failed to reset entries: {str(e)}", parent=self.root)




if __name__ == "__main__":

    root=Tk()
    obj=Attendance(root)
    root.mainloop()                