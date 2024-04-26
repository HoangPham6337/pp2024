class Student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__GPA = 0

    def __str__(self) -> str:
        return (
            f"Student name: {self.__name}\nStudent ID: {self.__id}\nDOB: {self.__dob}"
        )

    def __eq__(self, otherStudent) -> bool:
        if not isinstance(otherStudent, Student):
            return NotImplemented
        else:
            return self.__GPA == otherStudent.get_GPA()

    def __lt__(self, otherStudent) -> bool:
        if not isinstance(otherStudent, Student):
            return NotImplemented
        else:
            return self.__GPA < otherStudent.get_GPA()

    def to_dict(self):
        return {
            "name": self.__name,
            "id": self.__id,
            "dob": self.__dob,
            "GPA": self.__GPA
        }

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_dob(self) -> str:
        return self.__dob

    def set_GPA(self, GPA):
        self.__GPA = GPA

    def get_GPA(self) -> str:
        return self.__GPA
