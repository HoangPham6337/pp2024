from input import (
    get_input_as_string,
    get_input_as_int,
    get_input_as_date,
    get_input_as_float_floor,
)

from domains.Course import Course
from domains.Mark import Mark
from domains.Student import Student
from domains.StudentMark import StudentMark

from utilities import clear_screen, output_padding


def add_course(courseList, markList):
    if courseList.is_full():
        increase_courses = get_input_as_string(
            "Course list is full, increase the number of courses? (Y/N) "
        ).upper()
        if increase_courses == "N":
            return
        print(f"Current number of courses: {courseList.get_current()}")
        while True:
            if (
                courseList.set_number_of_course(
                    get_input_as_int("Enter new number of courses: ")
                )
                == -1
            ):
                continue
            break
    name, id, total = "", "", 0
    name = get_input_as_string("Enter the Course name: ").title()
    id = get_input_as_string("Enter the Course ID: ").upper()
    total = get_input_as_int("Enter the number of student in the course: ")
    ECTs = get_input_as_int("Enter ECTs: ")
    newCourse = Course(name, id, total)
    newMark = Mark(name, id, ECTs)
    courseList.add_course(newCourse)
    markList.add_course(newMark)


def show_all_student_course(studentList, courseList):
    courseInput = get_input_as_string("Enter Course name or ID: ")
    coursePosition = courseList.find_course(courseInput)
    if coursePosition == -1:
        input("Course not found, press Enter to continue.")
        return
    course = courseList.get_course(coursePosition)
    print(course)
    course.show_all_student(studentList)


def add_student(studentList, courseList, markList):
    if courseList.check_empty():
        input("Course list empty, please add a Course. Enter to try again!")
        return
    newStudent, name, id, dob = "", "", "", ""
    while True:
        name = get_input_as_string("Enter student name: ").title()
        id = get_input_as_string("Enter student ID: ").upper()
        dob = get_input_as_date(f'Enter "{name}" date of birth (DD-MM-YYYY): ')
        newStudent = Student(name, id, dob)
        newMark = StudentMark(name, id, dob)
        if studentList.check_duplicate(newStudent):
            print("Duplicate student, please try again!")
            continue
        break
    studentList.add_student(newStudent)

    courseList.show_courses()
    while True:
        courseChoice = get_input_as_string(
            'Enter the Course ID to add student or "empty" to skip: '
        ).upper()
        if courseChoice == "EMPTY":
            break
        coursePosition = courseList.find_course(courseChoice)
        if coursePosition == -1:
            input("Course not found, press Enter to try again!")
            continue
        course = courseList.get_course(coursePosition)
        mark = markList.get_course(coursePosition)

        if course.add_student(newStudent.get_id()) == -1:
            continue

        markChoice = get_input_as_string(
            "Do you want to add mark to student? (Y/N): "
        ).upper()
        if markChoice == "Y":
            while True:
                if newMark.set_mark(get_input_as_float_floor("Enter mark: ")) != -1:
                    break
        mark.add_student(newMark)
        break


def add_class_to_student(studentList, courseList, markList):
    if studentList.check_empty():
        input("No student found, please add one!\nEnter to continue.")
        return
    student, mark = "", ""
    while True:
        studentInput = get_input_as_string("Enter student name or id: ").upper()
        studentPosition = studentList.find_student(studentInput)
        if studentPosition == -1:
            print("Student not found, please try again!")
            continue
        clear_screen()
        student = studentList.get_student(studentPosition)
        print(student)
        break
    print()
    courseList.show_courses()

    while True:
        courseInput = get_input_as_string("Enter course name or ID to add student: ")
        coursePosition = courseList.find_course(courseInput)
        if coursePosition == -1:
            choice = get_input_as_string(
                "Course not found, do you want to try again? (Y/N) "
            ).upper()
            if choice == "N":
                return
        mark = markList.get_course(coursePosition)
        course = courseList.get_course(coursePosition)
        if course.check_duplicate_student(student.get_id()):
            print("Duplicate student, please try again!")
            continue
        course.add_student(student.get_id())
        break

    newMark = StudentMark(student.get_name(), student.get_id(), student.get_dob())
    while True:
        # if newMark.set_mark(get_input_as_float("Enter mark: ")) != -1:
        if newMark.set_mark(get_input_as_float_floor("Enter mark: ")) != -1:
            break
    mark.add_student(newMark)


def add_mark_to_student(markList, courseList):
    if courseList.check_empty():
        input("No course found, press Enter to continue!")
        return
    while True:
        mark = show_all_mark_course(markList, courseList)
        if mark:
            break
    print()
    studentInput = get_input_as_string("Enter student name or ID: ")

    studentPosition = mark.find_student(studentInput)
    if studentPosition == -1:
        input("Student not found, please try again!")
        return
    studentMark = mark.get_student(studentPosition)
    while True:
        if studentMark.set_mark(get_input_as_float_floor("Enter mark: ")) != -1:
            break


def show_all_mark_course(markList, courseList) -> object:
    courseInput = get_input_as_string("Enter Course name or ID: ")
    coursePosition = courseList.find_course(courseInput)
    if coursePosition == -1:
        input("Course not found, press Enter to continue.")
        return None
    mark = markList.get_course(coursePosition)
    clear_screen()
    print(mark)
    print()
    mark.show_all_student()
    return mark


def calculate_GPA(markList, studentList):
    studentInput = get_input_as_string("Enter student name or ID: ")
    if studentList.find_student(studentInput) == -1:
        print("Student not found, please try again!")
        return
    GPA = markList.calculate_GPA(studentInput, False)
    print("GPA: " + str(GPA))


def rank_GPA(markList, studentList):
    students = studentList.get_student_list()
    totalStudents = len(students)

    for student in students:
        student.set_GPA(markList.calculate_GPA(student.get_name(), True))

    # Bubble sort, horrible complexity but just to implement sorting
    for i in range(0, totalStudents):
        for j in range(0, totalStudents - i - 1):
            if students[j].__eq__(students[j + 1]):
                continue
            if students[j].__lt__(students[j + 1]):
                temp = students[j]
                students[j] = students[j + 1]
                students[j + 1] = temp

    headers = ["Student name", "Student ID", "GPA"]
    widths = [8, 10, 13]
    for header, width in zip(headers, widths):
        print(f"{header}{' ' * width}", end="")
    print()

    for student in students:
        print(
            f"{student.get_name()}{output_padding(student.get_name())}"
            f"{student.get_id()}{output_padding(student.get_id())}"
            f"{student.get_GPA()}"
        )
