import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

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
        img = Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\bg3.png")
        img = img.resize((1366, 780))
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=1366, height=730)
        
        # ************* Left Image ***************
        

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
        b1=Button(frame,image=self.photoimage2,borderwidth=0,cursor="hand2")
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
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Shankar2sep@",
                    database="face_recognition",
                    auth_plugin="mysql_native_password"
                )
                my_cursor = conn.cursor()

                query = "SELECT * FROM register WHERE EmailID=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email!")
                else:
                    my_cursor.execute(
                        "INSERT INTO register (`First Name`, `Last Name`, `Contact Number`, `EmailID`, `Security Question`, `Security Answer`, `Password`, `Confirm Password`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_sec_que.get(),
                            self.var_sec_ans.get(),
                            self.var_pas.get(),
                            self.var_conf_pas.get()
                        )
                    )
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error Code: {err.errno}, Message: {err.msg}")
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}")

# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
