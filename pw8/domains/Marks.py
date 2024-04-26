from .Courses import Courses
from utilities import output_padding
import numpy as np
import sys
sys.path.append("..")


class Marks(Courses):
    def __init__(self):
        super().__init__()

    def add_course(self, newCourse):
        self._Courses__courses.append(newCourse)

    def get_total(self):
        pass

    # def get_current(self):
    #     pass

    def set_number_of_course(self, numberOfCourse):
        pass

    def is_full(self):
        pass

    def check_empty(self):
        pass

    def show_courses(self):
        pass

    def calculate_GPA(self, student, omitOutput) -> int:
        listMarks, totalECTs = [], 0

        if not omitOutput:
            headers = ["Course name", "Course ID", "ECTs", "Mark"]
            widths = [9, 11, 16, 0]
            for header, width in zip(headers, widths):
                print(f"{header}{' ' * width}", end="")
            print()

        for mark in self._Courses__courses:
            studentPosition = mark.find_student(student)
            if studentPosition != -1:
                studentData = mark.get_student(studentPosition)
                studentMark = studentData.get_mark()
                listMarks.append(studentMark * mark.get_ECTs())
                totalECTs += mark.get_ECTs()

            if not omitOutput:
                print(
                    f"{mark.get_name()}{output_padding(mark.get_name())}"
                    f"{mark.get_id()}{output_padding(mark.get_id())}"
                    f"{mark.get_ECTs()}{output_padding(mark.get_ECTs())}"
                    f"{studentMark if studentPosition != -1 else 'No info'}"
                )

        gpaArray = np.array(listMarks, dtype=int)
        return gpaArray.sum() / totalECTs
