import os
from datetime import datetime


# Utility functions
def input_data(message) -> str:
    while True:
        data = input(message).strip()
        if check_null(data):
            print("Cannot leave input blank, please try again!")
            continue
        return data

def check_null(input_string) -> bool:
    if input_string == "":
        return True
    return False

def check_duplicate_list_obj(check_case, list_to_search, item_of_interest) -> bool:
    for item in list_to_search:
        if item.get_name() == check_case or item.get_id() == check_case:
            print(f"Duplicate {item_of_interest} found, please try again!")
            return True
    return False

def find_item_in_list(item_to_find, list_to_search):
    for i in range(0, len(list_to_search)):
        if list_to_search[i].get_name() == item_to_find or list_to_search[i].get_id() == item_to_find:
            return i
    return -1


# All about the course
class Course:
    def __init__(self, name, id, total):
        self.__name = name
        self.__id = id
        self.__total = total
        self.__current = 0

    def __str__(self) -> str:
        return f"Class name: {self.__name}\nClass ID: {self.__id}"
    
    def get_name(self) -> str:
        return self.__name
    
    def get_id(self) -> str:
        return self.__id
    
    def get_total_student(self) -> int:
        return self.__total
    
    def get_current_student(self) -> int:
        return self.__current

    def modify_total_student(self, number_student):
        if (number_student < 0):
            print(f"Invalid input, failed to change {self.__name} number of student")
        self.__total = number_student
    
    def add_current_student(self):
        self.__current += 1;

    def is_full(self) -> bool:
        if self.__current < self.__total:
            return False
        return True
    
def add_course(course_list, mark_list, course_limit):
        name, id, total = "", "", ""
        if len(course_list) >= course_limit:
            if input_data("Course limit reach, do you want to add more course? (Y/N)").upper() == 'Y':
                course_limit += 1
            else:
                print("Failed to add more course.")

        while True:
            name = input_data("Enter the course name: ").title()
            if check_duplicate_list_obj(name, course_list, "course"):
                continue
            id = input_data("Enter the class ID: ").upper()
            if check_duplicate_list_obj(id, course_list, "course"):
                continue
            break
        
        mark_list.append(Mark(id))
        
        while True:
            try:
                total = int(input_data("Enter the number of students: "))
                break
            except ValueError:
                print("Invalid input, enter number only. Please try again!")
        course_list.append(Course(name, id, total))

def show_all_courses(course_list):
    print("Class name" + " " * (tab_width - 10) + "Class ID" + " " * 12 + "Number of student" + " " * 3 + "Current")
    for course in course_list:
        total_student = str(course.get_total_student())
        current_student = str(course.get_current_student())
        print(
            course.get_name() + " " * (tab_width - len(course.get_name())) +
            course.get_id() + " " * (tab_width - len(course.get_id())) +
            total_student + " " * (tab_width - len(total_student)) +
            current_student + " " * (tab_width - len(current_student))
        )

class Mark:
    def __init__(self, class_id):
        self.__id = class_id
        self.__students_mark = []  # List of dictionary {ID: mark}
    
    def __str__(self):
        return f"This is the marking list for {self.id}"
    
    def get_id(self) -> str:
        return self.__id

    def add_mark(self, student_id, mark, student_list):
        if find_item_in_list(student_id, student_list) != -1:
            if mark > 0:
                student_mark = {
                    "ID": student_id,
                    "Mark": mark
                }
                self.__students_mark.append(student_mark)

    def show_mark(self, student_id) -> dict:
        for student in self.__students_mark:
            if student["ID"] == student_id:
                return student
        return None

    def show_all_mark(self, student_list):
        tab_width = 20
        print("Student name" + " " * 8 + "Student ID" + " " * 10 + "Mark")
        for student in self.__students_mark:
            student_position= find_item_in_list(self.__id, student_list)
            student_data = student_list[student_position]
            print(
                student_data.get_name() + " " * (tab_width - len(student_data.get_name())) +
                student_data.get_id() + " " * (tab_width - len(student_data.get_id())) +
                str(student["Mark"])
            )


# All about students
class Student:
    def __init__(self, name, id, dob, student_list):
        __name = name
        __id = id
        __dob = dob
        __courses = []
    
    def __str__(self) -> str:
        return f"Student name: {self.name}\nStudent ID: {self.id}"
    
    def get_name(self) -> str:
        return self.__name
    
    def get_id(self) -> str:
        return self.__id
    
    def set_courses(self, new_course):
        self.__courses.append(new_course)

    def get_courses(self) -> list:
        return self.__courses
    

def add_student(student_list, course_list):
    while True:
        name = input_data("Enter student name: ").title()
        if not check_duplicate_list_obj(name, student_list, "student"):
            break
        id = input_data("Enter student ID: ").upper()
        if not check_duplicate_list_obj(id, student_list, "student"):
            break
        
    


#Global variable
tab_width = 20
course_limit = int(input_data("Enter number of courses: "))
courses = []
students = []
marks = []

while True:
    os.system("cls")
    startup_display = "1. Enter student's information.\n" + "2. Enter class's information\n" + "3. Add class to existing student\n" + "4. Show all students data\n" + "5. Show all classes\n" + "6. Show all student from a class\n" + "7. Display marks for a given course\n"
    choice = input(
        "Enter your choice: \n" + 
        "1. Enter student's information.\n" + "2. Enter class's information.\n" + 
        "3. Add class to existing student.\n" + "4. Show all students data.\n" + 
        "5. Show all classes.\n" + "6. Show all student from a class.\n" + 
        "7. Add marks for a student in a given course.\n" + "8. Display marks for a given course.\n" +
        '"exit" to quit the program.\n'
    )
    match choice:
        case "1":
            os.system("cls")
        case "2":
            add_course(courses, marks, course_limit)
            os.system("cls")
        case "3":
            os.system("cls")
        case "4":
            os.system("cls")
        case "5":
            show_all_courses(courses)
            input()
            os.system("cls")
        case "6":
            os.system("cls")
        case "7":
            os.system("cls")
        case "8":
            os.system("cls")
            marks[0].show_all_mark(students)
        case "exit":
            exit()
        case _:
            input("Invalid input, please try again. Press Enter to continue.")