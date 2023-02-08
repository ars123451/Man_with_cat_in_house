from random import randint


class Man:
    def __init__(self):
        self.house = None
        self.fullness = 50
        self.no_money = 0

    def __str__(self):
        return f"Man's fullness = {self.fullness}"

    def work(self):
        print('I go to work')
        self.house.money += 100
        self.fullness -= 10

    def sleep(self):
        print('I sleep')
        self.fullness -= 20

    def shopping(self):
        if self.house.money > 50:
            print('I go shopping')
            self.house.money -= 50
            self.house.food += 50
        else:
            print('Not enough money!')
            self.no_money += 1

    def eat(self):
        if self.house.food > 10:
            print('I eat')
            self.house.food -= 10
            self.fullness += 10
        else:
            print("Not enough food!")

    def go_to_the_house(self, house):
        self.house = house

    def to_buy_cat_food(self):
        if self.house.money > 50:
            print("I buy cat food")
            self.house.cat_food += 50
            self.house.money -= 50
        else:
            print('Not enough money!')

    def clean_house(self):
        print("I clean house")
        self.house.dust -= 20
        self.fullness -= 20

    def act(self):
        if self.fullness <= 40:
            self.eat()
        elif self.house.food <= 40:
            self.shopping()
        elif self.house.money <= 50:
            self.work()
        elif self.house.cat_food < 30:
            self.to_buy_cat_food()
        elif self.house.dust > 15 and self.house.dust >= 0:
            self.clean_house()
        else:
            solution = randint(1, 7)
            if solution == 1:
                self.eat()
            elif solution == 2:
                self.work()
            elif solution == 3:
                self.shopping()
            elif solution == 4:
                self.clean_house()
            elif solution == 5:
                self.to_buy_cat_food()
            else:
                self.sleep()


class Cat:
    def __init__(self):
        self.house = None
        self.fullness = 50

    def __str__(self):
        return f"Cat's fullness = {self.fullness}"

    def sleep(self):
        print("I sleep")
        self.fullness -= 10

    def eat(self):
        if self.house.cat_food > 10:
            print("I eat")
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            print("Not enough food!")

    def play(self):
        print("I play")
        self.fullness -= 10
        self.house.dust += 3

    def go_home(self, house):
        self.house = house

    def act(self):
        if self.fullness < 20:
            self.eat()
        else:
            cat_solution = randint(1, 5)
            if cat_solution == 1:
                self.sleep()
            elif cat_solution == 2:
                self.eat()
            else:
                self.play()


class House:
    def __init__(self, money, food):
        self.money = money
        self.food = food
        self.cat_food = 0
        self.dust = 0

    def __str__(self):
        return f'Money = {self.money}, Food = {self.food}\nCat food = ' \
               f'{self.cat_food}, Dust = {self.dust}'


house_1 = House(70, 70)
man_1 = Man()
man_1.go_to_the_house(house_1)
cat_1 = Cat()
cat_1.go_home(house_1)
cat_2 = Cat()
cat_2.go_home(house_1)
counter = 1
while counter <= 10000:
    print(f'===========DAY {counter}==========')
    if man_1.fullness < 0:
        print('DEAD...')
        break
    elif cat_1.fullness < 0:
        print('DEAD...')
        break
    elif cat_1.fullness < 0:
        print('DEAD...')
        break

    else:
        print('Man: ')
        man_1.act()
        counter += 1
        print(man_1)
        print('\nCat 1:')
        cat_1.act()
        print(cat_1)
        print('\nCat 2:')
        cat_2.act()
        print(cat_2)
        print("\nHouse:")
        print(house_1)
        if man_1.no_money == 1:
            print('No money...')
            break
        elif house_1.dust >= 100:
            print('The house is too dirty!')
            break
        elif house_1.cat_food < 0:
            print('There is no food for cat!')
            break
        else:
            pass
