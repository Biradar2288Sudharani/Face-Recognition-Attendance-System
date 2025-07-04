from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql
import cv2
import tkinter as tk
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")
        self.root.wm_iconbitmap("face.ico")

        # *************** Variable Creating *******************

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()
        self.var_com_search=StringVar()
        self.var_search=StringVar()
        
        # Image One
        img=Image.open(r"C:college_images\s1.png")
        img=img.resize((455,120))
        self.photoimage=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=455,height=120)
        
        # Image Two
        img1=Image.open(r"C:college_images\s2.png")
        img1=img1.resize((455,120))
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=455,y=0,width=455,height=120)
        
        # Image Three
        img2=Image.open(r"C:college_images\s4.png")
        img2=img2.resize((455,120))
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=910,y=0,width=455,height=120)

        # Background Image
        img3=Image.open(r"C:college_images\bg3.png")
        img3=img3.resize((1366,768))
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=110,width=1366,height=768)

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",33,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=50)

        back_btn=Button(title_lbl,text="Back Button",borderwidth=0,cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")  # return_login
        back_btn.place(x=1200,y=8,width=145,height=30)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1366,height=560)

# ************************************* --> Left LABEL FRAME STARTED <-- **************************************************

        # Left Main Frame----------Student Details
        Left_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_Frame.place(x=0,y=0,width=682,height=550)

        # Left Image 
        img_left=Image.open(r"C:college_images\left_image.png")
        img_left=img_left.resize((678,100))
        self.photoimage_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_Frame,image=self.photoimage_left)
        f_lbl.place(x=0,y=0,width=678,height=100)

        # ++++++++++++++++++++++++++ Current_Course Information ++++++++++++++++++++++++++++

        Current_Course_Frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_Course_Frame.place(x=2,y=100,width=675,height=110)

        # Department
        dep_label=Label(Current_Course_Frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Current_Course_Frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)   
        dep_combo["values"]=("Select Department","CSE","E&TC","CIVIL","MECH","IT","TEXT TILE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # Course
        course_label=Label(Current_Course_Frame,text="Course:",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_Course_Frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)  
        course_combo["values"]=("Select Course","Engineering","Diploma", "Nursing", "Pharmacy")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(Current_Course_Frame,text="Year:",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_Course_Frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)  
        year_combo["values"]=("Select Year","First Year","Second Year","Third year","Fourth year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semister
        semister_label=Label(Current_Course_Frame,text="Semister:",font=("times new roman",13,"bold"),bg="white")
        semister_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semister_combo=ttk.Combobox(Current_Course_Frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)  
        semister_combo["values"]=("Select Semister","1-Sem","2-Sem","3-Sem","4-Sem","5-Sem","6-Sem","7-Sem","8-Sem")
        semister_combo.current(0)
        semister_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # +++++++++++++++++++++++++++++++ Class Student Information +++++++++++++++++++++++++++++++++++

        class_student_Frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_Frame.place(x=2,y=210,width=675,height=308)
        
        # Student ID 
        studentID_label=Label(class_student_Frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_Frame,width=20,textvariable=self.var_std_id,font=("times new roman",13,"bold"))  
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name 
        studentname_label=Label(class_student_Frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_Frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))  
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Student Class Division 
        class_div_label=Label(class_student_Frame,text="Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student_Frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=18)  # textvariable=self.var_div,
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(1)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # Student Roll Number
        roll_no_label=Label(class_student_Frame,text="Roll Number:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_Frame,width=20,textvariable=self.var_rollno,font=("times new roman",13,"bold"))  
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Student Gender
        gender_label=Label(class_student_Frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_Frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)  # textvariable=self.var_gender,
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(1)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # Student Date Of Birth
        dob_label=Label(class_student_Frame,text="Date Of Birth:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_Frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))  
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Student Email ID
        email_label=Label(class_student_Frame,text="Email Id:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_Frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))  
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Student Phone Number
        phone_no_label=Label(class_student_Frame,text="Phone Number:",font=("times new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_Frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))  
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address Information
        address_label=Label(class_student_Frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_Frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))  
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Information
        teacher_label=Label(class_student_Frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_Frame,width=20,textvariable=self.var_teacher, font=("times new roman",13,"bold"))  
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # +++++++++++++++++ Radio Button Generating ++++++++++

        self.var_radio1=StringVar()
        self.var_radio2=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_Frame,variable=self.var_radio1,text="Take Photo Sample",value="YES")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student_Frame,variable=self.var_radio2,text="No Photo Sample",value="NO")
        radiobtn2.grid(row=6,column=1)

        # ++++++++++++++++++++++++++ Button Frames ++++++++++++++++++++++++++++++
        
        btn_frame=Frame(class_student_Frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=215,width=665,height=35)
        
        # Save Button Creating
        save_btn=Button(btn_frame,text="Svae",command=self.add_data_event,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        save_btn.grid(row=0,column=0)

        # ============= Bind Ctrl+S to save function ==============
        self.root.bind('<Control-s>', self.add_data_event)

        # Update Button Creating
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        update_btn.grid(padx=1,row=0,column=1)

        # Delete Button Creating
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_with_event,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        delete_btn.grid(padx=1,row=0,column=2)

        # ========== To replace delete button to keyboard delete key button ==========
        self.root.bind('<Delete>', self.delete_with_event)
        
        # Reset Button Creating
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data ,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        reset_btn.grid(padx=1,row=0,column=3)

        # ++++++++++++ Button Frame ++++++++++++

        btn_frame1=Frame(class_student_Frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=2,y=250,width=665,height=35)

        take_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=33,font=("times new roman",13,"bold"),bg="blue",fg="white")  # command=self.generate_dataset,
        take_btn.grid(row=0,column=0)
 
        update_btn=Button(btn_frame1,text="Update Photo Sample",width=33,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(padx=1,row=0,column=1)

# ************************************* --> LEFT LABEL FRAME COMPLETED <-- **************************************************

# ************************************* --> RIGHT LABEL FRAME STARTED <-- **************************************************

        # Right Label Frame----------Student Details
        Right_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=686,y=0,width=675,height=540)

        # Right Image
        img_right=Image.open(r"C:college_images\bg7.png")
        img_right=img_right.resize((683,95))
        self.photoimage_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_Frame,image=self.photoimage_right)
        f_lbl.place(x=0,y=0,width=683,height=95)

        # ++++++++++++ Search System +++++++++++++++ 

        search_Frame=LabelFrame(Right_Frame,bd=2,bg="white",relief=RIDGE,text="View Student Details And Search System",font=("times new roman",12,"bold"))
        search_Frame.place(x=2,y=95,width=683,height=64)

        search_label=Label(search_Frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=0,pady=5,sticky=W)
        
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_Frame,textvariable=self.var_com_search,font=("times new roman",13,"bold"),state="readonly",width=15)  # command=self.var_com_search,
        search_combo["values"]=("Select","Roll No","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        search_entry=ttk.Entry(search_Frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))  # command=self.var_search,
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_Frame,command=self.search_data,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_Frame,command=self.fetch_data,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        # ++++++++ Table Frame Starting +++++++++++++

        table_Frame=LabelFrame(Right_Frame,bd=2,bg="white",relief=RIDGE)
        table_Frame.place(x=2,y=160,width=665,height=360)

        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_Frame,column=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phoneno","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semister")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phoneno",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phoneno",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1) 
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

# ************************************* --> RIGHT LABEL FRAME COMPLETED <-- **************************************************

# ****************************** MYSQL DataBase Connection Part Started ************************* 

    # *******FUNCTION DECLARATION ******
    def add_data_event(self,event=None):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),                                                                                                    
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_rollno.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_photo.get(),
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            pass
    # ***************** FETCH DATA **********************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

    # *************** GET CURSOR *********************
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        data = self.student_table.item(cursor_row, "values")

        if not data:  # If data is empty, show an error and return
            messagebox.showerror("Error", "No data found! Please select a valid record.")
            return  

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])   

        if data and len(data) > 0:
            self.var_dep.set(data[0])
        else:
            print("Warning: No data returned or data is empty.")


    # ******************* UPDATE FUNCTION ********************

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Shankar2sep@",
                        database="face_recognition",
                        auth_plugin="mysql_native_password"
                    )
                    my_cursor = conn.cursor()

                    query = """UPDATE student SET Department=%s,Course=%s,Year=%s,Semister=%s,Name=%s,Division=%s,`Roll No`=%s,Gender=%s,`Date Of Birth`=%s,Email=%s,`Phone Number`=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s WHERE StudentID=%s """

                    # Prepare parameters with type conversion if necessary
                    parameters = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        int(self.var_rollno.get()) if self.var_rollno.get().isdigit() else None,
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        int(self.var_phone.get()) if self.var_phone.get().isdigit() else None,
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        int(self.var_std_id.get()) if self.var_std_id.get().isdigit() else None
                    )

                    # Print the query and parameters for debugging
                    print("Executing query:", query)
                    print("With parameters:", parameters)

                    # Execute the query
                    my_cursor.execute(query, parameters)

                    messagebox.showinfo("Success", "Student Details Successfully Updated", parent=self.root)
                    conn.commit()
                    self.fetch_data()  # Refresh the data if needed
                    conn.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"MySQL Error: {str(err)}", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)

    # *************** DELETE FUNCTION *********************

    def delete_with_event(self,event=None): 
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
                    my_cursor=conn.cursor()
                    sql="delete from student Where StudentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            pass
    # *************** RESET FUNCTION *********************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semister")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_rollno.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ********************** GENERATE DATASET OR TAKE PHOTO SAMPLES *****************************
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get() == "" or self.var_std_id.get() == "": 
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                query = """UPDATE student SET Department=%s, Course=%s,Year=%s, Semister=%s, Name=%s, Division=%s, `Roll No`=%s, Gender=%s, `Date Of Birth`=%s, Email=%s, `Phone Number`=%s, Address=%s, Teacher=%s, PhotoSampleStatus=%s WHERE StudentID=%s """

                # Prepare parameters with type conversion if necessary
                parameters = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        int(self.var_rollno.get()) if self.var_rollno.get().isdigit() else None,
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        int(self.var_phone.get()) if self.var_phone.get().isdigit() else None,
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        int(self.var_std_id.get()) if self.var_std_id.get().isdigit() else None
                    )
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ************************* Load Predifined Data On Face Frontals From opencv *****************************
                face_classifier = cv2.CascadeClassifier(r"C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3
                    # minimum neighbour = 5

                    for (x,y,w,h) in faces:
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
                        file_name_path=r"C:data\."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Datasets Completed !!!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    # *********** Search Function Creation **************
    def search_data(self):
        # Check for empty fields
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select a search option and enter a search term.", parent=self.root)
        else:
            try:
                # Mapping dropdown options to database column names
                column_mapping = {"Roll No": "Roll No", "Phone Number": "Phone Number"}

                # Get the selected search column
                search_column = column_mapping.get(self.var_com_search.get())

                # Validate the selected column
                if not search_column:
                    messagebox.showerror("Error", "Invalid search option selected.", parent=self.root)
                    return

                # Establish the database connection
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Shankar2sep@",
                    database="face_recognition",
                    auth_plugin="mysql_native_password"
                )
                my_cursor = conn.cursor()

                # Construct a safe SQL query
                query = f"SELECT * FROM student WHERE `{search_column}` LIKE %s"
                search_term = f"%{self.var_search.get()}%"
                print(f"Executing query: {query} with search term: {search_term}")  # Debugging statement
                my_cursor.execute(query, (search_term,))

                # Fetch and display data
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())  # Clear current data
                    for row in data:
                        # Ensure `row` matches the number of columns in `student_table`
                        self.student_table.insert("", "end", values=row)
                else:
                    messagebox.showinfo("Info", "No records found matching the search criteria.", parent=self.root)

                # Commit and close connection
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

if __name__== " __main__ ":
    root=Tk()
    obj=Student(root)
    root.mainloop() 
