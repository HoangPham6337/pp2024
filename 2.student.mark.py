import os
import platform
from datetime import datetime


# Utility functions
def clear_screen():
    if (
        platform.uname().system == "Linux" or platform.uname().system == "Darwin"
    ):  # MacOS
        os.system("clear")
    else:
        os.system("cls")


def input_string(message) -> str:
    while True:
        data = input(message).strip()
        if check_null(data):
            print("Cannot leave input blank, please try again!")
            continue
        return data


def input_int(message) -> int:
    while True:
        data = input(message).strip()
        try:
            data = int(data)
            return data
        except ValueError:
            print("Invalid input, please try again!")

def input_float(message) -> int:
    while True:
        data = input(message).strip()
        try:
            data = float(data)
            return data
        except ValueError:
            print("Invalid input, please try again!")


def find_item_in_list(itemToFind, listToSearch, caseInsensitive) -> int:
    if caseInsensitive == 1:
        itemToFind = itemToFind.upper()
        for i in range(0, len(listToSearch)):
            if (
                listToSearch[i].get_name().upper() == itemToFind
                or listToSearch[i].get_id().upper() == itemToFind
            ):
                return i
        return -1
    else:
        for i in range(0, len(listToSearch)):
            if (
                listToSearch[i].get_name() == itemToFind
                or listToSearch[i].get_id() == itemToFind
            ):
                return i
        return -1


def find_in_list(itemToFind, listToSearch) -> int:
    for i in range(0, len(listToSearch)):
        if itemToFind == listToSearch[i]:
            return i
    return -1


def check_null(inputString) -> bool:
    return inputString == ""


