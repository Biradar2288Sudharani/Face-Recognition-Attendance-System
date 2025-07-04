# This is main part of this project
import cx_Freeze
import sys
import os 
import warnings
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\lenovo\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\lenovo\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("manage.py", base=base, icon="face.ico")]

cx_Freeze.setup(
    name = "Face Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'college_images','data','database','Attendance_Report','Attendance_Graphs',]}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Biradar Sudharani",
    executables = executables
    )

warnings.filterwarnings("ignore", category=SyntaxWarning)

# Application execution command: python setup.py bdist_msi , python setup.py build

'''
# 🎓 Face Recognition Attendance System
Welcome to the **Face Recognition Attendance System** — a smart, contactless, and efficient solution designed to automate the process of student attendance using face recognition technology. Developed using Python, OpenCV, Tkinter, and integrated with Twilio WhatsApp API for real-time parent communication.
---

## 📌 Key Features
- 👤 **Student Registration System**
  - Add, update, delete, and view student profiles
  - Store details like ID, name, roll number, department, contact, email, and address

- 📸 **Face Capture Module**
  - Capture student face images using webcam
  - Automatically stores them under unique folders for training

- 🧠 **Face Recognition & Attendance**
  - Real-time face recognition using OpenCV (LBPH)
  - Marks attendance automatically and saves to `.csv`

- 📊 **Attendance Analytics**
  - Displays monthly and overall attendance statistics
  - Graphs using **Matplotlib**
  - Average calculations for each student

- 💬 **WhatsApp Alerts for Parents**
  - Uses **Twilio API** to send:
    - ✔️ Congratulatory message if attendance ≥ 95%
    - ⚠️ Warning if attendance < 75%
    - ✅ Regular summary updates

- 🗓️ **Timetable Integration**
  - Links face recognition attendance with lecture-wise timetable
  - Calculates subject-wise attendance
  - Fully automated average detection
---
## 🛠️ Technologies Used
| Technology       | Purpose                          |
|------------------|----------------------------------|
| Python           | Backend logic                    |
| OpenCV           | Face detection & recognition     |
| Tkinter          | GUI interface                    |
| MySQL/CSV        | Data storage                     |
| Matplotlib       | Attendance graph visualization   |
| Twilio API       | WhatsApp alert integration       |
---
## ⚙️ Requirements
Install required packages:
```bash
pip install opencv-python
pip install mysql-connector-python
pip install twilio
pip install matplotlib
--------------------------------------------
How to run this project ?
To run this project using this "python manage.py"
'''