from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class HelpProgram:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face")

        # Title
        title_lbl = Label(
            self.root,
            text="Help & Support",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="darkblue"
        )
        title_lbl.pack(fill=X)

        # Background Image
        img3 = Image.open(r"images\24.png")
        img3 = img3.resize((1530, 790), Image.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=50, width=1530, height=710)

        # Content Frame
        content_frame = Frame(bg_img, bg="white", bd=2, relief=RIDGE)
        content_frame.place(x=300, y=80, width=960, height=340)

        # Help Text
        help_text = (
            "Welcome to the Help Section!\n\n"
            "For assistance, you can contact our support team:\n"
            "Email: harshgupta@gmail.com\n"
            "Phone: 9899266556\n\n"
            "Thank you for using our application!"
        )

        help_label = Label(
            content_frame,
            text=help_text,
            font=("times new roman", 14),
            bg="white",
            fg="darkblue",
            
        )
        help_label.place(x=280,y=50 ,width=400,height=200)

       

if __name__ == "__main__":
    root = Tk()
    app = HelpProgram(root)
    root.mainloop()
