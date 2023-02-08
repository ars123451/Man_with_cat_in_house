from random import randint

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 50

    def __str__(self):
        return f'My fullness - {self.fullness}'

    def work(self):
        cprint('I go to work', color="blue")
        self.house.money += 50
        self.fullness -= 10

    def sleep(self):
        cprint('I sleep', color='blue')
        self.fullness -= 20

    def shopping(self):
        if self.house.money > 50:
            cprint('I go shopping', color='blue')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('Not enough money!', color='red')

    def eat(self):
        if self.house.food > 10:
            cprint('I eat', color='blue')
            self.house.food -= 10
            self.fullness += 10
        else:
            cprint("Not enough food!", color='red')

    def go_to_the_house(self, house):
        self.house = house

    def act(self):
        if self.fullness <= 40:
            self.eat()
        elif self.house.food <= 40:
            self.shopping()
        elif self.house.money <= 50:
            self.work()
        else:
            solution = randint(1, 6)
            if solution == 1:
                self.eat()
            elif solution == 2:
                self.work()
            elif solution == 3:
                self.shopping()
            else:
                self.sleep()


class House:
    def __init__(self, money, food):
        self.money = money
        self.food = food
    def __str__(self):
        return f'Money = {self.money}, Food = {self.food}'


house_1 = House(70, 70)
man_1 = Man("Jack")
man_1.house = house_1
counter = 1
while counter <= 365:
    cprint(f'===========DAY {counter}==========', color='yellow')
    if man_1.fullness < 0:
        cprint('DEAD...', color='red')
        break
    else:
        man_1.act()
        counter += 1
        print(man_1)
        print(house_1)

# print(man_1)
# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
