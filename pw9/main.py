from input import get_input_as_int_curses, get_input_as_int
import curses
from curses import wrapper
from utilities import clear_screen
from domains import Students, Courses, Marks
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
from output import (
    compatibility_check,
    header_builder,
    message_builder,
)
from gui import Application
from pickle_file import compress_data
from pickle_file_thread import (
    BackgroundPickleFile,
    BackgroundImportPickleFile
)

courses = Courses()
students = Students()
marks = Marks()

import_file = BackgroundImportPickleFile(courses, students, marks)

import_file.start()
import_file.join()
courses, students, marks = import_file.return_result()

# main_window()
main_window = Application(courses, students, marks)
main_window.mainloop()

export_file = BackgroundPickleFile(courses, students, marks)
export_file.start()
export_file.join()

compress_data()