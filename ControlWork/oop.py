class Person:

    def __init__(self, age):
        self.age = age


    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.age = age
        else:
            print(f'Ошибка: Возраст должен быть положительным')

    def get_age(self,):
        return self.age

p = Person(18)
p.set_age(27)
print(p.get_age())
p.set_age(-5)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self,):
        return f'I am an animal'

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self,):
        return f'Woof'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self,):
        return f'Meow'


dog = Dog('Buddy')
cat = Cat('Kitty')

print(dog.name, dog.speak())
print(cat.name, cat.speak())


class Vehicle:
    def __init__(self,vehicle):
        self.vehicle = vehicle

    def move(self):
        return f'Vehicle is moving'

class Car(Vehicle):
    def __init__(self, vehicle='Car'):
        super().__init__(vehicle)

    def move(self):
        return f'Car is driving'

class Bicycle(Vehicle):
    def __init__(self, vehicle='Bike'):
        super().__init__(vehicle)

    def move(self):
        return f'Bicycle is pedaling'

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))

from abc import ABC,abstractclassmethod
import math
class Shape(ABC):

    @abstractclassmethod
    def area(self):
        """метод реализован"""
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self,):
        return f'Прямоугольник {self.width}x{self.height}'

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)



rect1 = Rectangle(10,5)
circle = Circle(7)

print(rect1.area())
print(round(circle.area(),2))






