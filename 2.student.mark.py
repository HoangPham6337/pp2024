import os
from datetime import datetime

# Utility functions
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


def find_item_in_list(item_to_find, list_to_search) -> int:
    for i in range(0, len(list_to_search)):
        if list_to_search[i].get_name() == item_to_find or list_to_search[i].get_id() == item_to_find:
            return i
    return -1

def find_in_list(item_to_find, list_to_search) -> int:
    for i in range(0, len(list_to_search)):
        if item_to_find == list_to_search[i]:
            return i
    return -1

def check_null(input_string) -> bool:
    return input_string == ""

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
        self.number_of_course = 0
    
    def set_number_of_course(self, number_of_course):
        if number_of_course > 0:
            self.number_of_course = number_of_course
        else:
            print("Invalid input, please try again!")
    
    def addCourse(self, newCourse):
        if find_item_in_list(newCourse.get_name(), self.__courses) != -1:
            print("Duplicate course, please try again!")
        elif len(self.__courses) >= self.number_of_course:
            print("Maximum number of courses reach, please increase the limit.")
        else:
            self.__courses.append(newCourse)
    
    def show_courses(self):
        tab_width = 20
        print("Class name" + " " * (tab_width - 10) + "Class ID" + " " * 12 + "Number of student" + " " * 3 + "Current")
        for course in self.__courses:
            print(
                course.get_name() + " " * (tab_width - len(course.get_name())) +
                course.get_id() + " " * (tab_width - len(course.get_id())) +
                str(course.get_total()) + " " * (tab_width - len(str(course.get_total()))) +
                str(course.get_current())
            )

class Course:
    def __init__(self, name, id, total):
        self.__name = name
        self.__id = id
        self.__total = total
        self.__current = 0
        self.__students = []

    def __str__(self) -> str:
        return f"Class name {self.__name}\nClass Id: {self.__id}\nTotal student: {self.__total}\nCurrent number of student: {self.__current}"

    def get_name(self) -> str:
        return self.__name
    
    def get_id(self) -> str:
        return self.__id

    def get_total(self) -> int:
        return self.__total

    def set_total(self, total):
        if total > 0 and total > self.__total:
            self.__total = total
        elif total < self.__total:
            print("Input smaller than current number of student. Please try again!")
        else:
            print("Invalid input, please try again!")
    
    def get_current(self) -> int:
        return self.__current
    
    def add_student(self, newStudent, student_list):
        if find_item_in_list(newStudent, student_list) == -1:
            self.__current += 1
            self.__students.append(newStudent)

    def is_full(self) -> bool:
        return self.__current < self.__total

def add_course(course_list):
    name, id, total = "", "", 0
    name = input_string("Enter the class name: ").title()
    id = input_string("Enter the class ID: ").upper()
    total = int(input_string("Enter the number of student in the class: "))
    newCourse = Course(name, id, total)
    course_list.addCourse(newCourse)


# Student related class and function
class Students:
    def __init__(self):
        self.__students = []  # List of object student

    def add_student(self, newStudent):  # Object newStudent
        self.__students.append(newStudent)

    def check_duplicate(self, newStudent):
        return find_item_in_list(newStudent.get_id(), self.__students) != -1
    
    def show_all_student(self):
        tab_width = 20
        for student in self.__students:
            print(
                student.get_name() + " " * (tab_width - len(student.get_name())) +
                student.get_id() + " " * (tab_width - len(student.get_id())) +
                student.get_dob()
            )

class Student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
    
    def __str__(self) -> str:
        return f"Student name: {self.__name}\nStudent ID: {self.__id}\nDOB: {self.__dob}"

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id
    
    def get_dob(self) -> str:
        return self.__dob

def add_student(student_list):
    name, id, dob = "", "", ""
    while True:
        name = input_string("Enter student name: ").title()
        id = input_string("Enter student ID: ").upper()
        dob = input_date(f"Enter \"{name}\" date of birth (DD-MM-YYYY): ")
        newStudent = Student(name, id, dob)
        if student_list.check_duplicate(newStudent):
            continue
        break

    student_list.add_student(newStudent)
    student_list.show_all_student()

students = Students()
courses = Courses()
# marks = Marks("MAT101")

courses.set_number_of_course(input_int("Enter number of courses: "))
while True:
    os.system("cls")
    startup_display = "1. Enter student's information.\n" + "2. Enter course's information\n" + "3. Add class to existing student\n" + "4. Show all students data\n" + "5. Show all classes\n" + "6. Show all student from a class\n" + "7. Display marks for a given course\n"
    choice = input(startup_display)
    
    match choice:
        case "1":
            os.system("cls")
            add_student(students)

        case "2":
            os.system("cls")
            add_course(courses)
            input()
        case "3":
            os.system("cls")
        case "4":
            os.system("cls")
        case "5":
            os.system("cls")
            courses.show_courses()
            input()
        case "6":
            os.system("cls")
        case "7":
            os.system("cls")
        case "8":
            os.system("cls")
        case "exit":
            exit()
        case _:
            input("Invalid input, please try again. Press Enter to continue.")