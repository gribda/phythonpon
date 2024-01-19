import random
class human:

    def __init__(self, name, home=None, car=None):
        self.name = name
        self.money = 200
        self.enjoyment = 100
        self.home = home
        self.car = car

    def get_home(self, home):
        print()
        self.home = home

    def get_car(self, car):
        if car != None:
            print(f"Придбана автівка, марка {car.marka}")
        self.car = car
        print(f"Придбана автівка, марка {car.marka}")
    def work(self):

        print("Ідем працювати")
        money = random.randint(5, 20)
        print("Сьогодні заробили {}$")
        self.money += money

    def chill(self):
        print("Відпочиваємо")
        enjoymnet = random.randint(6, 8)
        print(f"Ви відпочили і почуваєтесь на всі {enjoyment} процентів!")

    def shopping(self):
        if self.car != None:
            print(f"Ідем за покупками")
        else:
            print(f"Їдемо на {self.car.marka} за покупками")

            print(f"я сьогодні був у магазині у мне залишок {self.money}")
            self.food = 1
            self.food = self.food

            self.money = 7
    def clean_house(self):
        if self.home != None:
            print(f"Ти не можешь прибратись")
        else:
            print("Пішли прибратись")
            self.home.cleanliness_level += 1
            self.enjoyment -= 3

    def life(self):
        r = random.randint(1, 4)
        if r == 1:
            self.work()
        elif r == 2:
            self.chill()
        elif r == 3:
            self.clean_house()
            

    def is_alive(self):
        if self .money <= 0 or self.home.food <= 0:
            return False
        return True

    def info(self):
        print("=============")
        print(f"Стан {self.name}:")
        print(f"Рівень задоволення - {self.enjoyment}")
        print(f"Залишок грошей - {self.money}")
        print(f"Наявність їжі - {self.home.food}")
        print(f"Порядок в кімнаті - {self.home.cleanliness_level}")


class Car:
    def __init__(self, marka):
        self.marka = marka
        self.passengers = []

    def add_passengers(self, *human):
        self.passengers.append(h)

    def passengers_info(self):
        print(f"Авто {self.marka}, ", end='')
        if self.passengers != []:
            print(f"Авто {self.marka}, зараз в в гараже:")
            for p in self.passengers:
                print(p.name)
        else:
            print("пасажири відсутні.")




class Home:
    def __init__(self):
        self.food = 0
        self.cleanliness_level = 50

human1 = human("Serq", car=Car("Mercedes-Benz GLA-Class"), home=Home())
day = 1
while(human.is_alive()):
    human.life()
    human.info()
    print(f"День {day}")
    day += 1

'''car = Car("Mercedes-Benz GLA-Class")
car.add_passengers(human1, human2, human3)
car.passengers_info()'''