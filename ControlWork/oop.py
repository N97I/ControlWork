# class Person:
#
#     def __init__(self, age):
#         self.age = age
#
#
#     def set_age(self, age):
#         if isinstance(age, int) and age > 0:
#             self.age = age
#         else:
#             print(f'Ошибка: Возраст должен быть положительным')
#
#     def get_age(self,):
#         return self.age
#
# p = Person(18)
# p.set_age(27)
# print(p.get_age())
# p.set_age(-5)


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


