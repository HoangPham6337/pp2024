from Student import Student
from Students import Students
import json

students = Students()
student1 = Student("Something1", "1233123", "12/03/2004")
student2 = Student("Something2", "5676507", "22/05/2004")
student3 = Student("Something3", "0983243", "31/12/2004")

students.add_student(student1)
students.add_student(student2)
students.add_student(student3)
with open("test.json", "r+") as fcc_file:
    student_dict = [students.get_student(i).to_dict() for i in range(len(students.get_student_list()))]
    json.dump(student_dict, fcc_file)

f = open("test.json", "r")
json_obj = json.load(f)
print(json.dumps(json_obj, indent=4))
f.close()

students_input = Students()
with open("test.json", "r") as input_file:
    students_data = json.load(input_file)
    for student_dict in students_data:
        student = Student(student_dict["name"], student_dict["id"], student_dict["dob"])
        students_input.add_student(student)
for student in students_input.get_student_list():
    print(student.__str__())
