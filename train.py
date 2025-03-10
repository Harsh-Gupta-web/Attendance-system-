from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face")

#title
        title_lbl=Label(self.root, text="TRAIN DATA SET",font=("times new roman", 35, "bold"), bg="white", fg="RED")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        imgtop_img=Image.open(r"images\17.jpg")
        imgtop_img=imgtop_img.resize((1530,325),Image.BICUBIC)
        self.photoimgtop_img=ImageTk.PhotoImage(imgtop_img)

        f_lbl=Label(self.root,image=self.photoimgtop_img)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        imgbottom_img=Image.open(r"images\17.jpg")
        imgbottom_img=imgtop_img.resize((1530,325),Image.BICUBIC)
        self.photoimgbottom_img=ImageTk.PhotoImage(imgbottom_img)

        f_lbl=Label(self.root,image=self.photoimgbottom_img)
        f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
    # Train the classifier and save 
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")                  

        







if __name__ == "__main__":

    root=Tk()
    obj=Train(root)
    root.mainloop()                