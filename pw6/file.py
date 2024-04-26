from genericpath import isfile
import json
import tarfile
import os

from domains import Courses, Course, Student, Students, Marks, Mark, StudentMark

def export_courses(courseList):
    with open("data/courses.json", "w") as coursesFile:
        courseDict = []
        courseMax = {"courseMax": courseList.get_total()}
        courseDict.append(courseMax)
        courseDict.append([courseList.get_course(i).to_dict() for i in range(courseList.get_current())])
        json.dump(courseDict, coursesFile)

def export_students(studentList):
    with open("data/students.json", "w") as studentsFile:
        studentDict = [studentList.get_student(i).to_dict() for i in range(len(studentList.get_student_list()))]
        json.dump(studentDict, studentsFile)

def export_marks(markList):
    with open("data/marks.json", "w") as marksFile:
        markDict = []
        markList = [markList.get_course(i) for i in range(markList.get_current())]
        for mark in markList:
            result = []
            result.append({
                "name": mark.get_name(),
                "id": mark.get_id(),
                "ECTs": mark.get_ECTs()
                })
            studentList = mark.get_students()
            studentDict = [studentList[i].to_dict() for i in range(len(studentList))]
            result.append(studentDict)
            markDict.append(result)
        json.dump(markDict, marksFile)

def compress_data(courseList, studentList, markList):
    with tarfile.open("data/students.dat", "w:gz") as f_out:
        for json_file in ["data/courses.json", "data/students.json", "data/marks.json"]:
            f_out.add(json_file, arcname=os.path.basename(json_file))
    for json_file in ["data/courses.json", "data/students.json", "data/marks.json"]:
        os.remove(json_file)

def extract_data() -> int:
    if os.path.isfile("data/students.dat"):
        with tarfile.open("data/students.dat", "r:gz") as tar:
            tar.extractall(path="data/")
        return 1
    return 0

def import_courses(courseList) -> int:
    if os.path.isfile("data/courses.json"):
        with open("data/courses.json", "r") as input_courses:
            coursesData = json.load(input_courses)
            maxCourse = coursesData[0]
            courseList.set_number_of_course(maxCourse["courseMax"])
            for courseDict in coursesData[1]:
                newCourse = Course(name=courseDict["name"], id=courseDict["id"], total=courseDict["total"])
                newCourse.set_current(courseDict["current"])
                for studentID in courseDict["studentsID"]:
                    newCourse.add_student_from_file(studentID)
                courseList.add_course(newCourse)
        return 1
    return 0

def import_students(studentsList) -> int:
    if os.path.isfile("data/students.json"):
        with open("data/students.json", "r") as input_students:
            studentsData = json.load(input_students)
            for studentDict in studentsData:
                newStudent = Student(name=studentDict["name"], id=studentDict["id"], dob=studentDict["dob"])
                newStudent.set_GPA(studentDict["GPA"])
                studentsList.add_student(newStudent)
        return 1
    return 0

def import_marks(marksList) -> int:
    if os.path.isfile("data/marks.json"):
        with open("data/marks.json", "r") as input_marks:
            marksData = json.load(input_marks)
            for course in marksData:
                courseInfo = course[0]
                newMark = Mark(name=courseInfo["name"], id=courseInfo["id"], ECTs=courseInfo["ECTs"])
                studentsMark = course[1]
                for student in studentsMark:
                    newStudent = StudentMark(name=student["name"], id=student["id"], dob=student["dob"])
                    newStudent.set_mark(student["mark"])
                    newMark.add_student(newStudent)
                marksList.add_course(newMark)
        return 1
    return 0

def import_data(courseList, studentList, markList):
    if extract_data() == 1:
        result_1 = import_courses(courseList)
        result_2 = import_students(studentList)
        result_3 = import_marks(markList)
        if result_1 == 1 and result_2 == 1 and result_3 == 1:
            return
        else:
            print("Data is corrupted, please delete the folder data/ and try again!")