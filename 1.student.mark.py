import os
# Utility functions

def formatted_input(message, option):
    user_input = input(message).strip()
    if option == 1:
        user_input = user_input.upper()
    elif option == 2:
        user_input = user_input.title()
    elif option == 3:
        user_input = user_input.capitalize()
    return user_input

def check_null(input_string):
    if input_string == "":
        return True
    return False

def check_duplicate_in_list(check_case, list_to_search):
    for item in list_to_search:
        for key in item.keys():
            if key == check_case or item[key] == check_case:
                return True
        return False

def is_class_full(class_to_check):
    if class_to_check["Current"] < class_to_check["Total"]:
        return False
    return True

def find_dict_in_list(key, dict_to_find, list_to_search):
    for i in range(0, len(list_to_search)):
        if list_to_search[i][key] == dict_to_find:
            return i
    return -1

# Function for adding information
def add_class(class_list):
    class_name = formatted_input("Enter the class name: ", 3)
    class_id = formatted_input("Enter the class ID: ", 1)
    number_of_student = int(input("Enter number of student for this class: "))

    # Check for duplication in class list
    if check_duplicate_in_list(class_name, class_list) or check_duplicate_in_list(class_id, class_list):
        input("Duplicate class, please try again!")

    new_class = {
        "Name": class_name,
        "ID": class_id,
        "Total": number_of_student,
        "Current": 0,
        "Student list": [],
        "Mark list": []
    }
    class_list.append(new_class) 

def add_student(student_list, class_list):
    # Input student's data
    student_name = formatted_input("Enter your student's name: ", 2)  # Capitalize every first letter
    student_id = formatted_input(f"Enter {student_name} ID: ", 1)

    if check_duplicate_in_list(student_name, student_list) or check_duplicate_in_list(student_id, student_list):
        # Check for student duplication: name, id
        input("Duplicate student, please try again!")
        return

    student_dob = input(f"Enter {student_name} date of birth: ").strip()

    student = {
        "Name": student_name,
        "ID": student_id,
        "DOB": student_dob,
    }
    add_student_to_class(student, class_list)
    student_list.append(student)

def add_student_to_class(student, class_list):
    show_all_class(class_list)
    class_to_add = formatted_input("Enter the class ID to add: ", 1)

    if check_null(class_to_add):
        return

    class_position = find_dict_in_list("ID", class_to_add, class_list)
    if class_position != -1:
        if is_class_full(class_list[class_position]):
            if formatted_input(f"The class is full, do you want to increase the total number of student in {class_to_add} (Y/N): ", 1) == 'Y':
                class_list[class_position]["Total"] += 1
            else:
                input(f"Failed to add to {class_to_add}, please choose another class. Press Enter to continue.")
                return
        class_list[class_position]["Student list"].append(student["ID"])
        class_list[class_position]["Current"] += 1
    else:
        input("Class not found, class set to None. Press Enter to continue.")

def add_student_class_standalone(student_list, class_list):
    student = formatted_input("Enter student ID: ", 1)
    if find_dict_in_list("ID", student, student_list) != -1:
        add_student_to_class({"ID": student}, class_list)
    else:
        input("Student not found! Press Enter to continue.")

def add_mark(student_list, class_list):
    _class = formatted_input("Enter class ID: ", 1)
    class_position = find_dict_in_list("ID", _class, class_list)
    if class_position == -1:
        input("Class not found, press Enter to try again.")

    student = formatted_input("Enter student ID: ", 1)
    student_position = find_dict_in_list("ID", student, student_list)
    if student_position == -1:
        input("Student not found, press Enter to try again.")
    mark = input("Enter student mark: ")
    class_list[class_position]["Mark list"].append({student: mark})

# Functions for query information
def show_all_student(student_list):
    tab_width = 20
    print("Student name" + " " * 8 + "Student ID" + " " * 10 + "Date of birth" + " " * 7)
    for student in student_list:
        for item in student.keys():
            if len(item) < tab_width:
                print(student[item] + " " * (tab_width - len(student[item])), end="")  # Formatted output
            else:
                print(student[item], end="")
        print()

def show_all_class(class_list):
    tab_width = 20
    print("Class name" + " " * (tab_width - 10) + "Class ID" + " " * 12 + "Number of student" + " " * 3 + "Current")
    for item in class_list:
        # If the class name smaller than tab_width, insert spaces to align the output
        print(
            item["Name"] + " " * (tab_width - len(item["Name"])) +
            item["ID"] + " " * (tab_width - len(item["ID"])) +
            str(item["Total"]) + " " * (tab_width - len(str(item["Total"]))) +
            str(item["Current"])
        )

def show_students_class(student_list, class_list):
    tab_width = 20
    class_to_display = formatted_input("Enter the class ID to display: ",1)
    class_position = find_dict_in_list("ID", class_to_display, class_list)
    if class_position == -1:
        input("No class found. Press Enter to try again!")
        return

    print("Student name" + " " * 8 + "Student ID" + " " * 10 + "Date of birth" + " " * 7)
    for student in class_list[class_position]["Student list"]:
        student_position = find_dict_in_list("ID", student, student_list)
        student_data = student_list[student_position]
        for key in student_data.keys():
            print(student_data[key] + " " * (tab_width - len(student_data[key])), end="")
        print()

def show_mark(student_list, class_list):
    tab_width = 20
    class_to_display = formatted_input("Enter the class ID to display: ",1)
    class_position = find_dict_in_list("ID", class_to_display, class_list)   
    if class_position == -1:
        input("No class found. Press Enter to try again!")
        return
    print("Student name" + " " * 8 + "Student ID" + " " * 10 + "Mark")
    for student in class_list[class_position]["Mark list"]:
        for key in student.keys():
            student_position = find_dict_in_list("ID", key, student_list)
            student_data = student_list[student_position]
            print(
                student_data["Name"] + " " * (tab_width - len(student_data["Name"])) + 
                student_data["ID"] + " " * (tab_width - len(student_data["ID"])) + 
                student[key]
            )
# Initialize program data
classes = []
students = []

while True:
    os.system("cls")
    startup_display = "1. Enter student's information.\n" + "2. Enter class's information\n" + "3. Add class to existing student\n" + "4. Show all students data\n" + "5. Show all classes\n" + "6. Show all student from a class\n" + "7. Display marks for a given course\n"
    choice = input(
        "Enter your choice: \n" + 
        "1. Enter student's information.\n" + "2. Enter class's information.\n" + 
        "3. Add class to existing student.\n" + "4. Show all students data.\n" + 
        "5. Show all classes.\n" + "6. Show all student from a class.\n" + 
        "7. Add marks for a student in a given course.\n" + "8. Display marks for a given course.\n"
    )
    match choice:
        case "1":
            os.system("cls")
            if len(classes) == 0:
                input("Class list empty, enter a class first. Please try again!")
                continue
            add_student(students, classes)
        case "2":
            os.system("cls")
            add_class(classes)
        case "3":
            os.system("cls")
            add_student_class_standalone(students, classes)
        case "4":
            os.system("cls")
            show_all_student(students)
            input("Press Enter to continue.")
        case "5":
            os.system("cls")
            show_all_class(classes)
            input("Press Enter to continue.")
        case "6":
            os.system("cls")
            show_students_class(students, classes)
            input("Press Enter to continue.")
        case "7":
            os.system("cls")
            add_mark(students, classes)
            input("Press Enter to continue.")
        case "8":
            os.system("cls")
            show_mark(students, classes)
            input("Press Enter to continue.")
        case "exit":
            exit()
        case _:
            input("Invalid input, please try again. Press Enter to continue.")