def input_date(message) -> datetime:
    while True:
        date = input_string(message)
        try:
            date = datetime.strptime(date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
            return date
        except ValueError:
            print("Invalid date-time input. Please try again!")


# Courses related class and functions
class Courses:
    def __init__(self):
        self.__courses = []  # List of course object
        self.__number_of_course = 0

    def get_total(self) -> int:
        return self.__number_of_course

    def get_current(self) -> int:
        return len(self.__courses)

    def set_number_of_course(self, numberOfCourse) -> int:
        if numberOfCourse > 0:
            self.__number_of_course = numberOfCourse
            return 0
        else:
            print("Invalid input, please try again!")
            return -1

    def add_course(self, newCourse):
        if find_item_in_list(newCourse.get_name(), self.__courses, 0) != -1:
            print("Duplicate course, please try again!")
        else:
            self.__courses.append(newCourse)

    def find_course(self, courseToFind) -> int:  # Course ID or name
        return find_item_in_list(courseToFind, self.__courses, 1)

    def get_course(self, coursePosition) -> object:
        return self.__courses[coursePosition]

    def is_full(self) -> bool:
        return len(self.__courses) >= self.__number_of_course

    def check_empty(self) -> bool:
        return len(self.__courses) == 0

    def show_courses(self):
        tab_width = 20
        print(
            "Class name"
            + " " * (tab_width - 10)
            + "Class ID"
            + " " * 12
            + "Number of student"
            + " " * 3
            + "Current"
        )
        for course in self.__courses:
            print(
                course.get_name()
                + " " * (tab_width - len(course.get_name()))
                + course.get_id()
                + " " * (tab_width - len(course.get_id()))
                + str(course.get_total())
                + " " * (tab_width - len(str(course.get_total())))
                + str(course.get_current())
            )


class Course:
    def __init__(self, name, id, total):
        self.__name = name
        self.__id = id
        self.__total = total
        self.__current = 0
        self.__studentsID = []  # Student ID only, not object

    def __str__(self) -> str:
        return f"Class name {self.__name}\nClass Id: {self.__id}\nTotal student: {self.__total}\nCurrent number of student: {self.__current}"

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_total(self) -> int:
        return self.__total

    def set_total(self, newTotal):
        if newTotal > 0 and newTotal > self.__total:
            self.__total = newTotal
        elif newTotal < self.__total:
            print("Input smaller than current number of student. Please try again!")
        else:
            print("Invalid input, please try again!")

    def get_current(self) -> int:
        return self.__current

    def is_full(self) -> bool:
        return self.__current >= self.__total

    def add_student(self, newStudentID) -> int:
        if self.is_full():
            if (
                input_string(
                    "The course is full. Do you want to add more student? (Y/N) "
                ).upper()
                == "Y"
            ):
                self.set_total(
                    input_int(
                        f"Current maximum: {self.get_total()}. Enter the new value: "
                    )
                )
            else:
                input(f"Failed to add student to course, please try again!")
                return -1

        if find_in_list(newStudentID, self.__studentsID) == -1:
            self.__current += 1
            self.__studentsID.append(newStudentID)
            return 0
        else:
            print("Duplicate student.")
            return -1

    def check_duplicate_student(self, newStudentID):
        return find_in_list(newStudentID, self.__studentsID) != -1

    def show_all_student(self, studentList):
        tabWidth = 20
        print(
            "Student name"
            + " " * 8
            + "Student ID"
            + " " * 10
            + "Date of birth"
            + " " * 7
        )
        for studentID in self.__studentsID:
            studentPosition = studentList.find_student(studentID)
            student = studentList.get_student(studentPosition)
            print(
                student.get_name()
                + " " * (tabWidth - len(student.get_name()))
                + student.get_id()
                + " " * (tabWidth - len(student.get_id()))
                + student.get_dob()
            )


def add_course(courseList):
    if courseList.is_full():
        choice = input_string("Course list is full, do you want to increase the number of courses? (Y/N) ").upper()
        if choice == "N":
            return
        print(f"Current number of courses: {courseList.get_current()}")
        while True:
            if (courseList.set_number_of_course(input_int("Enter new number of courses: "))== -1):
                continue
            break
    name, id, total = "", "", 0
    name = input_string("Enter the class name: ").title()
    id = input_string("Enter the class ID: ").upper()
    total = int(input_string("Enter the number of student in the class: "))
    newCourse = Course(name, id, total)
    courseList.add_course(newCourse)


def show_all_student_course(studentList, courseList):
    courseInput = input_string("Enter class name or ID: ")
    coursePosition = courseList.find_course(courseInput)
    if coursePosition == -1:
        input("Class not found, press Enter to continue.")
        return
    course = courseList.get_course(coursePosition)
    print(course)
    course.show_all_student(studentList)


# Student related class and function
class Students:
    def __init__(self):
        self.__students = []  # List of object student

    def add_student(self, newStudent):  # Object newStudent
        self.__students.append(newStudent)

    def check_duplicate(self, newStudent):
        return find_item_in_list(newStudent.get_id(), self.__students, 0) != -1

    def find_student(self, student) -> int:
        return find_item_in_list(student, self.__students, 1)

    def get_student(self, studentPosition) -> object:
        return self.__students[studentPosition]

    def show_all_student(self):
        tab_width = 20
        print(
            "Student name"
            + " " * 8
            + "Student ID"
            + " " * 10
            + "Date of birth"
            + " " * 7
        )
        for student in self.__students:
            print(
                student.get_name()
                + " " * (tab_width - len(student.get_name()))
                + student.get_id()
                + " " * (tab_width - len(student.get_id()))
                + student.get_dob()
            )


class Student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob

    def __str__(self) -> str:
        return (
            f"Student name: {self.__name}\nStudent ID: {self.__id}\nDOB: {self.__dob}"
        )

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_dob(self) -> str:
        return self.__dob


def add_student(studentList, courseList):
    if courseList.check_empty():
        input("Class list empty, please add a class. Press Enter to try again!")
        return
    newStudent, name, id, dob = "", "", "", ""
    while True:
        name = input_string("Enter student name: ").title()
        id = input_string("Enter student ID: ").upper()
        dob = input_date(f'Enter "{name}" date of birth (DD-MM-YYYY): ')
        newStudent = Student(name, id, dob)
        if studentList.check_duplicate(newStudent):
            print("Duplicate student, please try again!")
            continue
        break
    studentList.add_student(newStudent)
    courseList.show_courses()
    while True:
        courseChoice = input_string('Enter the class ID to add student or "empty" to skip:').upper()
        if courseChoice == "EMPTY":
            break
        coursePosition = courseList.find_course(courseChoice)
        if coursePosition == -1:
            input("Course not found, press Enter to try again!")
            continue
        course = courseList.get_course(coursePosition)

        if course.add_student(newStudent.get_id()) == -1:
            continue

        # Add maximum check
        break


def add_student_standalone(studentList, courseList):
    student = ""
    while True:
        studentInput = input_string("Enter student name or id: ").upper()
        studentPosition = studentList.find_student(studentInput)
        if studentPosition == -1:
            print("Student not found, please try again!")
            continue
        student = studentList.get_student(studentPosition)
        break
    courseList.show_courses()

    while True:
        courseInput = input("Enter course name or ID to add student: ")
        coursePosition = courseList.find_course(courseInput)
        if coursePosition == -1:
            choice = input_string(
                "Course not found, do you want to try again? (Y/N) "
            ).upper()
            if choice == "Y":
                continue
            else:
                return
        course = courseList.get_course(coursePosition)
        if course.check_duplicate_student(student.get_id()):
            print("Duplicate student, please try again!")
            continue
        course.add_student(student.get_id())
        break


students = Students()
courses = Courses()

courses.set_number_of_course(input_int("Enter number of courses: "))
while True:
    clear_screen()
    startup_display = (
        "1. Enter student's information.\n"
        + "2. Enter course's information\n"
        + "3. Add class to existing student\n"
        + "4. Show all students data\n"
        + "5. Show all classes\n"
        + "6. Show all student from a class\n"
        + "7. Add marks for a student in a given course.\n"
        + "8. Display marks for a given course\n"
        + '"exit" to quit the program.\n'
    )
    choice = input(startup_display)

    match choice:
        case "1":
            clear_screen()
            add_student(students, courses)

        case "2":
            clear_screen()
            add_course(courses)
            input()
        case "3":
            clear_screen()
            add_student_standalone(students, courses)
            input()
        case "4":
            clear_screen()
            students.show_all_student()
            input()
        case "5":
            clear_screen()
            print(
                f"Maximum number of courses: {courses.get_total()}\nCurrent number of courses: {courses.get_current()}\n"
            )
            courses.show_courses()
            input()
        case "6":
            clear_screen()
            show_all_student_course(students, courses)
            input()
        case "7":
            clear_screen()
        case "8":
            clear_screen()
        case "exit":
            exit()
        case _:
            input("Invalid input, please try again. Press Enter to continue.")
