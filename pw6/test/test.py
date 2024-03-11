import pickle
from Courses import Courses
from Course import Course
from Students import Students
from Student import Student

courses = Courses()
course1 = Course("Math", "MAT101", 20)
course2 = Course("Physics", "PHY101", 30)
courses.add_course(course1)
courses.add_course(course2)

testP = pickle.dumps(courses)

testPLoad = pickle.loads(testP)

testPLoad.show_courses()

students = Students()
student1 = Student("test1", "id1", "1234")
student2 = Student("test2", "id2", "5678")
students.add_student(student1)
students.add_student(student2)

testS = pickle.dumps(students)
testSLoad = pickle.loads(testS)
testSLoad.show_all_student()
