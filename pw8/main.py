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
from pickle_file import (
    create_dir,
    import_pickle_wrapper,
    pickle_courses,
    pickle_file_wrapper,
    pickle_students,
    pickle_marks,
    pickle_load_courses,
    pickle_load_students,
    pickle_load_marks,
    compress_data,
    extract_data
)
from pickle_file_thread import (
    BackgroundPickleFile,
    BackgroundImportPickleFile
)

courses = Courses()
students = Students()
marks = Marks()

# create_dir()
# extract_data()
# pickle_load_courses(courses)
# pickle_load_students(students)
# pickle_load_marks(marks)
# courses, students, marks = import_pickle_wrapper(courses, students, marks)
import_file = BackgroundImportPickleFile(courses, students, marks)

import_file.start()
import_file.join()
courses, students, marks = import_file.return_result()

def choose_menu(choice):
    match str(choice):
        case "1":
            clear_screen()
            add_student(students, courses, marks)
        case "2":
            clear_screen()
            add_course(courses, marks)
        case "3":
            clear_screen()
            students.show_all_student()
            add_class_to_student(students, courses, marks)
        case "4":
            clear_screen()
            students.show_all_student()
            input("Press Enter to return.")
        case "5":
            clear_screen()
            print(
                f"Maximum number of courses: {courses.get_total()}\n"
                f"Current number of courses: {courses.get_current()}\n"
            )
            courses.show_courses()
            input("Press Enter to return.")
        case "6":
            clear_screen()
            show_all_student_course(students, courses)
            input("Press Enter to return.")
        case "7":
            clear_screen()
            courses.show_courses()
            add_mark_to_student(marks, courses)
        case "8":
            clear_screen()
            courses.show_courses()
            show_all_mark_course(marks, courses)
            input("Press Enter to return.")
        case "9":
            clear_screen()
            calculate_GPA(marks, students)
            input("Press Enter to return.")
        case "10":
            clear_screen()
            rank_GPA(marks, students)
            input("Press Enter to return.")
        case "11":
            clear_screen()
            exit()
        case "exit":
            clear_screen()
            return "exit"

use_old_ui = False
def welcome_screen(stdscr):
    curses.curs_set(False)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    BLUE_AND_BLACK = curses.color_pair(1)
    # WHITE_AND_RED = curses.color_pair(2)
    # WCYAN_AND_BLACK = curses.color_pair(2)
    stdscr.clear()
    stdscr.refresh()

    max_y, max_x = stdscr.getmaxyx()

    if compatibility_check(stdscr, max_y, max_x, 2):
        clear_screen()
        return True
    else:
        header_builder(stdscr, 1, max_x)

    message_builder(stdscr, 3, max_x)

    menuWindow = curses.newwin(15, 45, 21, (max_x - 34) // 2)
    choiceWindow = curses.newwin(2, 11, 21, (max_x - 58) // 2)

    if (courses.get_total() == 0):
        curses.curs_set(True)
        courses.set_number_of_course(
            get_input_as_int_curses(menuWindow, "Enter number of courses: ", False, 19)
        )
        curses.curs_set(False)
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
        '"exit" to quit the program.',
    ]

    option = 1
    while True:
        menuWindow.clear()
        for i in range(0, len(startup_display)):
            if i == option - 1:
                display = "=>" + startup_display[i]
                menuWindow.addstr(i, 0, display, curses.A_BLINK | BLUE_AND_BLACK)
            else:
                menuWindow.addstr(i, 0, startup_display[i])
        menuWindow.refresh()

        key = stdscr.getkey()
        if key == "KEY_UP":
            option -= 1 if option >= 0 else 0
            if option == 0:
                option = 11
        elif key == "KEY_DOWN":
            option += 1 if option < 12 else 0
            if option == 12:
                option = 1
        elif key in [10, "\n", "\r", curses.KEY_ENTER]:
            if option == 11:
                break
            elif option in range(1, 11):
                curses.endwin()
                choose_menu(option)
            # Return the terminal back to curses
            stdscr = curses.initscr()
            curses.cbreak()
            stdscr.keypad(True)
        elif key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            choiceWindow.addstr("Choice: ")
            choice = get_input_as_int_curses(choiceWindow, "", True, 2)
            choiceWindow.clear()
            choiceWindow.refresh()
            curses.endwin()
            choose_menu(choice)
            curses.cbreak()
            stdscr.keypad(True)
        export_file = BackgroundPickleFile(courses, students, marks)
        export_file.start()
        export_file.join()
    return False

use_old_ui = wrapper(welcome_screen)
if use_old_ui:
    clear_screen()
    if courses.get_total() == 0:
        courses.set_number_of_course(get_input_as_int("Enter number of courses: "))
    while True:
        clear_screen()
        startup_display = (
            "1. Enter student's information.\n"
            + "2. Enter course's information\n"
            + "3. Add course to existing student\n"
            + "4. Show all students data\n"
            + "5. Show all Courses\n"
            + "6. Show all student from a Course\n"
            + "7. Add marks for a student in a given course.\n"
            + "8. Display marks for a given course\n"
            + "9. Show student GPA\n"
            + "10. Rank student's GPA\n"
            + '"exit" to quit the program.\n'
        )
        choice = input(startup_display)
        exitCode = choose_menu(choice)
        if exitCode == "exit":
            break
        export_file = BackgroundPickleFile(courses, students, marks)
        export_file.start()
        export_file.join()

# pickle_courses(courses)
# pickle_students(students)
# pickle_marks(marks)
# pickle_file_wrapper(courses, students, marks)
compress_data()