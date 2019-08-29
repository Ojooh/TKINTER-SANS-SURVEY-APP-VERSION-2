import cx_Freeze
import sys
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

# os.environ['TCL_LIBRARY'] = r'env\tcl\tcl8.6'
# os.environ['TK_LIBRARY'] = r'env\tcl\tk8.6'

os.environ['TCL_LIBRARY'] = r"C:\Python36\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python36\tcl\tK8.6"


executables = [cx_Freeze.Executable("UserXP.py", base=base, icon="images/halo_shield.ico"), cx_Freeze.Executable("admin.py", base=base, icon="images/halo_shield.ico")]

cx_Freeze.setup(
    name = "Cyber Security Awareness V2",
    options = {"build_exe": {"packages":["tkinter", "itertools", "idna"], "include_files":["admin.py", "images/Adminbutton.png", "images/backbutton.png", "images/exitbutton.png", "images/nextt.png", "images/nextbutton.png", "images/start.png", "images/leveler.png", "images/halo_shield.ico", "images/halo_shield.png", "images/user_awareness1.png", "db/user_responses.json", "db/reverse_questions.json", "db/questions_answers.json", "tcl86t.dll", "tk86t.dll"]}},
    version = "0.02",
    description = "Cyber Security Awareness Application V2",
    executables = executables
    )

