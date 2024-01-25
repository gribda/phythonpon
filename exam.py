import random


class duck:

    def __init__(self, name, home=None, eat=None):
        self.name = name
        self.hunger = 40
        self.joy = 70
        self.thirst = 60
        self.hunt = hunt
        self.lake = lake
    def get_lake(self, lake):
        print()
        self.lake = lake

    def get_hunt(self, hunt):
        if car != None:
            print(f" по полював за рибою {lake.fish}")
        self.fish = fish
        print(f"Придбана риба 3 шт. {lake.fish}")

    def hunt(self):

        print("Ідем полювати")
        fish = random.randint(1, 6)
        print("Сьогодні заробили риби {}")
        self.fish += fish

    def swim(self):
        print("Плаваємо в озері")
        enjoymnet = random.randint(3, 9)
        print(f"Ви поплавили і ваш рівень задоволення {joy} процентів!")

    def thirst(self):
        if self.thirst != None:
            print(f"йдемо Пити воду")
        else:
            print(f"Ідемо в воду {self.car.marka} за рибкою")

            print(f"я сьогодні попив і в мене осталося {self.fish}")
            self.thirst = 2
            self.thirst = self.thirst

            self.thirst = 5

    def family(self):
        if self.family != None:
            print(f"тобі ні з ким зустрічаються")
        else:
            print("ти зустрів сім'ю")
            self.family_food_level += 3
            self.joy -= 9

    def life(self):
        r = random.randint(1, 6)
        if r == 1:
            self.hunt()
        elif r == 2:
            self.swim()
        elif r == 3:
            self.family()

    def is_alive(self):
        if self.fish <= 0 or self.food <= 0:
            return False
        return True

    def info(self):
        print(f"Стан {self.name}:")
        print(f"Рівень задоволення - {self.joy}")
        print(f"Наявність їжі - {self.fish}")
        print(f"Наявність води - {self.thirst}")
        print(f"Родина - {self.family}")


class Home:
    def __init__(self):
        self.food = 0
        self.cleanliness_level = 50


duck = duck("Utka", family=Family("Family has nice life"), lake=Lake())
day = 1
while (duck.is_alive()):
    duck.life()
    duck.info()
    print(f"День {day}")
    day += 1
