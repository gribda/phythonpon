class Student:
    count = 0
    def __init__(self, name="No name", height=160):
        self.height = height
        self.name = name
        Student.count += 1

    def __str__(self):
        return f"Я студент  {self.name}.\nМій зріст {self.height} см"

    def __del__(self):
        print("Я ухожу")





print(Student.count)
student = Student("Vitalik", 170)
print(student)

#student1 = Student(height=170)
#student2 = Student(height=150)
#print(student.height)
#print(student1.height)
#print(student2.height)
#print(student2.count)