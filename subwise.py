import pandas as pd
import os
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from datetime import datetime

output_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report"
os.makedirs(output_path, exist_ok=True)

class SubjectWiseMonthlyAverage:
    def __init__(self, root):
        self.root = root
        self.root.title("📘 Subject-Wise Monthly Average Attendance")
        self.root.geometry("800x600")

        Label(root, text="📊 Monthly Subject-Wise Attendance Analyzer", font=("Helvetica", 18, "bold"), fg="blue").pack(pady=20)
        Button(root, text="📁 Load Attendance CSV", font=("Helvetica", 12), command=self.load_csv).pack(pady=10)
        Button(root, text="✅ Calculate & Save Average Attendance", font=("Helvetica", 12), command=self.calculate_average).pack(pady=10)

        self.filename = None
        self.manual_lectures = {}

    def load_csv(self):
        self.filename = filedialog.askopenfilename(initialdir=output_path, title="Select Attendance File",
                                                   filetypes=[("CSV files", "*.csv")])
        if self.filename:
            messagebox.showinfo("✅ File Loaded", f"Loaded file:\n{self.filename}")

    def calculate_average(self):
        if not self.filename:
            messagebox.showerror("❌ Error", "Please load a CSV file first.")
            return

        try:
            df = pd.read_csv(self.filename)

            # Clean data
            df.columns = df.columns.str.strip()
            df["Subject"] = df["Subject"].str.strip().str.replace("  ", " ", regex=False)
            df["Status"] = df["Status"].str.strip()
            df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='coerce')
            df.dropna(subset=["Date"], inplace=True)
            df["Month"] = df["Date"].dt.strftime("%B %Y")

            # Calculate Days Present per student
            present_df = df[df["Status"] == "Present"].groupby(
                ["Roll Number", "Name", "Subject", "Month"]
            )["Date"].nunique().reset_index(name="Days Present")

            # --- Step: Ask manual input for working days per subject per month ---
            subject_months = present_df[["Subject", "Month"]].drop_duplicates()
            for _, row in subject_months.iterrows():
                subj = row["Subject"]
                month = row["Month"]
                key = (subj, month)
                if key not in self.manual_lectures:
                    while True:
                        try:
                            val = simpledialog.askinteger("Input", f"Enter total lectures for {subj} in {month}:", minvalue=1)
                            if val is not None:
                                self.manual_lectures[key] = val
                                break
                            else:
                                messagebox.showerror("Error", f"Input required for {subj} - {month}")
                        except ValueError:
                            messagebox.showerror("Error", "Enter a valid number!")

            # Add Total Lectures from manual input
            present_df["Total Lectures"] = present_df.apply(
                lambda row: self.manual_lectures.get((row["Subject"], row["Month"]), 0), axis=1
            )

            # Calculate attendance %
            present_df["Attendance %"] = (present_df["Days Present"] / present_df["Total Lectures"] * 100).clip(upper=100).round(2)

            # Save to CSV
            save_path = os.path.join(output_path, "Monthly_Subject_Wise_Average_Corrected.csv")
            present_df.to_csv(save_path, index=False)

            messagebox.showinfo("🎉 Success", f"Corrected Average attendance saved to:\n{save_path}")

        except Exception as e:
            messagebox.showerror("⚠️ Error", f"Something went wrong:\n{str(e)}")

# Run GUI
if __name__ == "__main__":
    root = Tk()
    app = SubjectWiseMonthlyAverage(root)
    root.mainloop()
