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
        print("Method")

class Student(Human):
    group = "7831"
    def __init__(self, height):
        self.height = height


class Teacher(Human):




hum = Human()
print(hum.get_height())
hum.set_height(10000000000000000)
print(hum.get_height())

buid = builder():
print(buid.group)
print(buid.group)

teac = teacher():
print(teac.height)
print(teac.group)