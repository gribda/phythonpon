class Cat:
    count = 0
    def __init__(self, name="No name", height=16):
        self.height = height
        self.name = name
        Cat.count += 1

    def __init__(self, name="No name", weight=6):
        self.weight = weight
        self.name = name
        Cat.count += 1
    def __str__(self):
        return f"Я кіт  {self.name}.\nМій зріст {self.height} см"
    def __str__(self):
        return f"Я кіт  {self.name}.\nМій Я важу {self.height} кг"
    def __del__(self):
        print("Я уходжу")





print(Cat.count)
cat = Cat("snejok", 21)
print(Cat)

#cat1 = cat(height=14)
#cat2 = cat(height=18)
#print(cat.height)
#print(cat1.height)
#print(cat2.height)
#print(cat2.count)