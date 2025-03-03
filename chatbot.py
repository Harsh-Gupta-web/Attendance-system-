from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("730x620+0+0")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img1 = Image.open(r"images\29.jpeg")
        img1 = img1.resize((200, 70), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,image=self.photoimg1,compound=LEFT,text="CHAT ME",font=("arial",30,"bold"),fg="green",bg="white")
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=("arial",14,"bold"),fg="green",bg="white")
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,width=40,textvariable=self.entry,font=("times new roman",16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",font=("arial",15,"bold"),command=self.send,bg="green",width=8)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clar=Button(btn_frame,text="Clear",font=("arial",15,"bold"),command=self.clear,bg="red", fg="white",width=8)
        self.clar.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=("arial",14,"bold"),fg="red",bg="white")
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

#====================================FUNCTION============================================
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    
    
    
    
    
    def send(self):
        user_input = self.entry.get().lower() 
        self.text.insert(END, '\n' + "You: " + user_input)
        self.text.yview(END)

        if(user_input==""):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg="red")
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg="red")

        if(user_input=="hi"):
            self.text.insert(END,'\n'+'Bot:Hi')
        
        elif (user_input == "what is this project about"):
            self.text.insert(END, '\n' + "Bot: This is a Face Recognition Attendance System project designed to mark attendance using facial recognition technology.")
        elif (user_input == "who developed this project"):
            self.text.insert(END, '\n' + "Bot: This project was developed by Harsh Gupta.")
        elif (user_input == "how does facial recognition work"):
            self.text.insert(END, '\n' + "Bot: Facial recognition uses machine learning algorithms to identify and verify a person by analyzing their facial features.")
        elif (user_input == "what programming language is used in this project"):
            self.text.insert(END, '\n' + "Bot: The project is implemented using Python.")

        # Technical Questions
        elif (user_input == "what libraries are used in this project"):
            self.text.insert(END, '\n' + "Bot: This project uses libraries like OpenCV for facial recognition, Tkinter for GUI, PIL for image handling, and NumPy for numerical operations.")
        elif (user_input == "how is attendance recorded"):
            self.text.insert(END, '\n' + "Bot: Attendance is recorded in a CSV file with the person's name, ID, and timestamp when their face is recognized.")
        elif (user_input == "can i use this project for my organization"):
            self.text.insert(END, '\n' + "Bot: Yes, you can customize this project to fit your organization's requirements.")
        elif (user_input == "what database is used in this project"):
            self.text.insert(END, '\n' + "Bot: MySQL is used to store and retrieve user data in this project.")

        # Usage Questions
        elif (user_input == "how do i start the application"):
            self.text.insert(END, '\n' + "Bot: Run the main Python file using your Python interpreter. It will open the application window.")
        elif (user_input == "how do i add a new face"):
            self.text.insert(END, '\n' + "Bot: Navigate to the 'Train Data' section and capture the images of the new user. Then, train the model to recognize the face.")
        elif (user_input == "how do i export attendance"):
            self.text.insert(END, '\n' + "Bot: Click on the 'Export' button in the application. It will save the attendance data to a CSV file.")
        elif (user_input == "what happens if the face is not recognized"):
            self.text.insert(END, '\n' + "Bot: If the face is not recognized, the system will not mark attendance. Ensure the face is registered and the model is trained.")

        # Error Handling Questions
        elif (user_input == "what if the application crashes"):
            self.text.insert(END, '\n' + "Bot: Check for any error messages in the console. Most common issues are missing dependencies or incorrect database configurations.")
        elif (user_input == "why is my face not recognized"):
            self.text.insert(END, '\n' + "Bot: Make sure your face is properly captured during the registration process and that the model is trained with sufficient data.")
        elif (user_input == "what if the csv export fails"):
            self.text.insert(END, '\n' + "Bot: Ensure you have the necessary permissions to write to the selected directory and that the data exists before exporting.")

        # Advanced Questions
        elif (user_input == "can i use this with multiple cameras"):
            self.text.insert(END, '\n' + "Bot: Yes, you can modify the code to support multiple camera inputs.")
        elif (user_input == "how accurate is this system"):
            self.text.insert(END, '\n' + "Bot: The accuracy depends on the quality of the training data and the environment. Good lighting and a clear view of the face improve accuracy.")
        elif (user_input == "can this system detect masks"):
            self.text.insert(END, '\n' + "Bot: The current system does not support mask detection. However, you can integrate a mask detection module using pre-trained models.")
        elif (user_input == "is this system secure"):
            self.text.insert(END, '\n' + "Bot: The system is designed for basic attendance purposes. For secure applications, consider encrypting sensitive data.")

        # Customization Questions
        elif (user_input == "can i change the design of the application"):
            self.text.insert(END, '\n' + "Bot: Yes, you can modify the Tkinter GUI code to customize the appearance of the application.")
        elif (user_input == "can i add additional features"):
            self.text.insert(END, '\n' + "Bot: Absolutely! Features like email notifications, SMS alerts, or real-time reporting can be added with some extra coding.")
        elif (user_input == "how do i change the database"):
            self.text.insert(END, '\n' + "Bot: You can modify the database connection settings in the code to use another database like SQLite or PostgreSQL.")

        # Default Response
        else:
            self.text.insert(END, '\n' + "Bot: I'm sorry, I don't understand that.")

        self.entry1.delete(0, END)  # Clear the entry field after sending





if __name__ == "__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()        