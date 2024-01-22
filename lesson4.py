class Human:
    height = 170
    _pole = 100
    group = "?????"
    def set_height(self, height):
        if height > 210:
            return
        self.__height = height
    def __method(self, height):
        if height > 210:
            return
        self.__height = height
    def get_height(self):
        self.__method()
        return self.__height

    def __method(self):
        (print"Method")

class Student(Human):
    group = "7831"
    def __init__(self, height):
        self.height = height


class Teacher(Human):




h = Human()
print(h.get_height())
h.set_height(10000000000000000)
print(h.get_height())

stud = Student()
print(stud.height)
print(stud.group)

t = teacher()
print(t.height)
print(t.group)
