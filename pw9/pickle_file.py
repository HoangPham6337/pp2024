import pickle, os
import tarfile
from domains import (
    Courses,
    Students,
    Students,
    Marks,
)

def create_dir():
    if not os.path.exists("data_pickle"):
        os.makedirs("data_pickle")

def pickle_courses(courseList):
    with open("data_pickle/courses", "wb") as courses_file:
        pickle.dump(courseList, courses_file)
    
def pickle_students(studentList):
    with open("data_pickle/students", "wb") as students_file:
        pickle.dump(studentList, students_file)

def pickle_marks(markList):
    with open("data_pickle/marks", "wb") as mark_file:
        pickle.dump(markList, mark_file)

def compress_data():
    with tarfile.open("data_pickle/students.dat", "w:gz") as f_out:
        for file in ["data_pickle/courses", "data_pickle/students", "data_pickle/marks"]:
            f_out.add(file, arcname=os.path.basename(file))
    for file in ["data_pickle/courses", "data_pickle/students", "data_pickle/marks"]:
        os.remove(file)

def extract_data():
    if os.path.isfile("data_pickle/students.dat"):
        with tarfile.open("data_pickle/students.dat", "r:gz") as tar:
            tar.extractall(path="data_pickle/")

def pickle_load_courses(courses) -> Courses:
    if os.path.isfile("data_pickle/courses"):
        with open("data_pickle/courses", "rb") as courses_file:
            newCourse = pickle.load(courses_file)
            return newCourse
    return courses

def pickle_load_students(students) -> Students:
    if os.path.isfile("data_pickle/students"):
        with open("data_pickle/students", "rb") as students_file:
            newStudents = pickle.load(students_file)
            return newStudents
    return students

def pickle_load_marks(marks) -> Marks:
    if os.path.isfile("data_pickle/marks"):
        with open("data_pickle/marks", "rb") as marks_file:
            newMarks = pickle.load(marks_file)
            return newMarks
    return marks

def pickle_file_wrapper(courses, students, marks):
    """Automatically extract all objects data using pickle"""
    pickle_courses(courses)
    pickle_students(students)
    pickle_marks(marks)

def import_pickle_wrapper(courses, students, marks):
    """Automatically decompress data, import objects data and serialize them"""
    create_dir()
    extract_data()
    return pickle_load_courses(courses), pickle_load_students(students), pickle_load_marks(marks)