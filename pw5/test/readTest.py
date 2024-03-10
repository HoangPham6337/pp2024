import json
import tarfile
import os
if os.path.isfile("data/students.dat"):
    with tarfile.open("data/students.dat", "r:gz") as tar:
        tar.extractall(path="data/")
with open("data/courses.json", "r") as file:
    course_data = json.load(file)
    print(json.dumps(course_data, indent=4))

with open("data/students.json", "r") as file:
    course_data = json.load(file)
    print(json.dumps(course_data, indent=4))

with open("data/marks.json", "r") as file:
    course_data = json.load(file)
    print(json.dumps(course_data, indent=4))

