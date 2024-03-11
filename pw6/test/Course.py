from utilities import (
    find_in_list,
    output_padding
)
from input import (
    get_input_as_int,
    get_input_as_string
)
import sys
sys.path.append("..")


class Course:
    def __init__(self, name, id, total):
        self.__name = name
        self.__id = id
        self.__total = total
        self.__current = 0
        self.__studentsID = []  # Student ID only, not object

    def __str__(self) -> str:
        returnString = f"Course name {self.__name}\n"
        returnString += f"Course Id: {self.__id}\n"
        returnString += f"Total student: {self.__total}\n"
        returnString += f"Current number of student: {self.__current}"
        return returnString

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_total(self) -> int:
        return self.__total

    def set_total(self, newTotal):
        if newTotal > self.__total:
            self.__total = newTotal
        else:
            print(
                "Invalid input, please enter a number greater than the current total."
            )

    def get_current(self) -> int:
        return self.__current

    def set_current(self, current):
        self.__current = current

    def is_full(self) -> bool:
        return self.__current >= self.__total

    def add_student(self, newStudentID) -> int:
        if self.is_full():
            if (
                get_input_as_string(
                    "The course is full. Do you want to add more student? (Y/N) "
                ).upper() == "Y"
            ):
                self.set_total(
                    get_input_as_int(
                        f"Current maximum: {self.get_total()}. Enter the new value: "
                    )
                )
            else:
                input("Failed to add student to course, please try again!")
                return -1

        if find_in_list(newStudentID, self.__studentsID) == -1:
            self.__current += 1
            self.__studentsID.append(newStudentID)
            return 0
        else:
            print("Duplicate student.")
            return -1

    def add_student_from_file(self, newStudentID):
        self.__studentsID.append(newStudentID)

    def check_duplicate_student(self, newStudentID):
        return find_in_list(newStudentID, self.__studentsID) != -1

    def show_all_student(self, studentList):
        headers = ["Student name", "Student ID", "Date of birth"]
        widths = [8, 10, 7]
        for header, width in zip(headers, widths):
            print(f"{header}{' ' * width}", end="")
        print()

        for student_id in self.__studentsID:
            student_position = studentList.find_student(student_id)
            student = studentList.get_student(student_position)
            print(
                f"{student.get_name()}{output_padding(student.get_name())}"
                f"{student.get_id()}{output_padding(student.get_id())}"
                f"{student.get_dob()}"
            )

    def to_dict(self):
        return {
            "name": self.__name,
            "id": self.__id,
            "total": self.__total,
            "current": self.__current,
            "studentsID": self.__studentsID
        }
