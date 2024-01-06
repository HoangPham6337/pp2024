print("Student grade management system.")


# Utility functions ----------------------------------------------------------------------------------------------------
# Function to check if input is NULL
def check_null(input_string):
    if input_string == "":
        return True
    return False


# Function to search for a dict in a list
def search_list_of_dictionary(search_term, list_to_search):
    for item in list_to_search:
        for key in item.keys():
            if key == search_term:
                return True
            if item[key] == search_term:
                return True
    return False


# Function to check duplication in a list, check both key and key's value
def check_duplicate_in_list(check_case, list_to_search):
    for item in list_to_search:
        for key in item.keys():
            if key == check_case:
                return True
            if item[key] == check_case:
                return True
    return False


# Function to check if a class is full
def is_class_full(class_to_add):
    if class_to_add["Current student"] < class_to_add["Number of student"]:
        return False
    return True


def find_item_in_list(item_to_search, list_to_search):
    for i in range(0, len(list_to_search)):
        if list_to_search[i]["Class name"] == item_to_search or list_to_search[i]["Class ID"] == item_to_search:
            return i
    return -1


# Function for adding information --------------------------------------------------------------------------------------
# Create a function to add student
def add_student(class_list, student_list):
    # Input student's data
    student_name = input("Enter your student's name: ").title().strip()  # Capitalize every first letter
    student_id = input(f"Enter {student_name} ID: ").upper().strip()

    if check_duplicate_in_list(student_name, student_list) or check_duplicate_in_list(student_id, student_list):
        # Check for student duplication: name, id
        print("Duplicate student, please try again!")
        return

    student_dob = input(f"Enter {student_name} date of birth: ").strip()

    student = {
        "Student name": student_name,
        "Student ID": student_id,
        "DOB": student_dob,
        "Class ID": add_student_to_class(class_list)
    }
    student_list.append(student)
    student_list.sort()


# Create a function to add class
def add_class(class_list):
    class_name = input("Enter the class name: ").capitalize()
    class_id = input("Enter the class ID: ").upper()
    number_of_student = int(input("Enter number of student for this class: "))

    # Check for duplication in class list
    if check_duplicate_in_list(class_name, class_list) or check_duplicate_in_list(class_id, class_list):
        print("Duplicate class, please try again!")

    new_class = {
        "Class name": class_name,
        "Class ID": class_id,
        "Number of student": number_of_student,
        "Current student": 0,
        "Mark list": []
    }
    class_list.append(new_class)
    class_list.sort()


def add_student_to_class(class_list):
    show_class(class_list)
    while True:
        student_class = input("Enter student's class (leave blank to set to None): ").upper().strip()

        # Check if the input is NULL then set the class to None
        student_class = None if check_null(student_class) else student_class
        if student_class is None:
            return student_class

        class_position = find_item_in_list(student_class, class_list)
        if class_position != -1:  # If class is found
            if is_class_full(class_list[class_position]):
                if input("The class is full, do you want to increase the class's student number? (Y/N)").upper() == 'Y':
                    class_list[class_position]["Current student"] += 1
                else:
                    input(f"Failed to add to {student_class}, please choose another class. Press Enter to continue.")

            class_list[class_position]["Current student"] += 1  # Increase the class's students
            return student_class
        else:
            user_choice = input("Class not found. Do you want to add new class? (Y/N)").upper().strip()
            if user_choice == 'Y':
                add_class(class_list)
            else:
                print("Student's class will be set to None")
                input("Press Enter to continue.")
                break
    return None


def add_table_mark(student_list, class_list):
    show_class(class_list)
    class_to_add = input("Enter a class to add mark: ")
    class_data = []
    for i in range(0, len(student_list)):
        if student_list[i]["Class ID"] == class_to_add:
            del student_list[i]["DOB"]
            class_data.append(student_list[i])
    for item in class_list:


# Functions for query information---------------------------------------------------------------------------------------
# Print all classes
def show_class(class_list):
    tab_width = 20
    print("Class name" + " " * (tab_width - 10) + "Class ID" + " " * 12 + "Number of student" + " " * 3 + "Current")
    for item in class_list:
        # If the class name smaller than tab_width, insert spaces to align the output
        # print(item[key] + " " * (tab_width - len(key)) + "|" + item[key])
        print(
            item["Class name"] + " " * (tab_width - len(item["Class name"])) +
            item["Class ID"] + " " * (tab_width - len(item["Class ID"])) +
            str(item["Number of student"]) + " " * (tab_width - len(str(item["Number of student"]))) +
            str(item["Current student"])
        )


# Function to print all student of the school
def show_all_student(student_list):
    tab_width = 20
    print("Student name" + " " * 8 + "Student ID" + " " * 10 + "Date of birth" + " " * 7 + "Class ID")
    for student in student_list:
        for item in student.keys():
            if len(item) < tab_width:
                print(student[item] + " " * (tab_width - len(student[item])), end="")  # Formatted output
            else:
                print(student[item], end="")
        print()


# Function to display all students in a class - work in progress
def show_students_class(student_list, class_list):
    tab_width = 20
    search = input("Enter the class name or class ID that you want to display data: ").upper().strip()
    print("Student name" + " " * 8 + "Student ID" + " " * 10)
    for item in student_list:
        if item["Class ID"] == search:
            print(item["Student name"] + " " * (tab_width - len(item["Student name"])) + item["Student ID"])


def show_mark(mark_list):
    for item in mark_list:
        print(f"{item["Student name"]} : {item["Mark"]}")


# Program starts here---------------------------------------------------------------------------------------------------
# Initialized program data
students = [
    {"Student name": "Pham Xuan Hoang", "Student ID": "22BI13175", "DOB": "12/03/2004", "Class ID": "MAT101"},
    {"Student name": "Someone", "Student ID": "22BIabcdef", "DOB": "123", "Class ID": "MAT101"}
]
# classes = [{"Math": "MAT101"}, {"Physics": "PHY101"}, {"Programming": "ICT101"}, {"French": "F101"}]  # Dummy data
classes = []
# Placeholder only -> reimplement later
while True:
    choice = input("Enter your choice: \n1. Enter student's information.\n2. Enter class's information\n")
    match choice:
        case "1":
            if len(classes) == 0:
                print("Class list empty, enter a class first. Please try again!")
                continue
            add_student(classes, students)
        case "2":
            add_class(classes)
        case "3":
            show_all_student(students)
        case "4":
            show_class(classes)
        case "5":
            show_students_class(students, classes)
        case "6":
            mark_table = add_table_mark(students, classes)
        case "exit":
            exit(0)
        case _:
            print("Wrong input, please try again!")
