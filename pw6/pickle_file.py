import pickle, os
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