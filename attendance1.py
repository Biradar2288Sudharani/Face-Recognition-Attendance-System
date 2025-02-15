from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # ************* Variable Creation ***************
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendane = StringVar()
        global mydata
        mydata = []

        # First Image
        img1 = Image.open(r"C:college_images\h1.png")
        img1 = img1.resize((685, 150))
        self.photoimage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=0, y=0, width=683, height=150)

        # Second Image
        img2 = Image.open(r"C:college_images\atten2.png")
        img2 = img2.resize((683, 150))
        self.photoimage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=685, y=0, width=683, height=150)

        # Background Image
        img3 = Image.open(r"C:college_images\bg3.png")
        img3 = img3.resize((13665, 768))
        self.photoimage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimage3,bg="black")
        bg_img.place(x=0, y=110, width=1366, height=768)

        title_lbl = Label(bg_img, text="Attendance Management System",font=("times new roman", 32, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=48)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=50, width=1366, height=700)

        # Left Label Frame----------Student Details
        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=0, y=0, width=680, height=540)

        # Left Image
        img_left = Image.open(r"C:college_images\atten.png")
        img_left = img_left.resize((674,140))
        self.photoimage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_Frame, image=self.photoimage_left)
        f_lbl.place(x=2, y=0, width=674, height=140)

        left_inside_frame = Frame(Left_Frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=2, y=142, width=670, height=370)

        # ********* Labeled Entry ***********

        labels = ["AttendanceId:", "Roll Number:", "Name:", "Department:", "Time:", "Date:"]
        variables = [self.var_atten_id, self.var_atten_roll, self.var_atten_name,self.var_atten_dep, self.var_atten_time, self.var_atten_date]

        for idx, text in enumerate(labels):
            label = Label(left_inside_frame, text=text, font=("times new roman", 13, "bold"), bg="white")
            label.grid(row=idx, column=0, padx=15, pady=10, sticky=W)

            entry = ttk.Entry(left_inside_frame, width=20, textvariable=variables[idx],font=("times new roman", 13, "bold"))
            entry.grid(row=idx, column=1, padx=15, pady=10, sticky=W)

        # Attendance
        attendance_label = Label(left_inside_frame, text="Attendance Status:",font=("times new roman", 13, "bold"), bg="white")
        attendance_label.grid(row=6, column=0, padx=15, pady=10)

        self.atten_status = ttk.Combobox(left_inside_frame, width=18, textvariable=self.var_atten_attendane,font=("times new roman", 13, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=6, column=1, padx=15, pady=10)
        self.atten_status.current(0)

        # ++++++++++++++++++++++++++ Button Frames ++++++++++++++++++++++++++++++
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=330,width=680,height=35)
        
        # Import CSV Button Creating
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        save_btn.grid(padx=0,row=0,column=0)

        # Export CSV Button Creating
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        update_btn.grid(padx=1,row=0,column=1)
        
        # Delete Button Creating
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        delete_btn.grid(padx=1,row=0,column=2)
        
        # Reset Button Creating
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        reset_btn.grid(padx=1,row=0,column=3)

#========================== Right Label Frame ========================
        # Student Details
        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",font=("times new roman", 12, "bold"))
        Right_Frame.place(x=683, y=0, width=677, height=540)

        table_Frame = Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
        table_Frame.place(x=3, y=5, width=668, height=510)

        # *********** Scroll Bar Table ***********
        scroll_x = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_Frame, columns=("id", "roll", "name", "dep", "time", "date", "attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll Number")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("dep", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance Status")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("dep", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ******************** Data Fetching ***************************************************
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # ****** Import CSV ******
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ****** Export CSV *******
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                               filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", f"Your data exported to {os.path.basename(fln)} successfully.")
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
    
    # ************************** Fetch Data **************************
    def fetch_data(self):
        try:
            # Clear existing data in the table
            for row in self.AttendanceReportTable.get_children():
                self.AttendanceReportTable.delete(row)
            
            # Fetch updated data from CSV file
            with open("Attendance Report/sudha.csv", "r") as file:
                for line in file.readlines()[1:]:  # Skip the header row
                    row = line.strip().split(",")
                    self.AttendanceReportTable.insert("", END, values=row)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ************* Delete Function ******
    def delete_data(self):
        selected_item = self.AttendanceReportTable.focus()  # Get the selected row from the Treeview
        if not selected_item:
            messagebox.showerror("Error", "Please select a row to delete", parent=self.root)
            return

        # Get data from the selected row
        selected_row = self.AttendanceReportTable.item(selected_item)['values']
        if not selected_row:
            messagebox.showerror("Error", "No valid data found in the selected row", parent=self.root)
            return

        try:
            delete = messagebox.askyesno("Delete Confirmation", "Do you want to delete this record?", parent=self.root)
            if delete:
                # Read the existing data from the CSV
                file_path = "Attendance Report/sudha.csv"
                updated_data = []
                selected_row_str = ",".join([str(x).strip() for x in selected_row])  # Ensure consistent formatting

                with open(file_path, "r") as file:
                    for line in file:
                        # Compare rows as strings after stripping whitespace
                        if line.strip() != selected_row_str:
                            updated_data.append(line)

                # Write back the updated data to the CSV
                with open(file_path, "w") as file:
                    file.writelines(updated_data)

                # Refresh the table to reflect the changes
                self.fetch_data()

                messagebox.showinfo("Success", "Selected row deleted successfully", parent=self.root)
            else:
                return  # Do nothing if 'No' is selected
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)



    # ************** Get Cursor ********
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendane.set(rows[6])

        # ********* Reset Operation **********
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendane.set("")         

if __name__== " __main__ ":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()