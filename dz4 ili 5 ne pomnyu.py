class Human:
    height = 190
    _pole = 100
    group = "?????"
    def set_height(self, height):
        if height > 200:
            return
        self.__height = height
    def __method(self, height):
        if height > 200:
            return
        self.__height = height
    def get_height(self):
        self.__method()
        return self.__height

    def __method(self):
        (print"Method")

class Student(Human):
    group = "3019"
    def __init__(self, height):
        self.height = height


class archaeologist(Human):




h = Human()
print(h.get_height())
h.set_height(1000000)
print(h.get_height())

stud = Student()
print(stud.height)
print(stud.group)

ar = archaeologist()
print(ar.height)
print(ar.group)