from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql
import cv2
import mysql.connector
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")
        
        # Title name given
        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=50)
        
        # Top Image Creating
        img_top=Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\Images\train1.png")
        img_top=img_top.resize((1366,330))
        self.photoimage_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=50,width=1366,height=330)
         
        # Train Data Button Creating
        btn_lbl=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times of new roman",30,"bold"),bg="black",fg="blue")
        btn_lbl.place(x=0,y=370,width=1366,height=50)

        # Bottom Image Creating
        img_bottom=Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\Images\train3.png")
        img_bottom=img_bottom.resize((1366,295))
        self.photoimage_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimage_bottom)
        f_lbl.place(x=0,y=420,width=1366,height=295)
    
    def train_classifier(self):
        data_dir=("C:\\Users\\lenovo\\Desktop\\Face_Recognisation_System\\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   # Gray Scale Image
            imageNp=np.array(img,)
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        # *************** Train the Classifier and Save them ******************
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("C:\\Users\\lenovo\\Desktop\\Face_Recognisation_System\\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!!")
      

#if __name__== " __main__ ":
root=Tk()
obj=Train(root)
root.mainloop()