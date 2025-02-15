import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\lenovo\AppData\Local\Programs\Python\Python312\tcl\tcl8"
os.environ['TK_LIBRARY'] = r"C:\Users\lenovo\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"

executables = [cx_Freeze.Executable("login1.py", base=base, icon="face.ico")]

cx_Freeze.setup(
    name = "Face Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'college_images','data','database','Attendance Report','.venv','.vscode','__pycache__']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Biradar Sudharani",
    executables = executables
    )

# Application execution command: python setup.py bdist_msi 