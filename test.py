# Utility functions-----------------------------------------------------------------------------------------------------
# Function to check duplication in a list, check both key and key's value


def check_duplicate_in_list(check_case, list_to_search):
    for item in list_to_search:
        for key in item.keys():
            if key == check_case:
                return True
            if item[key] == check_case:
                return True
    return False


def formatted_input(message, option):
    user_input = input(message).strip()
    if option == 1:
        user_input = user_input.upper()
    elif option == 2:
        user_input = user_input.title()
    elif option == 3:
        user_input = user_input.capitalize()
    return user_input


# Function for adding information---------------------------------------------------------------------------------------
def add_class(class_list):
    class_name = formatted_input("Enter the class name", 3)
    class_id = formatted_input("Enter the class ID: ", 1)
    number_of_student = int(input("Enter number of student for this class: "))

    # Check for duplication in class list
    if check_duplicate_in_list(class_name, class_list) or check_duplicate_in_list(class_id, class_list):
        print("Duplicate class, please try again!")

    new_class = {
        "Name": class_name,
        "ID": class_id,
        "Number of student": number_of_student,
        "Current student": 0,
        "Student list": [],
        "Mark list": []
    }
    class_list.append(new_class)


# Create a function to add student
def add_student(student_list, class_list):
    # Input student's data
    student_name = formatted_input("Enter your student's name: ", 2)  # Capitalize every first letter
    student_id = formatted_input(f"Enter {student_name} ID: ", 1)

    if check_duplicate_in_list(student_name, student_list) or check_duplicate_in_list(student_id, student_list):
        # Check for student duplication: name, id
        print("Duplicate student, please try again!")
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
    class_to_add = formatted_input("Enter the class ID to add: ", 1)
    for item in class_list:
        if item["ID"] == class_to_add:
            item["Student list"].append(student["ID"])
            return
    print("Class not found, class set to None")



print("Student mark management")
classes = []
students = []
add_class(classes)
add_student(students, classes)

