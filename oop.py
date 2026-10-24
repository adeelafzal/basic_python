class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def welcome():
        print("Welcome dear")

    def get_avg(self):
        total = sum(self.marks)
        totalSubjects = len(self.marks)
        avg = total/totalSubjects
        return avg


class Car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.start = True
        self.acc = True

    print("Car started...")


class Account:

    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance -= amount
        self.get_balance()

    def credit(self, amount):
        self.balance += amount
        self.get_balance()

    def get_balance(self):
        print("Your balance:", self.balance)


class Bank:

    def __init__(self, name, branch_code):
        self.name = name
        self.__code = branch_code

    def __welcome_bank(self):
        print("Welcome to", self.name)

    def get_branch(self):
        print("Branch code:", self.__code)
        self.__welcome_bank()


class Car:

    name = "Anonymus"

    @staticmethod
    def start(name):
        print("Start car", name)

    @staticmethod
    def stop():
        print("Stop car")


    @classmethod
    def do_something(cls, name):
        cls.name = name


class ToyotaCar(Car):

    def __init__(self, name):
        self.name = name
        super().__init__()


class ResultCard:

    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.che + self.math) / 3) + "%"



class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real,"i +", self.img, "j")


    def __add__(self, num2):
        newreal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newreal, newImg)
    

    def __sub__(self, num2):
        newreal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newreal, newImg)



class Circle:

    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius


class Employee:

    def __init__(self, role, dep, salary):
        self.role = role
        self.dep = dep
        self.salary = salary


    def show_details(self):
        print(self.role, self.dep, self.salary)


class Engineer(Employee):

    def __init__(self, name, age, role, dep, salary):
        self.name = name
        self.age = age
        super().__init__(role, dep, salary)


class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price


    def __gt__(self, other):
        return self.price > other.price


order1 = Order("Chips", 20)
order2 = Order("Burger", 10)

print(order1 > order2)