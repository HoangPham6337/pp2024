import tkinter as tk
import tkinter.ttk as ttk
from functions import (
    add_student,
    add_class_to_student,
    add_course,
    add_mark_to_student,
    show_all_mark_course,
    show_all_student_course,
    calculate_GPA,
    rank_GPA,
)
# Resources
header = """███╗   ███╗ █████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝     ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
██╔████╔██║███████║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝"""
message1 = (
    "Welcome to the Student Marks Management System, an interactive and "
    "user-friendly application designed to streamline the process of managing "
    "and tracking student performance across various courses. This system is "
    "an ideal tool for educational institutions, teachers, and administrative "
    "staff who seek an efficient way to handle academic records."
)
message2 = (
    "Upon launching the Student Marks Management System, you will be greeted with a main menu offering various options, "
    "such as adding or viewing student information, managing courses, and recording marks. Navigate through these options "
    "using the mouse and keyboard, and follow the on-screen prompts to input or retrieve data."
)
startup_display = [
    "1. Enter student's information.",
    "2. Enter course's information.",
    "3. Add course to existing student.",
    "4. Show all students data.",
    "5. Show all Courses.",
    "6. Show all student from a Course.",
    "7. Add marks for a student in a given course.",
    "8. Display marks for a given course.",
    "9. Show student GPA.",
    "10. Rank student's GPA.",
    "Quit the program.",
    "Show welcome message"
]
default_font = ('TkDefaultFont', 6)

def open_message_window(parent):
    subwindow = tk.Toplevel(parent)
    subwindow.title("Welcome")
    subwindow.geometry("500x400")

    wrap_length = 450
    message_frame_1 = ttk.Frame(subwindow, padding=(10,10))
    message_frame_1.pack()
    ttk.Label(message_frame_1, text=message1, font=default_font, wraplength=wrap_length).pack()

    message_frame_2 = ttk.Frame(subwindow, padding=(10,10))
    message_frame_2.pack()
    ttk.Label(message_frame_2, text=message2, font=default_font, wraplength=wrap_length).pack()
    ttk.Button(subwindow, text="Close", command=subwindow.destroy).pack()

class Application(tk.Tk):
    def __init__(self, courseList, studentList, markList):
        super().__init__()
        self.title("GPA Management System")
        self.geometry("800x600")

        self.courseList = courseList
        self.studentList = studentList
        self.markList = markList
        self.init_ui()
    
    def init_ui(self):
        h_label = ttk.Label(self, text=header, font=("Courier", 4))
        # Main menu
        menu_frame = ttk.Frame(self, width=100)
        ttk.Button(menu_frame, text=startup_display[0], command=lambda: add_student(self.studentList, self.courseList, self.markList)).grid(column=0, row=0, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[1], command=lambda: add_course(self.courseList, self.markList)).grid(column=0, row=1, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[2], command=lambda: add_class_to_student(self.studentList, self.courseList, self.markList)).grid(column=0, row=2, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[3], command=lambda: self.studentList.show_all_student()).grid(column=0, row=3, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[4], command=lambda: self.courseList.show_courses()).grid(column=0, row=4, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[5], command=lambda: show_all_student_course(self.studentList, self.courseList)).grid(column=0, row=5, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[6], command=lambda: add_mark_to_student(self.markList, self.courseList)).grid(column=0, row=6, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[7], command=lambda: show_all_mark_course(self.markList, self.courseList)).grid(column=0, row=7, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[8], command=lambda: calculate_GPA(self.markList, self.studentList)).grid(column=0, row=8, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[9], command=lambda: rank_GPA(self.markList, self.studentList)).grid(column=0, row=9, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[10], command=self.quit).grid(column=0, row=10, sticky=tk.EW)
        ttk.Button(menu_frame, text=startup_display[11], command=lambda: open_message_window(self)).grid(column=0, row=11, sticky=tk.EW)

        # Initialize widgets
        h_label.pack(pady=20)
        menu_frame.pack()