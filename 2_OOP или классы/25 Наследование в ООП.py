""" Наследование в объектно-ориентированном программировании """

class Person:  # класс, который будет наследоваться
    def can_walk(self):
        print('я могу ходить')

class Doctor(Person):  # добавляем наслудуемый класс, и теперь все методы, аттрибуты и прочее будет доступно для наследника
    def can_cure(self):
        print('Я могу лечить')

class Architector(Person):
    def can_build(self):
        print('Я могу строить')

a = Doctor()
b = Architector()
a.can_cure()
a.can_walk()
print()
b.can_build()
b.can_walk()
print()
print(issubclass(Doctor,Person)) # issubclass метод для проверки является ли класс подклассом другого класса
print(issubclass(Person,Doctor)) # False
print(isinstance(b,Architector)) # True
print(isinstance(b,Person)) # True











