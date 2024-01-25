import random


class Human:

    def __init__(self, name, home=None):
        self.name = name
        self.hunger = 40
        self.joy = 70
        self.thirst = 60
        self.food = 100
        self.family_food_level = 0
        self.lake = None
        self.home = home

    def get_lake(self, lake):
        self.lake = lake

    def get_hunt(self):
        if self.home is not None:
            print(f"Идем охотиться за рыбой в {self.lake.fish}")
        self.food += 3
        print(f"Приобретено рыбы: 3 шт. У вас теперь {self.food} еды")

    def hunt(self):
        print("Идем охотиться")
        fish = random.randint(1, 6)
        print(f"Сегодня поймали рыбы: {fish}")
        self.food += fish

    def swim(self):
        print("Плаваем в озере")
        enjoyment = random.randint(3, 9)
        print(f"Вы поплавали, и ваш уровень удовольствия {enjoyment} процентов!")

    def drink(self):
        if self.thirst != None:
            print("Идем пить воду")
        else:
            print(f"Идем в воду {self.lake} за рыбкой")
            print(f"Сегодня попил, и у вас осталось {self.thirst} единиц жажды")

    def family(self):
        if self.family_food_level <= 0:
            print("У вас нет еды для семьи")
        else:
            print("Вы встретились со своей семьей")
            self.family_food_level -= 3
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
        if self.food <= 0:
            return False
        return True

    def info(self):
        print(f"Состояние {self.name}:")
        print(f"Уровень удовлетворения - {self.joy}")
        print(f"Наличие еды - {self.food}")
        print(f"Наличие воды - {self.thirst}")
        if self.home is not None:
            print(f"Семья - {self.home.family}")


class Home:
    def __init__(self, family=None):
        self.food = 0
        self.cleanliness_level = 50
        self.family = family


class Lake:
    def __init__(self, fish=None):
        self.fish = fish


class Family:
    def __init__(self, description):
        self.description = description


lake = Lake(fish="рыба в озере")
home = Home(family=Family("Семья счастлива"))
human = Human(name="Иван", home=home)

day = 1
while human.is_alive():
    human.life()
    human.info()
    print(f"День {day}")
    day += 1