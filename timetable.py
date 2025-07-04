import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import *
from PIL import Image, ImageTk
import os
import csv
import pandas as pd
import re
import mysql.connector
from tkinter import LabelFrame
from datetime import datetime, timedelta
from attendance1 import Attendance
from Avg_Atten import AttendanceAnalyzer

class Time_Table:
    def __init__(self,root):
        self.source_var = StringVar()
        self.source_var.set("csv")
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")
        self.root.wm_iconbitmap("face.ico")

        self.var_id = StringVar()
        self.var_day = StringVar()
        self.var_time = StringVar()
        self.var_batch = StringVar()
        self.var_subject = StringVar()
        self.var_staff_name = StringVar()
        self.var_batch_info = StringVar()


        # ************* MySQL Connection ***************
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="Shankar2sep@",database="face_recognition",auth_plugin="mysql_native_password")
            self.my_cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect to MySQL: {str(e)}", parent=self.root)

        # ************* Variable Creation ***************
        self.var_id = StringVar()
        self.var_day = StringVar()
        self.var_time = StringVar()
        self.var_batch = StringVar()
        self.var_subject = StringVar()
        self.var_staff_name = StringVar()

        # Background Image
        img3 = Image.open(r"C:college_images\bg3.png")
        img3 = img3.resize((1366, 768))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimage3)
        bg_img.place(x=0, y=0, width=1366, height=768)

        title_lbl = Label(bg_img, text="Time Table Management System", font=("times new roman", 33, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=50)

# *********************************** LEFT FRAME STARTED *********************************************
        Left_Frame = LabelFrame(self.root, bd=2, bg="pink", relief=RIDGE, text="Time Table From CSV", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=0, y=50, width=682, height=650)

        import_btn = Button(Left_Frame, text="Import CSV", command=self.import_csv, font=("times new roman", 14, "bold"), bg="blue", fg="white")
        import_btn.place(x=280, y=400, width=120, height=40)

        table_frame = Frame(Left_Frame)
        table_frame.place(x=0, y=0, width=678, height=400)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.TimeTable = ttk.Treeview(table_frame, columns=("ID", "Day", "Time", "Batch", "Subject", "Staff_Name","Batch_Info"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        for col in ("ID", "Day", "Time", "Batch", "Subject", "Staff_Name","Batch_Info"):
            self.TimeTable.heading(col, text=col)
            self.TimeTable.column(col, width=100)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.TimeTable.xview)
        scroll_y.config(command=self.TimeTable.yview)

        self.TimeTable["show"] = "headings"
        self.TimeTable.pack(fill=BOTH, expand=1)
        self.TimeTable.bind("<ButtonRelease-1>", self.get_cursor)

        self.source_var = tk.StringVar(value="csv")
        self.TimeTable.bind("<ButtonRelease-1>", self.get_cursor_csv)

        # ****************** Choose frame creation ******************
        choice_frame = LabelFrame(Left_Frame, bd=2, relief=RIDGE, bg="pink", text="Choice Time Table", font=("times new roman", 12, "bold"))
        choice_frame.place(x=0, y=440, width=678, height=185)

        # Professional instruction label
        instruction = tk.Label(choice_frame,
            text="""🗓️Kindly proceed by designating the source for today’s timetable either 
         retrieve it from the compiled CSV dataset or initiate manual configuration.""",
            wraplength=850, justify="left",font=("times new roman",14,"bold"),fg="black", bg="pink")
        instruction.place(x=0,y=0)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times New Roman", 12, "bold"))

        Label(choice_frame, text="Enter Day:", font=("Arial", 14, "bold"), bg="black", fg="white").place(x=80, y=55, width=120, height=30)
        self.day_entry = tk.Entry(choice_frame, font=("Arial", 14, "bold"), bg="white", fg="black")
        self.day_entry.place(x=200, y=55, width=110, height=30)

        Label(choice_frame, text="Enter Date:", font=("Arial", 14, "bold"), bg="black", fg="white").place(x=350, y=55, width=120, height=30)
        self.date_entry = tk.Entry(choice_frame, font=("Arial", 14, "bold"), bg="white", fg="black")
        self.date_entry.place(x=470, y=55, width=120, height=30)

        csv_radio = tk.Radiobutton(choice_frame, text="CSV File",command=self.load_selected_timetable,variable=self.source_var, value="csv",font=("times new roman", 14, "bold"), bg="pink", fg="purple")
        csv_radio.place(x=170, y=95)

        mysql_radio = tk.Radiobutton(choice_frame, text="Database",command=self.load_selected_timetable, variable=self.source_var, value="mysql",font=("times new roman", 14, "bold"), bg="pink", fg="purple")
        mysql_radio.place(x=390, y=95)

        # ********** Attendance Button **********
        attendance_btn = Button(choice_frame, text="Start Attendance",command=self.match_attendance,font=("times new roman", 16, "bold"), bg="green", fg="white")
        attendance_btn.place(x=240, y=132, width=200, height=30)

# ********************************************** RIGHT FRAME STARTED **********************************************
        Right_Frame = LabelFrame(self.root, bd=2, bg="pink", relief=RIDGE, text="Manual Time Table Entry", font=("times new roman", 12, "bold"))
        Right_Frame.place(x=686, y=50, width=680, height=650)

        labels = ["ID :", "Day :", "Time :", "Batch :", "Subject :", "Staff_Name :", "Batch Info"]
        variables = [self.var_id, self.var_day, self.var_time, self.var_batch, self.var_subject, self.var_staff_name, self.var_batch_info]

        for idx, text in enumerate(labels):
            label = Label(Right_Frame, text=text, font=("times new roman", 13, "bold"), bg="pink")
            label.grid(row=idx, column=0, padx=15, pady=2, sticky=W)

            entry = ttk.Entry(Right_Frame, width=20, textvariable=variables[idx], font=("times new roman", 13, "bold"))
            entry.grid(row=idx, column=1, padx=15, pady=2, sticky=W)

        table_Frame = Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
        table_Frame.place(x=3, y=220, width=670, height=375)

        btn_frame1 = Frame(Right_Frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=3, y=592, width=670, height=35)

        Button(btn_frame1, text="Save", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=self.save_data).grid(row=0, column=0)
        Button(btn_frame1, text="Update", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=self.update_data).grid(row=0, column=1)
        Button(btn_frame1, text="Delete", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=self.delete_data).grid(row=0, column=2)
        Button(btn_frame1, text="Reset", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=self.reset_fields).grid(row=0, column=3)

        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)

        self.TimeTableManual = ttk.Treeview(table_Frame, columns=("ID", "Day", "Time", "Batch", "Subject", "Staff_Name","Batch_Info"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        for col in ("ID", "Day", "Time", "Batch", "Subject", "Staff_Name","Batch_Info"):
            self.TimeTableManual.heading(col, text=col)
            self.TimeTableManual.column(col, width=100)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.TimeTableManual.xview)
        scroll_y.config(command=self.TimeTableManual.yview)

        self.TimeTableManual["show"] = "headings"
        self.TimeTableManual.pack(fill=BOTH, expand=1)
        self.TimeTableManual.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def import_csv(self):
        try:
            file_path = filedialog.askopenfilename(title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
            if not file_path:
                return
            with open(file_path, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in self.TimeTable.get_children():
                    self.TimeTable.delete(row)
                for row in reader:
                    if len(row) >= 7:
                        self.TimeTable.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            messagebox.showinfo("Success", "CSV Imported Successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error importing CSV:\n{str(e)}", parent=self.root)
    
    # ********************************** Connecting time table to Radio Button ***************
    def load_selected_timetable(self):
        day_entered = self.day_entry.get().strip()
        date_entered = self.date_entry.get().strip()  # New line
        source = self.source_var.get()
        if not day_entered or not date_entered:
            messagebox.showerror("Error", "Please enter both Day and Date to load the timetable.", parent=self.root)
            return
        if source == "csv":
            try:
                with open("C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\BTech.csv", newline="", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    header = next(reader)
                    for row in reader:
                        if len(row) >= 6 and row[1].strip().lower() == day_entered.lower():
                            messagebox.showinfo("Success", f"✅ Timetable loaded for {day_entered}, {date_entered} from CSV.", parent=self.root)
                            return
                    messagebox.showwarning("No Data", f"No timetable found in CSV for '{day_entered}'.", parent=self.root)
            except Exception as e:
                messagebox.showerror("CSV Error", str(e), parent=self.root)
        elif source == "mysql":
            try:
                query = "SELECT ID, Day, Time, Batch, Subject, Staff_Name, Batch_Info FROM timetable WHERE LOWER(Day) = %s"
                self.my_cursor.execute(query, (day_entered.lower(),))
                rows = self.my_cursor.fetchall()
                if rows:
                    messagebox.showinfo("MySQL Time Table", f"✅ Timetable loaded for {day_entered}, {date_entered} from MySQL.", parent=self.root)
                else:
                    messagebox.showwarning("No Data", f"No timetable found in MySQL for '{day_entered}'.", parent=self.root)
            except Exception as e:
                messagebox.showerror("MySQL Error", str(e), parent=self.root)

    def parse_time_range(self, time_range_str):
        try:
            start_str, end_str = time_range_str.split("to")
            start_time = datetime.strptime(start_str.strip(), "%H:%M").time()
            end_time = datetime.strptime(end_str.strip(), "%H:%M").time()
            if end_time < start_time:
                end_time = (datetime.combine(datetime.today(), end_time) + timedelta(hours=12)).time()
            return start_time, end_time
        except Exception as e:
            print(f"Error parsing time range '{time_range_str}': {e}", parent=self.root)
            return None, None

    def match_attendance(self):
        day = (self.day_entry.get() or "").strip()
        date_entered = (self.date_entry.get() or "").strip()
        source = self.source_var.get()

        if not day or not date_entered:
            messagebox.showerror("Error", "❌ Please enter both Day and Date before matching attendance.", parent=self.root)
            return

        try:
            timetable = []

            # Load timetable
            if source == "csv":
                with open("C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\BTech.csv", "r", encoding="utf-8") as tfile:
                    reader = csv.DictReader(tfile)
                    for row in reader:
                        if (row.get("Day") or "").strip().lower() == day.lower():
                            time_range = (row.get("Time") or "").strip()
                            start_time, end_time = self.parse_time_range(time_range)
                            if start_time and end_time:
                                timetable.append({
                                    "start": start_time,
                                    "end": end_time,
                                    "subject": (row.get("Subject") or "").strip(),
                                    "batch": (row.get("Batch") or "").strip(),
                                    "staff": (row.get("Staff_Name") or "").strip(),
                                    "batch_info": (row.get("Batch Information") or "").strip()
                                })
            elif source == "mysql":
                query = "SELECT Day, Time, Batch, Subject, Staff_Name, Batch_Info FROM timetable WHERE LOWER(day) = %s"
                self.my_cursor.execute(query, (day.lower(),))
                rows = self.my_cursor.fetchall()
                for row in rows:
                    time_range = row[1] or ""
                    start_time, end_time = self.parse_time_range(time_range.strip())
                    if start_time and end_time:
                        timetable.append({
                            "start": start_time,
                            "end": end_time,
                            "subject": (row[3] or "").strip(),
                            "batch": (row[2] or "").strip(),
                            "staff": (row[4] or "").strip(),
                            "batch_info": (row[5] or "").strip()
                        })

            if not timetable:
                messagebox.showwarning("No Data", f"No timetable found for '{day}'.", parent=self.root)
                return

            matched_data = []
            unmatched_rolls = []

            with open("C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\Attendance.csv", "r", encoding="utf-8") as afile:
                reader = csv.DictReader(afile)
                for row in reader:
                    try:
                        student_time_str = (row.get("Time") or "").strip()
                        student_name = (row.get("Name") or "").strip()
                        roll_str = (row.get("Roll Number") or "").strip()
                        phone = (row.get("Phone Number") or "").strip()
                        branch = (row.get("Department") or row.get("Branch") or "").strip()

                        if not student_time_str or not student_name or not roll_str:
                            continue

                        student_time = datetime.strptime(student_time_str, "%H:%M:%S").time()
                        roll = int(roll_str)
                        matched = False

                        for slot in timetable:
                            if slot["start"] <= student_time <= slot["end"]:
                                batch_info = slot.get("batch_info", "").replace(" ", "").lower()
                                if batch_info == "-" or batch_info == "":
                                    matched_data.append({
                                        "Roll Number": roll_str,
                                        "Phone Number": phone,
                                        "Name": student_name,
                                        "Branch": branch,
                                        "Time": student_time.strftime("%H:%M:%S"),
                                        "Date": date_entered,
                                        "Status": "Present",
                                        "Subject": slot['subject']
                                    })
                                    matched = True
                                    break

                                match = re.search(r"rollno(\d+)to(\d+)", batch_info)
                                if match:
                                    start_roll = int(match.group(1))
                                    end_roll = int(match.group(2))
                                    if start_roll <= roll <= end_roll:
                                        matched_data.append({
                                            "Roll Number": roll_str,
                                            "Phone Number": phone,
                                            "Name": student_name,
                                            "Branch": branch,
                                            "Time": student_time.strftime("%H:%M:%S"),
                                            "Date": date_entered,
                                            "Status": "Present",
                                            "Subject": slot['subject']
                                        })
                                        matched = True
                                        break

                        if not matched:
                            unmatched_rolls.append(roll_str)
                    except Exception as e:
                        print(f"⚠️ Error parsing attendance row ({row}): {e}", parent=self.root)

            if not matched_data:
                messagebox.showwarning("No Matches", "No student attendance matched with timetable slots for this day.", parent=self.root)
                return

            final_file_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\FinalAttendance.csv"
            fieldnames = ["Roll Number", "Phone Number", "Name", "Branch", "Time", "Date", "Status", "Subject"]

            # Load existing data if any
            if os.path.exists(final_file_path):
                existing_df = pd.read_csv(final_file_path)
            else:
                existing_df = pd.DataFrame(columns=fieldnames)

            # Convert matched_data to DataFrame
            new_df = pd.DataFrame(matched_data)

            # Insert empty row after current day's data
            empty_row = pd.DataFrame([{col: "" for col in fieldnames}])
            new_df = pd.concat([new_df, empty_row], ignore_index=True)

            # Combine and drop duplicates
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            combined_df.drop_duplicates(subset=["Roll Number", "Date", "Subject"], keep="last", inplace=True)

            # Save final CSV
            combined_df.to_csv(final_file_path, index=False)

            # Show unmatched roll numbers
            if unmatched_rolls:
                unique_unmatched = sorted(set(unmatched_rolls))
                msg = (
                    "⚠️ Warning:\n\n"
                    "The following roll numbers were found in attendance but did not match any timetable batch slot:\n\n"
                    f"{', '.join(unique_unmatched)}\n\n"
                    "Please verify and update 'Batch Information' in the timetable."
                )
                messagebox.showwarning("Batch Info Missing", msg, parent=self.root)

            messagebox.showinfo("✅ Success", f"Final subject-wise attendance saved for {day}, {date_entered}!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to match attendance:\n{str(e)}", parent=self.root)

  # ************************ Preforming Operations on database ******************************
    def get_cursor(self, event=""):
        try:
            selected = self.TimeTableManual.focus()
            values = self.TimeTableManual.item(selected, "values")
            if values:
                self.var_id.set(values[0])
                self.var_day.set(values[1])
                self.var_time.set(values[2])
                self.var_batch.set(values[3])
                self.var_subject.set(values[4])
                self.var_staff_name.set(values[5])
                self.var_batch_info.set(values[6])
        except Exception as e:
            messagebox.showerror("Error", f"Could not load selected row: {str(e)}", parent=self.root)

    def get_cursor_csv(self, event=""):
        try:
            selected = self.TimeTable.focus()
            values = self.TimeTable.item(selected, "values")
            if values:
                self.var_id.set(values[0])
                self.var_day.set(values[1])
                self.var_time.set(values[2])
                self.var_batch.set(values[3])
                self.var_subject.set(values[4])
                self.var_staff_name.set(values[5])
                self.var_batch_info.set(values[6])
        except Exception as e:
            messagebox.showerror("Error", f"Could not load selected row from CSV: {str(e)}", parent=self.root)

    def reset_fields(self):
        for var in [self.var_id, self.var_day, self.var_time, self.var_batch, self.var_subject, self.var_staff_name, self.var_batch_info]:
            var.set("")

    def save_data(self):
        if self.var_id.get() == "" or self.var_day.get() == "" or self.var_time.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            query = """INSERT INTO timetable (id, day, time, batch, subject, staff_name,batch_info) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            values = (self.var_id.get(),self.var_day.get(),self.var_time.get(),self.var_batch.get(),self.var_subject.get(),self.var_staff_name.get(),self.var_batch_info.get())
            self.my_cursor.execute(query, values)
            self.conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Record saved successfully", parent=self.root)
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "ID already exists", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data:\n{str(e)}", parent=self.root)

    def fetch_data(self):
        self.my_cursor.execute("SELECT * FROM timetable")
        rows = self.my_cursor.fetchall()
        for i in self.TimeTableManual.get_children():
            self.TimeTableManual.delete(i)
        for row in rows:
            self.TimeTableManual.insert("", tk.END, values=row)

    def update_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return
        confirm = messagebox.askyesno("Confirm Update", "Are you sure you want to update this record?", parent=self.root)
        if confirm:
            try:
                self.my_cursor.execute("""UPDATE timetable SET day=%s, time=%s, batch=%s, subject=%s, staff_name=%s, batch_info=%s WHERE id=%s """, (self.var_day.get(),self.var_time.get(),self.var_batch.get(),self.var_subject.get(),self.var_staff_name.get(),self.var_batch_info.get(),self.var_id.get()))
                self.conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Record updated successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred:\n{str(e)}", parent=self.root)
        else:
            messagebox.showinfo("Cancelled", "Update operation cancelled", parent=self.root)

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please select a record to delete", parent=self.root)
            return
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?", parent=self.root)
        if confirm:
            self.my_cursor.execute("DELETE FROM timetable WHERE id=%s", (self.var_id.get(),))
            self.conn.commit()
            self.fetch_data()
            self.reset_fields()
            messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)

    def timetable_manage(self):
        self.new_window=Toplevel(self.root)
        self.app=Time_Table(self.new_window)

# Run Application
if __name__ == "__main__":
    root = Tk()
    obj = Time_Table(root)
    root.mainloop()
