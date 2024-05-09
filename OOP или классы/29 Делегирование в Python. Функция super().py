""" Наследование Делегирование Delegating (используется для удаления дублей кода)
или как вызвать метод из родительского класса в дочернем классе super().метод родителя(аргументы если есть)"""
'''Функция super() позволяет использовать функциональность родительского класса в дочернем классе, 
а также обеспечивает более гибкую и удобную работу с наследованием. 
Использование super() помогает избежать дублирования кода и делает программу более читаемой и поддерживаемой.'''

class Person:
    def __init__(self,name,surname):
        self.name =name
        self.surname = surname

    def __str__(self):
        return f'Человек {self.name} {self.surname}'

    def info(self):
        print('Родительский класс')
        print(self)

class Doctor(Person): # Дочерний класс
    def __init__(self,name,surname,age):
        super().__init__(name,surname) # важна последовательность, сначала вызовется родительский метод,
        # передаст значения, а потом уже дочерний - сохранит значения в третий аттрибут
        self.age = age

    def __str__(self):
        return f'Доктор  {self.name} {self.surname} {self.age}'

a = Person('bob','abroms')
b = Doctor('Nika','Lana',32)
print(a) # Человек bob abroms
print(b) # Доктор  Nika Lana 32
print('-'*20)
b.info() # ->Родительский класс -> Доктор  Nika Lana 32
















