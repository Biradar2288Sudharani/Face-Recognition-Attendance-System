import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
from  time import strftime
from  datetime import datetime
from Main1 import F_R_S

def main():
    win=Tk()  
    app=Login(win)
    win.mainloop()

# =========================================================================================================================================================
class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1365x768+0+0")
        self.root.title("Login")
        self.root.wm_iconbitmap("face.ico")

        # ******** Background Image Creation **********
        img = Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\home_bg.png")
        img = img.resize((1366, 780))
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=1366, height=730)

        # ******* Frame Creation **********
        frame=Frame(self.root,bg="black")
        frame.place(x=480,y=150,width=300,height=400)

        img1 = Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\logo.png")
        img1 = img1.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=580, y=150, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="red",bg="black")
        get_str.place(x=75,y=90)

        # ********* User and Password Label Creation *************
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=60, y=140)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=30,y=170,width=240)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=60, y=210)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=30,y=240,width=240)

        # ****** Username image and password image creation *********
        img2 = Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\username.png")
        img2 = img2.resize((25, 25))
        self.photoimage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=510, y=290, width=25, height=25)

        img3 = Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\pass.png")
        img3 = img3.resize((25, 25))
        self.photoimage3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimage3)
        f_lbl.place(x=510, y=360, width=25, height=25)

        # ******** Logon Button Creation ************
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=2,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=90,y=290,width=100,height=30)

         # ******** New User Register Button Creation ************
        newregbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        newregbtn.place(x=10,y=330,width=160)

        # ******** Forget Password Button Creation ************
        forgetbtn=Button(frame,command=self.forgot_password,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        forgetbtn.place(x=10,y=350,width=160)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    # **************** Login Function Creation *****************
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "sudharanibiradar970@gmail.com" and self.txtpass.get() == "Shankar2sep@":
            messagebox.showinfo("Success", "Welcome")
        else:
            try:
                # Database connection
                conn = mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()

                # Validate user credentials
                my_cursor.execute("SELECT * FROM register WHERE EmailID=%s AND Password=%s", (
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                            ))
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid Username and Password...Please Try Again!")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main:
                        self.new_window = Toplevel(self.root)  # Create new window
                        self.app = F_R_S(self.new_window)      # Pass the new window to the F_R_S class

                conn.close()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
    
    #  ************ Reset Password Function ***************
    def reset(self):
        if self.combo_security_question.get() == "Select":
            messagebox.showerror("Error", "Select Security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            try:
                # Establish database connection
                conn = mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()

                # Query to validate security question and answer
                query = ("SELECT * FROM register WHERE `EmailID`=%s AND `Security Question`=%s AND `Security Answer`=%s")
                value = (self.txtuser.get(), self.combo_security_question.get(), self.txt_security.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                # Handle query results
                if row is None:
                    messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
                else:
                    # Update the password
                    update_query = "UPDATE register SET Password=%s WHERE EmailID=%s"
                    update_value = (self.txt_newpass.get(), self.txtuser.get())
                    my_cursor.execute(update_query, update_value)
                    conn.commit()

                    # Inform the user and close the reset window
                    messagebox.showinfo("Info", "Your password has been reset. Please log in with the new password.", parent=self.root2)
                    self.root2.destroy()

                conn.close()

            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}", parent=self.root2)


    # ********** Forget Password Function Creation*************
    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email ID to reset password")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()

            query=("select * from register where EmailID=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("300x400+480+150")

                # ***** Forgot Frame Label Creation *****
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="black")
                l.place(x=0,y=10,relwidth=1)
                 
                # **** In forget password label creation 
                # **** Row 1
                security_question = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_question.place(x=30, y=100)
                
                # **** Row 2
                self.combo_security_question = ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")   # textvariable=self.sec_que, 
                self.combo_security_question["values"] = ("Select", "Your Birth Place", "Your Best Friend's Name", "Your Hobby")
                self.combo_security_question.place(x=30, y=130, width=250)
                self.combo_security_question.current(0)
                
                # **** Row 3
                security_answer = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_answer.place(x=30, y=160)
                
                # **** Row 4
                self.txt_security = ttk.Entry(self.root2,font=("times new roman", 15, "bold"))  # textvariable=self.sec_ans, 
                self.txt_security.place(x=30, y=190, width=250)
                
                # **** Row 5
                new_password= Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=30, y=220)
                
                # **** Row 6
                self.txt_newpass = ttk.Entry(self.root2,font=("times new roman", 15, "bold"))  # textvariable=self.sec_ans, 
                self.txt_newpass.place(x=30, y=250, width=250)

                # ****** Reset Button Creation **********
                btn=Button(self.root2,command=self.reset,text="Reset",font=("times new roman", 15, "bold"),fg="white",bg="green")
                btn.place(x=80,y=290)

# =========================================================================================================================================================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1365x768+0+0")
        self.root.title("Register")
        self.root.wm_iconbitmap("face.ico")

        # *************** Variable Declaration *****************
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_sec_que = StringVar()
        self.var_sec_ans = StringVar()
        self.var_pas = StringVar()
        self.var_conf_pas = StringVar()
        
        # ************* Background Image ***************
        img = Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\bg5.png")
        img = img.resize((1366, 780))
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=1366, height=730)
        
        # ************* Left Image ***************
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\home_bg2.png")
        left_lbl = Label(self.root, image=self.bg)
        left_lbl.place(x=100, y=100, width=400, height=500)

        # *********** Main Frame ***********
        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=750, height=500)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=10, y=10)

        # Row 1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=30, y=60)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=30, y=90, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=350, y=60)
        l_name_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        l_name_entry.place(x=350, y=90, width=250)

        # Row 2
        contact = Label(frame, text="Contact Number", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=30, y=150)
        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        contact_entry.place(x=30, y=180, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=350, y=150)
        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        email_entry.place(x=350, y=180, width=250)

        # Row 3
        security_question = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_question.place(x=30, y=240)
        self.combo_security_question = ttk.Combobox(frame, textvariable=self.var_sec_que, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_question["values"] = ("Select", "Your Birth Place", "Your Best Friend's Name", "Your Hobby")
        self.combo_security_question.place(x=30, y=270, width=250)
        self.combo_security_question.current(0)

        security_answer = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_answer.place(x=350, y=240)
        security_answer_entry = ttk.Entry(frame, textvariable=self.var_sec_ans, font=("times new roman", 15, "bold"))
        security_answer_entry.place(x=350, y=270, width=250)

        # Row 4
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=30, y=330)
        password_entry = ttk.Entry(frame, textvariable=self.var_pas, font=("times new roman", 15, "bold"))
        password_entry.place(x=30, y=360, width=250)

        confirm_password = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_password.place(x=350, y=330)
        confirm_password_entry = ttk.Entry(frame, textvariable=self.var_conf_pas, font=("times new roman", 15, "bold"))
        confirm_password_entry.place(x=350, y=360, width=250)

        # ************ Check Button ***************
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree to the Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0, bg="white")
        checkbtn.place(x=30, y=400)

        # ********* Register Button *************
        img1=Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\register.png")
        img1=img1.resize((120,80))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=440,width=120,height=40)
        

        # ********* Login Button *************
        img2=Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\login.png")
        img2=img2.resize((120,80))
        self.photoimage2=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimage2,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=350,y=440,width=120,height=60)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_sec_que.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pas.get() != self.var_conf_pas.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()

                query = "SELECT * FROM register WHERE EmailID=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email!")
                else:
                    my_cursor.execute(
                        "INSERT INTO register (`First Name`, `Last Name`, `Contact Number`, `EmailID`, `Security Question`, `Security Answer`, `Password`, `Confirm Password`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                                                                                                                                        self.var_fname.get(),
                                                                                                                                                                                                                        self.var_lname.get(),
                                                                                                                                                                                                                        self.var_contact.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_sec_que.get(),
                                                                                                                                                                                                                        self.var_sec_ans.get(),
                                                                                                                                                                                                                        self.var_pas.get(),
                                                                                                                                                                                                                        self.var_conf_pas.get()
                                                                                                                                                                                                                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error Code: {err.errno}, Message: {err.msg}")
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}")

    # ******** Login Button Functions ********
    def return_login(self):
        self.root.destroy()   

# Run the application
if __name__ == "__main__":
    main()
