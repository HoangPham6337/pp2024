from .Course import Course
from utilities import find_item_in_list, output_padding
import sys
sys.path.append("..")


class Mark(Course):
    def __init__(self, name, id, ECTs):
        super().__init__(name, id, 0)
        self.__ECTs = ECTs
        self.__students = []  # Student mark object

    def __str__(self) -> str:
        return f"Course name: {self._Course__name}\nCourse ID: {self._Course__id}"

    def get_total(self):
        pass

    def set_total(self):
        pass

    def get_current(self):
        pass

    def get_students(self):
        return self.__students

    def get_ECTs(self) -> int:
        return self.__ECTs

    def is_full(self):
        pass

    def add_student(self, newStudent):
        self.__students.append(newStudent)

    def find_student(self, student) -> int:
        if len(self.__students) == 0:
            return -1
        position = find_item_in_list(student, self.__students, 1)
        position = (
            position
            if position != -1
            else find_item_in_list(student, self.__students, 1)
        )
        return position

    def get_student(self, studentPosition) -> object:
        return self.__students[studentPosition]

    def show_all_student(self):
        headers = ["Student name", "Student ID", "Mark"]
        widths = [8, 10, 16]
        for header, width in zip(headers, widths):
            print(f"{header}{' ' * width}", end="")
        print()

        for student in self.__students:
            print(
                f"{student.get_name()}{output_padding(student.get_name())}"
                f"{student.get_id()}{output_padding(student.get_id())}"
                f"{student.get_mark()}{output_padding(student.get_mark())}"
            )
