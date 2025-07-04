import re
import tkinter
from tkinter import *
import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1365x768+0+0")
        self.root.title("Register")
        
        # *************** Variable Declaration *****************
        self.var_fname = tk.StringVar()
        self.var_lname = tk.StringVar()
        self.var_contact = tk.StringVar(value="+91 ")  # Add a space after +91
        self.var_email = tk.StringVar()
        self.var_sec_que = tk.StringVar()
        self.var_sec_ans = tk.StringVar()
        self.var_pas = tk.StringVar()
        self.var_conf_pas = tk.StringVar()
        self.var_check=tk.StringVar()
        # ** Separate Password Visibility Toggles **
        self.show_password = False
        self.show_confirm_password = False
        
        # ************* Background Image ***************
        img = Image.open(r"C:college_images\bg3.png").resize((1366, 780))
        self.photoimage = ImageTk.PhotoImage(img)
        tk.Label(self.root, image=self.photoimage).place(x=0, y=0, width=1366, height=730)
        
        # ************* Left Image ***************
        left_img = Image.open(r"C:college_images\home_bg2.png").resize((390, 500))
        self.photoimage1 = ImageTk.PhotoImage(left_img)
        tk.Label(self.root, image=self.photoimage1).place(x=110, y=100, width=390, height=500)
        
        # ************* Main Frame ***********
        frame = tk.Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=750, height=500)
        
        tk.Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white").place(x=10, y=10)
        
        # Row 1 - Name
        tk.Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white").place(x=30, y=60)
        ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15)).place(x=30, y=90, width=250)
        
        tk.Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place(x=350, y=60)
        ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15)).place(x=350, y=90, width=250)
        
        # Row 2 - Contact & Email
        self.contact_label = tk.Label(frame, text="Contact Number", font=("times new roman", 15, "bold"), bg="white")
        self.contact_label.place(x=30, y=150)

        # Entry for Contact Number
        self.contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        self.contact_entry.place(x=30, y=180, width=250)

        # Bind events to prevent deleting +91
        self.contact_entry.bind("<FocusIn>", self.focus_in_contact)
        self.contact_entry.bind("<KeyPress>", self.limit_contact_entry)

        tk.Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white").place(x=350, y=150)
        ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15)).place(x=350, y=180, width=250)
        
        # Row 3 - Security Question
        tk.Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white").place(x=30, y=240)
        self.combo_security_question = ttk.Combobox(frame, textvariable=self.var_sec_que, font=("times new roman", 15), state="readonly")
        self.combo_security_question["values"] = ("Select", "Your Birth Place", "Your Best Friend's Name", "Your Hobby")
        self.combo_security_question.place(x=30, y=270, width=250)
        self.combo_security_question.current(0)
        
        tk.Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white").place(x=350, y=240)
        ttk.Entry(frame, textvariable=self.var_sec_ans, font=("times new roman", 15)).place(x=350, y=270, width=250)
        
        # ************** Password Fields ***************
        tk.Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=30, y=330)
        self.password_entry = ttk.Entry(frame, textvariable=self.var_pas, font=("times new roman", 15), show="*")
        self.password_entry.place(x=30, y=360, width=250)
        self.toggle_btn1 = tk.Button(frame,text="Show", command=self.toggle_password, bg="black", fg="white", relief="flat")
        self.toggle_btn1.place(x=250, y=360, width=33, height=28)

        tk.Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=350, y=330)
        self.confirm_pass_entry = ttk.Entry(frame, textvariable=self.var_conf_pas, font=("times new roman", 15), show="*")
        self.confirm_pass_entry.place(x=350, y=360, width=250)
        self.toggle_btn2 = tk.Button(frame,text="Show", command=self.toggle_confirm_password, bg="black", fg="white", relief="flat")
        self.toggle_btn2.place(x=570, y=360, width=33, height=28)

        # ************ Check Button ***************
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree to the Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0, bg="white")
        checkbtn.place(x=30, y=400)
        
        # ********* Register Button *************
        img3=Image.open(r"C:college_images\register.png")
        img3=img3.resize((120,80))
        self.photoimage3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimage3,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=440,width=120,height=40)        

        # ********* Login Button *************
        img4=Image.open(r"C:college_images\login.png")
        img4=img4.resize((120,80))
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimage4,borderwidth=0,cursor="hand2")
        b1.place(x=350,y=440,width=120,height=60)

    def focus_in_contact(self, event):
        """ Ensures cursor starts after +91 """
        if self.var_contact.get() == "+91 ":
            self.contact_entry.icursor(len("+91 "))  # Move cursor after +91

    def limit_contact_entry(self, event):
        """ Prevents user from deleting +91 and ensures only numbers can be entered """
        if len(self.var_contact.get()) < 4:  # If user tries to remove "+91 "
            self.var_contact.set("+91 ")  # Reset it back
            self.contact_entry.icursor(len("+91 "))  # Move cursor after "+91 "
        elif event.keysym == "BackSpace" and self.contact_entry.index(tk.INSERT) <= 4:
            return "break"  # Block backspace before "+91 "
        elif not event.char.isdigit() and event.keysym not in ("BackSpace", "Left", "Right", "Delete"):
            return "break"  # Allow only numbers

    def toggle_password(self):
        """Toggles visibility for the Password field only."""
        if self.show_password:
            self.password_entry.config(show="*")
            self.toggle_btn1.config(text="Show")
        else:
            self.password_entry.config(show="")
            self.toggle_btn1.config(text="Hide")
        self.show_password = not self.show_password

    def toggle_confirm_password(self):
        """Toggles visibility for the Confirm Password field only."""
        if self.show_confirm_password:
            self.confirm_pass_entry.config(show="*")
            self.toggle_btn2.config(text="Show")
        else:
            self.confirm_pass_entry.config(show="")
            self.toggle_btn2.config(text="Hide")
        self.show_confirm_password = not self.show_confirm_password

    def validate_data(self):
        # Validate First Name - Should only contain letters
        if not self.var_fname.get().isalpha():
            messagebox.showerror("Invalid Input", "First name should contain only letters!", parent=self.root)
            return False

        # Validate Last Name - Should only contain letters
        if not self.var_lname.get().isalpha():
            messagebox.showerror("Invalid Input", "Last name should contain only letters!", parent=self.root)
            return False
        
        # Validate Contact Number - Should be in the format +91 followed by exactly 10 digits
        contact_pattern = r'^\+91\s\d{10}$'
        if not re.match(contact_pattern, self.var_contact.get()):
            messagebox.showwarning("Invalid Input", "Contact number should be in the format +91 XXXXXXXXXX", parent=self.root)
            return False

        # Validate Email - Should be in a valid email format
        email_pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.var_email.get()):
            messagebox.showerror("Invalid Input", "Invalid Email Format!", parent=self.root)
            return False

        # Validate Security Question Answer - Should contain only letters
        if not self.var_sec_ans.get().isalpha():
            messagebox.showerror("Invalid Input", "Security answer should contain only letters!", parent=self.root)
            return False

        # Validate Password - Must have at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(password_pattern, self.var_pas.get()):
            messagebox.showerror("Invalid Input", "Password must be at least 8 characters long with one uppercase, one lowercase, one number, and one special character!", parent=self.root)
            return False
        
        # Validate Confirm Password - Should match the password
        if self.var_pas.get() != self.var_conf_pas.get():
            messagebox.showerror("Invalid Input", "Passwords & Confirm Password do not match!", parent=self.root)
            return False
        
        # Check if the user has agreed to the terms and conditions
        if self.var_check.get() == 0:
            messagebox.showerror("Warning", "Please agree to the terms and conditions!", parent=self.root)
            return False
        return True
    
    def register_data(self):
        # First, check if any field is empty
        required_fields = [
            self.var_fname.get(),
            self.var_lname.get(),
            self.var_contact.get(),
            self.var_email.get(),
            self.var_sec_que.get(),
            self.var_sec_ans.get(),
            self.var_pas.get(),
            self.var_conf_pas.get(),
        ]      
        if any(field.strip() == "" or field == "Select" for field in required_fields):
            messagebox.showerror("Warning", "All fields are required!", parent=self.root)
            return False  # Stop validation if any field is empty
        # First, validate all the fields
        if not self.validate_data():
            return  # If validation fails, exit the function and do not proceed
        elif self.var_pas.get() != self.var_conf_pas.get():
            messagebox.showerror("Warning", "Password and Confirm Password must be the same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Warning", "Please agree to the terms and conditions", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()

                query = "SELECT * FROM register WHERE EmailID=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Warning", "User already exists, please try another email!", parent=self.root)
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
                    messagebox.showinfo("Success","User Registered Successfully ✅", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error Code: {err.errno}, Message: {err.msg}", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = Register(root)
    root.mainloop()