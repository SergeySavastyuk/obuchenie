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


class Phone: # Родительский класс
    def __init__(self):  # Инициализатор
        self.is_on = False
    def turn_on(self):  # Включаем телефон
        self.is_on = True
    def call(self):  # Если телефон включен, делаем звонок
        if self.is_on:
            print('Making call...')
class MobilePhone(Phone):  # Унаследованный класс
    def __init__(self):  # Добавляем новое свойство battery
        super().__init__() # наследуем инициализатор родителя
        self.battery = 0
    def charge(self, num): # Заряжаем телефон на величину переданного значения
        self.battery = num
        print(f'Charging battery up to ... {self.battery}%')
my_mobile_phone = MobilePhone()
print(dir(my_mobile_phone))

# создаем класс Vehicle
class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")
# создаем класс Car, который наследует Vehicle
class Car(Vehicle):
    def car_method(self):
        print("Это дочерний метод из класса Car")
# создаем класс Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def cycleMethod(self):
        print("Это дочерний метод из класса Cycle")
car_a = Car()
car_a.vehicle_method()  # вызов метода родительского класса
car_b = Cycle()
car_b.vehicle_method()  # вызов метода родительского класса



class Camera:
    def camera_method(self):
        print("Это родительский метод из класса Camera")
class Radio:
    def radio_method(self):
        print("Это родительский метод из класса Radio")
class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")
cell_phone_a = CellPhone()
cell_phone_a.camera_method() # Это родительский метод из класса Camera
cell_phone_a.radio_method()  # Это родительский метод из класса Radio














