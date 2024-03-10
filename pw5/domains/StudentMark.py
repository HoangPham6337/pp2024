from .Student import Student


class StudentMark(Student):
    def __init__(self, name, id, dob):
        super().__init__(name, id, dob)
        self.__mark = 0

    def get_mark(self) -> int:
        return self.__mark

    def set_mark(self, mark) -> int:
        if mark < 0:
            print("Invalid input, please try again!")
            return -1
        else:
            self.__mark = mark
            return 0
    
    def to_dict(self):
        return {
            "name": self.get_name(),
            "id": self.get_id(),
            "dob": self.get_dob(),
            "mark": self.__mark
        }
