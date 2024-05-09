""" Множественное наследование """
class Doctor:
    def __init__(self,rank):
        self.rank=rank
    def can(self):
        print('я доктор и я умею лечить')
class Builder:
    def __init__(self,degree):
        self.degree=degree
    def can(self):
        print('я строитель и я умею строить')
class Person(Doctor,Builder): # при множественном наследовании Родительские классы срабатывают слева на права
    def __init__(self,rank,degree): #  множественное наследование в __init__
        super().__init__(rank)  # сначала из первого родительского класса
        Builder.__init__(self,degree) # потом из второго родительского класса через вызов имя класса.инит(self,аттрибуты)
    def can(self):
        print('что я умею')
        super().can() # вызывается только из первого указанного родителя
        Builder.can(self) # для вызова из последующих нужно обращаться через сам класс Родителя
    def __str__(self):
        return f'я Person {self.rank} {self.degree}'
p1 = Person('спец',5)
p1.can() # я доктор и я умею лечить
print(Person.__mro__) # порядок разрешения методов в Python
print(p1)  # я Person спец 5





