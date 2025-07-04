import tkinter
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import mysql
import os
import tkinter as tk
from  time import strftime
from  datetime import datetime
from student1 import Student
from train1 import Train
from face_recognition1 import Face_Recognition
from attendance1 import Attendance
from Avg_Atten import AttendanceAnalyzer
from help1 import Help
from timetable import Time_Table

class F_R_S:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x768+0+0")
        self.root.title("Face Recognization System")
        self.root.wm_iconbitmap("face.ico")
 
        # Image One
        img=Image.open(r"C:college_images\h.png")
        img=img.resize((455,110))
        self.photoimage=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=455,height=110)
        
        # Image Two
        img1=Image.open(r"C:college_images\h1.png")
        img1=img1.resize((455,110))
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=455,y=0,width=455,height=110)
        
        # Image Three
        img2=Image.open(r"C:college_images\image2.png")
        img2=img2.resize((457,110))
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=910,y=0,width=457,height=110)

        # Background Image
        img3=Image.open(r"C:college_images\bg2.png")
        img3=img3.resize((1366,768))
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=110,width=1366,height=700)
        
        # Title Label Creation

        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1362,height=55)

        # Quote Label Creation

        quote_lbl=Label(bg_img,text="Self confidance is superpower! Once you start believe in yourself, The magic starts happening",font=("times new roman",25,"bold"),bg="black",fg="red")
        quote_lbl.place(x=0,y=550,width=1362,height=50)

        # ************ Time Logic Creation **************

        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="black",foreground="red")  # command=self.time,
        lbl.place(x=0,y=0,width=110,height=40) 
        time()

        # Student Details Button
        img4=Image.open(r"C:college_images\sd.png")
        img4=img4.resize((200,200))
        self.photoimage4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimage4,cursor="hand2", command=self.student_details)  # command=self.student_details,
        b1.place(x=130,y=70,width=200,height=200)
        b1_lbl=Button(bg_img,text="Student Details",cursor="hand2", command=self.student_details,font=("times new roman",23,"bold"),bg="darkblue",fg="white")  # command=self.student_details,
        b1_lbl.place(x=130,y=235,width=200,height=40)

        # Detect Button (FACE DETECTOR)
        img5=Image.open(r"C:college_images\fr.png")
        img5=img5.resize((200,200))
        self.photoimage5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.face_data)  # command=self.face_data
        b1.place(x=430,y=70,width=200,height=200)

        b1_lbl=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",23,"bold"),bg="darkblue",fg="white")  # command=self.face_data,
        b1_lbl.place(x=430,y=231,width=200,height=40)

        # Attendance Button (ATTENDANCE)
        img6=Image.open(r"C:college_images\atten.png")
        img6=img6.resize((200,200))
        self.photoimage6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimage6,cursor="hand2",command=self.attnedance_data)
        b1.place(x=730,y=70,width=200,height=200)

        b1_lbl=Button(bg_img,text="Attendance",cursor="hand2",command=self.attnedance_data,font=("times new roman",23,"bold"),bg="darkblue",fg="white")
        b1_lbl.place(x=730,y=230,width=200,height=40)

        # Time Table 
        img7=Image.open(r"C:college_images\timetable.png")
        img7=img7.resize((200,200))
        self.photoimage7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimage7,cursor="hand2",command=self.timetable_data)
        b1.place(x=1030,y=70,width=200,height=200)

        b1_lbl=Button(bg_img,text="Time Table",cursor="hand2",command=self.timetable_data,font=("times new roman",23,"bold"),bg="darkblue",fg="white")
        b1_lbl.place(x=1030,y=230,width=200,height=40)

        # Train Data Button 
        img8=Image.open(r"C:college_images\train.png")
        img8=img8.resize((200,200))
        self.photoimage8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.train_data)  #,command=self.train_data
        b1.place(x=130,y=300,width=200,height=200)

        b1_lbl=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",23,"bold"),bg="darkblue",fg="white") # command=self.train_data,
        b1_lbl.place(x=130,y=490,width=200,height=40)

        # Photos Button 
        img9=Image.open(r"C:college_images\photos.png")
        img9=img9.resize((200,200))
        self.photoimage9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.open_img)
        b1.place(x=430,y=300,width=200,height=200)

        b1_lbl=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",23,"bold"),bg="darkblue",fg="white")
        b1_lbl.place(x=430,y=490,width=200,height=40)

        # Average Attendance Button 
        img10=Image.open(r"C:college_images\graph1.png")
        img10=img10.resize((200,200))
        self.photoimage10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimage10,cursor="hand2",command=self.check_atten)
        b1.place(x=730,y=300,width=200,height=200)

        b1_lbl=Button(bg_img,text="Average Atten",cursor="hand2",command=self.check_atten,font=("times new roman",23,"bold"),bg="darkblue",fg="white")
        b1_lbl.place(x=730,y=490,width=200,height=40)

        # Exit Button 
        img11=Image.open(r"C:college_images\exit.png")
        img11=img11.resize((200,200))
        self.photoimage11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimage11,cursor="hand2",command=self.iExit)
        b1.place(x=1030,y=300,width=200,height=200)

        b1_lbl=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",23,"bold"),bg="darkblue",fg="white")
        b1_lbl.place(x=1030,y=490,width=200,height=40)

        # Help Desktop Button Creation
        b1_lbl=Button(bg_img,text="Help Desktop",cursor="hand2",command=self.help_data,font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_lbl.place(x=1232,y=56,width=130,height=30)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return        

    # *************Functions Buttons***************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 

    def attnedance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 

    def timetable_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Time_Table(self.new_window)  

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 

    def check_atten(self):
        self.new_window = tk.Toplevel(self.root)  # Creating a new window
        file_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\M2.csv"  # Ensure file path is correct
        self.app = AttendanceAnalyzer(self.new_window,file_path)

if __name__== " __main__ ":
    root=Tk()
    obj=F_R_S(root)
    root.mainloop()