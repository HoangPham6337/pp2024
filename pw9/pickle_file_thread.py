import threading
from pickle_file import pickle_file_wrapper, import_pickle_wrapper
class BackgroundPickleFile(threading.Thread):
    def __init__(self, courses, students, marks):
        threading.Thread.__init__(self)
        self.__courses = courses
        self.__students = students
        self.__marks = marks
    def run(self):
        pickle_file_wrapper(self.__courses, self.__students, self.__marks)
        # print("Finished exporting file")

class BackgroundImportPickleFile(threading.Thread):
    def __init__(self, courses, students, marks):
        threading.Thread.__init__(self)
        self.__courses = courses
        self.__students = students
        self.__marks = marks
    def run(self):
        self.__courses, self.__students, self.__marks = import_pickle_wrapper(self.__courses, self.__students, self.__marks)
    def return_result(self):
        return self.__courses, self.__students, self.__marks