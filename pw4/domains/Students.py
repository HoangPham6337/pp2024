from utilities import find_item_in_list, output_padding
import sys
sys.path.append("..")


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

    def get_student_list(self) -> list:
        return self.__students

    def check_empty(self) -> bool:
        return len(self.__students) == 0

    def show_all_student(self):
        print(f"Total number of student: {len(self.__students)}")
        headers = ["Student name", "Student ID", "Date of birth"]
        widths = [8, 10, 7]
        for header, width in zip(headers, widths):
            print(f"{header}{' ' * width}", end="")
        print()

        for student in self.__students:
            print(
                f"{student.get_name()}{output_padding(student.get_name())}"
                f"{student.get_id()}{output_padding(student.get_id())}"
                f"{student.get_dob()}"
            )
