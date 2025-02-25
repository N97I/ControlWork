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

