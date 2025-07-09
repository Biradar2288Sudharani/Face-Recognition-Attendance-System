import pandas as pd
import os
import re
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from twilio.rest import Client
from subwise import SubjectWiseMonthlyAverage

class AttendanceAnalyzer:
    OUTPUT_FOLDER = "Attendance_Graphs"

    def __init__(self, root, file_path):
        self.root = root
        self.file_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\sudha.csv"
        self.root.title("Face Recognition Attendance")
        self.root.geometry("1366x768")
        
        os.makedirs(self.OUTPUT_FOLDER, exist_ok=True)
        self.df = self.load_and_process_data()
        self.attendance_summary = None

        title_lbl = Label(self.root, text="Average Attendance", font=("times new roman", 32, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        self.selected_month = tk.StringVar()
        months = sorted(self.df["Month_Year"].unique())

        # Left Main Frame
        Left_Frame = LabelFrame(self.root, bd=2, bg="pink", relief=RIDGE, text="Average Attendance Details", font=("times new roman", 16, "bold"))
        Left_Frame.place(x=0, y=50, width=682, height=350)

        self.month_dropdown = ttk.Combobox(Left_Frame, textvariable=self.selected_month, values=months, state="readonly", font=("Arial", 12), width=15)
        self.month_dropdown.place(x=60, y=30, width=400, height=40)
        self.month_dropdown.set("Select Your Year & Month ===>")
        self.month_dropdown.config(foreground="black", font=("Arial", 18, "bold"))

        Label(Left_Frame, text="Enter Working Days:", font=("Arial", 14, "bold"), bg="black", fg="white").place(x=120, y=180, width=200, height=40)
        self.working_days_entry = tk.Entry(Left_Frame, font=("Arial", 14, "bold"), bg="white", fg="black")
        self.working_days_entry.place(x=330, y=180, width=50, height=40)

        Label(Left_Frame, text="Enter Attendance ID (Optional):", font=("Arial", 14, "bold"), bg="black", fg="white").place(x=80, y=110, width=300, height=40)
        self.attendance_id_entry = tk.Entry(Left_Frame, font=("Arial", 14, "bold"), bg="white", fg="black")
        self.attendance_id_entry.place(x=390, y=110, width=50, height=40)

        self.show_button = tk.Button(Left_Frame, text="Show Graph", command=self.show_graph, font=("times new roman", 18, "bold"), fg="black", bg="red")
        self.show_button.place(x=170, y=250, width=150, height=40)

        b1_lbl=Button(Left_Frame,text="Subject Wise",cursor="hand2",command=self.sub_data,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_lbl.place(x=380,y=250,width=150,height=40)

        # Right Label Frame
        Right_Frame = LabelFrame(self.root, bd=2, bg="pink", relief=RIDGE, text="WhatsTrack EduAlert", font=("times new roman", 16, "bold"))
        Right_Frame.place(x=684, y=50, width=680, height=350)

        admin_note = Label(Right_Frame, text="""🔽   This section is for admins only,
        If you want to send this month’s student attendance performance to 
        their guardians, please click the WhatsApp Send button below.""",
        font=("Helvetica", 12, "bold"), wraplength=550, justify="left", fg="black", bg="pink")
        admin_note.pack(pady=10)

        self.send_button = tk.Button(Right_Frame, text="Send WhatsApp", command=self.send_whatsapp_messages, font=("times new roman", 18, "bold"), fg="white", bg="green")
        self.send_button.place(x=150, y=120, width=200, height=40)

        Label(Right_Frame, text="Manual Alert Message:", font=("Arial", 14, "bold"), bg="black", fg="white").place(x=10, y=180)
        self.alert_entry = tk.Entry(Right_Frame, font=("Arial", 14, "bold"), width=100)
        self.alert_entry.place(x=10, y=210, width=650)

        self.alert_button = tk.Button(Right_Frame, text="Send WhatsApp", command=self.send_manual_alert, font=("times new roman", 18, "bold"), fg="white", bg="green")
        self.alert_button.place(x=150, y=250, width=200, height=40)

        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack()

        # Image One
        img1 = Image.open(r"C:college_images\graph2.png")
        img1 = img1.resize((682, 354))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=0, y=400, width=682, height=354)

        # Image Two
        img2 = Image.open(r"C:college_images\graph4.png")
        img2 = img2.resize((680, 354))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=685, y=400, width=680, height=354)

    def load_and_process_data(self):
        df = pd.read_csv(self.file_path, encoding="utf-8", header=None, on_bad_lines='skip')
        df.columns = ["Attendance ID", "Phone Number", "Name", "Department", "Time", "Date", "Attendance Status"]
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce", dayfirst=True)
        df = df.dropna(subset=["Date"])
        df["Month_Year"] = df["Date"].dt.to_period("M").astype(str)
        df["Attendance ID"] = pd.to_numeric(df["Attendance ID"], errors="coerce")
        df = df.dropna(subset=["Attendance ID"])
        df["Attendance ID"] = df["Attendance ID"].astype(int)
        return df

    def calculate_attendance_summary(self, month, working_days):
        month_data = self.df[self.df["Month_Year"] == month]
        if month_data.empty:
            self.attendance_summary = pd.DataFrame()
            return
        summary = month_data.groupby(["Attendance ID", "Name", "Phone Number"]).size().reset_index(name="Days Present")
        summary["Total Working Days"] = working_days
        summary["Month_Year"] = month
        summary["Attendance Percentage"] = (summary["Days Present"] / working_days) * 100
        summary["Attendance Percentage"] = summary["Attendance Percentage"].round(2)
        summary["Display Percentage"] = summary["Attendance Percentage"].clip(upper=100)
        self.attendance_summary = summary

    def clean_message(self, text):
        return text.encode('utf-8', 'ignore').decode('utf-8')

    def filter_by_attendance_id(self):
        attendance_id_input = self.attendance_id_entry.get().strip()
        if not attendance_id_input:
            return self.attendance_summary
        if not attendance_id_input.isdigit():
            messagebox.showerror("Input Error", "Attendance ID must be numeric.", parent=self.root)
            return pd.DataFrame()
        attendance_id = int(attendance_id_input)
        filtered = self.attendance_summary[self.attendance_summary["Attendance ID"] == attendance_id]
        if filtered.empty:
            messagebox.showinfo("Not Found", f"No data found for Attendance ID: {attendance_id}", parent=self.root)
        return filtered

    def send_whatsapp_messages(self):
        if self.attendance_summary is None:
            messagebox.showerror("Error", "No attendance summary available. Please generate it first.", parent=self.root)
            return

        filtered_summary = self.filter_by_attendance_id()
        if filtered_summary.empty:
            return

        account_sid = 'AC4f7deb22e8ab272b75f4e38c33b62970'
        auth_token = '3395e4046f5541f6d913d79f0d21f3bb'
        client = Client(account_sid, auth_token)

        for _, row in filtered_summary.iterrows():
            name = row["Name"]
            phone = str(row["Phone Number"])
            percent = row["Attendance Percentage"]
            days_present = int(row["Days Present"])
            total_days = int(row["Total Working Days"])
            month = row["Month_Year"]

            if not phone.startswith('+91'):
                phone = '+91' + phone

            remarks = "Good standing."
            if percent < 75:
                remarks = "Attendance is below the minimum requirement. Kindly ensure regular attendance."
            elif percent >= 95:
                remarks = "Excellent attendance! Keep up the good work."

            body = (
                f"Hi Parent/Guardian of {name},\n\n"
                f"This is to inform you that your child, {name}, has an attendance of {percent}% for {month}.\n\n"
                f"\u2705 Status: Present on {days_present} out of {total_days} working days.\n\n"
                f"\U0001F4CA Remarks: {remarks}\n\n"
                "\U0001F6A1 Note: Irregular attendance can impact academic performance and eligibility for exams."
            )
            cleaned_body = self.clean_message(body)
            message = client.messages.create(
                body=cleaned_body,
                from_='whatsapp:+14155238886',
                to='whatsapp:' + phone
            )
            print(f"Sent to {name} ({phone}): {message.sid}")

        messagebox.showinfo("Success", "WhatsApp message(s) sent successfully!", parent=self.root)

    def send_custom_alert(self, custom_message):
        if self.attendance_summary is None:
            messagebox.showerror("Error", "No attendance summary available. Please generate it first.", parent=self.root)
            return

        filtered_summary = self.filter_by_attendance_id()
        if filtered_summary.empty:
            return

        account_sid = 'AC4f7deb22e8ab272b75f4e38c33b62970'
        auth_token = '3395e4046f5541f6d913d79f0d21f3bb'
        client = Client(account_sid, auth_token)

        for _, row in filtered_summary.iterrows():
            phone = str(row["Phone Number"])
            name = row["Name"]

            if not phone.startswith('+91'):
                phone = '+91' + phone

            cleaned_msg = self.clean_message(f"📢 Manual Alert for {name}:\n\n{custom_message}")
            message = client.messages.create(
                body=cleaned_msg,
                from_='whatsapp:+14155238886',
                to='whatsapp:' + phone
            )
            print(f"Alert sent to {name} ({phone}): {message.sid}")

        messagebox.showinfo("Success", "Custom alert(s) sent!", parent=self.root)

    def send_manual_alert(self):
        alert_message = self.alert_entry.get().strip()
        if alert_message:
            self.send_custom_alert(alert_message)
        else:
            messagebox.showerror("Input Error", "Please enter a custom alert message.", parent=self.root)

    def show_graph(self):
        selected_month = self.selected_month.get().strip()
        working_days_input = self.working_days_entry.get().strip()

        if not selected_month or selected_month.startswith("Select"):
            messagebox.showerror("Input Error", "Please select a valid month.", parent=self.root)
            return

        if not working_days_input.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid number of working days.", parent=self.root)
            return

        working_days = int(working_days_input)
        self.calculate_attendance_summary(selected_month, working_days)

        if self.attendance_summary.empty:
            messagebox.showinfo("No Data", f"No attendance data found for {selected_month}", parent=self.root)
            return

        save_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\Average_Atten.csv"
        try:
            if os.path.exists(save_path):
                existing_df = pd.read_csv(save_path)
                updated_df = existing_df[existing_df["Month_Year"] != selected_month]
                combined_df = pd.concat([updated_df, self.attendance_summary], ignore_index=True)
            else:
                combined_df = self.attendance_summary
            combined_df.to_csv(save_path, index=False)
        except Exception as e:
            messagebox.showerror("File Save Error", f"Could not save summary CSV.\nError: {e}", parent=self.root)
            return

        graph_window = tk.Toplevel(self.root)
        graph_window.title(f"Attendance for {selected_month}")
        graph_window.geometry("1366x768")

        fig, ax = plt.subplots(figsize=(16, 10))
        display_data = self.filter_by_attendance_id()
        if display_data.empty:
            return

        ax.bar(display_data["Attendance ID"].astype(str), display_data["Display Percentage"], color='skyblue')
        ax.set_xlabel("Attendance ID")
        ax.set_ylabel("Attendance Percentage")
        ax.set_title(f"Attendance for {selected_month}")
        ax.set_ylim(0, 110)
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        for i, value in enumerate(display_data["Display Percentage"]):
            ax.text(i, value + 2, f"{value}%", ha="center", fontsize=10, fontweight="bold")

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def sub_data(self):
        self.new_window=Toplevel(self.root)
        self.app=SubjectWiseMonthlyAverage(self.new_window) 

if __name__ == "__main__":
    import tkinter as tk

    def on_closing():
        root.quit()
        root.destroy()

    file_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\sudha.csv"
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    analyzer = AttendanceAnalyzer(root, file_path)  # ✅ This order matters!
    root.mainloop()
