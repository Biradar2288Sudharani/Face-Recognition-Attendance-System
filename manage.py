import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
from time import strftime
from datetime import datetime
import re  # Import regular expressions for validation
from register1 import Register
from Main1 import F_R_S  # Assuming this is your main application file

def main():
    win = Tk()
    app = Login(win)
    win.mainloop()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1365x768+0+0")
        self.root.title("Login")
        self.root.wm_iconbitmap("face.ico")

        # Background Image
        img = Image.open(r"C:college_images\home_bg.png")
        img = img.resize((1366, 780))
        self.photoimage = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=1366, height=730)

        # Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=480, y=150, width=300, height=400)

        img1 = Image.open(r"C:college_images\logo.png")
        img1 = img1.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=580, y=150, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="red", bg="black")
        get_str.place(x=75, y=90)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=60, y=140)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=30, y=170, width=240)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=60, y=210)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=30, y=240, width=240)

        # Show/Hide Password Checkbox
        self.show_password_var = IntVar()
        show_pass_check = Checkbutton(frame, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility, font=("times new roman", 10, "bold"), bg="black", fg="white", activebackground="black", activeforeground="white")
        show_pass_check.place(x=30, y=270)

        # Icons for username and password
        img2 = Image.open(r"C:college_images\username.png")
        img2 = img2.resize((25, 25))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimage2).place(x=510, y=290, width=25, height=25)

        img3 = Image.open(r"C:college_images\pass.png")
        img3 = img3.resize((25, 25))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimage3).place(x=510, y=360, width=25, height=25)

        # Buttons
        Button(frame, command=self.login_with_event, text="Login", font=("times new roman", 15, "bold"), bd=2, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red").place(x=90, y=300, width=100, height=30)
        Button(frame, command=self.register_window, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red").place(x=10, y=340, width=160)
        Button(frame, command=self.forgot_password, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red").place(x=10, y=360, width=160)
        
        self.root.bind('<Return>', self.login_with_event)
        
    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")

    # ************************************ Validation of username and password*****************
    def validate_email(self, email):
        """ Validate Email Format """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)

    def validate_password(self, password):
        """ Validate Password Complexity """
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):  # At least one uppercase
            return False
        if not re.search(r"[a-z]", password):  # At least one lowercase
            return False
        if not re.search(r"[0-9]", password):  # At least one digit
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # At least one special character
            return False
        return True
    
    # ******************* Register Window Accessing on login page ******************
    def register_window(self):
        self.new_window = Toplevel(self.root)
        # Implement the Register class accordingly
        self.app = Register(self.new_window)

    def login_with_event(self, event=None):
        """ Login Validation and Database Check """
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        if not self.validate_email(username):
            messagebox.showerror("Error", "Invalid Email Format")
            return

        if not self.validate_password(password):
            messagebox.showerror("Error", "Password must contain at least:\n - One uppercase letter\n - One lowercase letter\n - One digit\n - One special character\n - Minimum 8 characters")
            return

        if username == "sudharanibiradar970@gmail.com" and password == "Shankar2sep@":
            messagebox.showinfo("Success", "Welcome")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Shankar2sep@", database="face_recognition", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE EmailID=%s AND Password=%s", (username, password))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username and Password...Please Try Again!")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = F_R_S(self.new_window)
                conn.close()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")

    # ******************** Forgot  Password Creation ************
    def forgot_password(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the Email ID to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Shankar2sep@", database="face_recognition", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE EmailID=%s", (self.txtuser.get(),))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter the valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("330x450+450+150")
                self.root2.configure(bg="white")

                Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white").pack(pady=10)

                Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white").pack(pady=5)
                self.combo_security_question = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_question["values"] = ("Select", "Your Birth Place", "Your Best Friend's Name", "Your Hobby")
                self.combo_security_question.pack(pady=5)
                self.combo_security_question.current(0)

                Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white").pack(pady=5)
                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.pack(pady=5)

                Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white").pack(pady=5)
                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"), show="*")
                self.txt_newpass.pack(pady=5)

                self.show_reset_password_var = IntVar()
                show_reset_pass_check = Checkbutton(self.root2, text="Show Password", variable=self.show_reset_password_var, command=self.toggle_reset_password_visibility, font=("times new roman", 10, "bold"), bg="white")
                show_reset_pass_check.pack()

                Button(self.root2, text="Reset Password", command=self.reset_password, font=("times new roman", 15, "bold"), bg="green", fg="white").pack(pady=20)

    def toggle_reset_password_visibility(self):
        if self.show_reset_password_var.get():
            self.txt_newpass.config(show="")
        else:
            self.txt_newpass.config(show="*")

    def reset_password(self):
        if self.combo_security_question.get() == "Select":
            messagebox.showerror("Error", "Select Security Question", parent=self.root2)
            return
        if self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
            return
        if self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
            return

        try:
            conn = mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()

            # ✅ Correct column names based on your DB
            query = """ SELECT * FROM register WHERE EmailID = %s AND `Security Question` = %s AND `Security Answer` = %s """
            my_cursor.execute(query, (self.txtuser.get(),self.combo_security_question.get(),self.txt_security.get()))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Incorrect security question or answer", parent=self.root2)
            else:
                update_query = "UPDATE register SET Password = %s WHERE EmailID = %s"
                my_cursor.execute(update_query, (
                    self.txt_newpass.get(),
                    self.txtuser.get()
                ))
                conn.commit()
                messagebox.showinfo("Success", "Password reset successfully. Please login with your new password.", parent=self.root2)
                self.root2.destroy()

        except Exception as es:
            messagebox.showerror("Error", f"Something went wrong: {str(es)}", parent=self.root2)
        finally:
            if conn.is_connected():
                conn.close()

    # ******** Login Button Functions ********
    def return_login(self):
        self.root.destroy()

# Run the application  
if __name__ == "__main__":
    main()
