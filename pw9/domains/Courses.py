from utilities import find_item_in_list, output_padding
import sys
sys.path.append("..")


class Courses:
    def __init__(self):
        self.__courses = []  # List of course object
        self.__number_of_course = 0

    def get_total(self) -> int:
        return self.__number_of_course

    def get_current(self) -> int:
        return len(self.__courses)

    def set_number_of_course(self, numberOfCourse) -> int:
        if numberOfCourse > self.__number_of_course:
            self.__number_of_course = numberOfCourse
            return 0
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
        headers = ["Course name", "Course ID", "Number of student", "Current"]
        widths = [9, 11, 3, 0]
        for header, width in zip(headers, widths):
            print(f"{header}{' ' * width}", end="")
        print()

        for course in self.__courses:
            print(
                f"{course.get_name()}{output_padding(course.get_name())}"
                f"{course.get_id()}{output_padding(course.get_id())}"
                f"{course.get_total()}{output_padding(course.get_total())}"
                f"{course.get_current()}"
            )
