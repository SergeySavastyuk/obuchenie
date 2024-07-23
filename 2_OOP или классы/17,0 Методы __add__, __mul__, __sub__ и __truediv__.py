""" Магические методы математические операции __add__(+), __mul__(*), __sub__(-) и __truediv__(/) """

class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __add__(self, other): # метод складывает аттрибут объекта с переданным значением и может вызываться без указания метода
        print('__add__ call')
        if isinstance(other,Person): # если данные принадлежат нашему классу (то есть мы пробуем сложить двух человек)
            return self.number+other.number # складываем данные двух человек

        if isinstance(other,(int,float)):
            return self.number+other

        if isinstance(other, str):  # для строк
            return self.name+other

    def __radd__(self, other): # метод складывает число с аттрибутом объекта
        print('__radd__ call')
        return self + other # вызовем метод __add__

    def __mul__(self, other):
        if isinstance(other,Person):
            return self.number*other.number

        if isinstance(other,(int,float)):
            return self.number*other

        if isinstance(other, str):  # для строк
            return self.name+other



a = Person('tat',600)
print('     вызовы по старинке ')
print(a.number+300) # 900
print(a.__add__(700)) # 1300
print(a.__add__('sos')) # tatsos
print("     !!!! метод не указывали   !!!")
print(a+500) # 1100 (питон к первому объекту пытается вызвать метод __add__, а второй объект добавляется,
# если первый объект - число, а второй - то куда надо прибавить, то будет срабатывать метод __radd__  )
print(a+'tot') # tattot
b = Person('vasa',1000)
print(' складываем двух человек ')
print(a+b)
print(b+a)
print(' тут сработал по умолчанию метод __radd__ ')
print(12+b) # 1012
print(' метод __mul__')
print(b*3) # 3000
print(b*'123') # vasa123
print(a*b) # 600000
print("-"*50)

""" метод сохранения нового баланса в новом объекте """
class Person2:
    def __init__(self, name, balance):
        print(" новый объект ")
        self.name = name
        self.balance = balance

    def __repr__(self):  # для красивого вывода срабатывает при запуске команды print
        return f'человек {self.name} с номером {self.balance}'

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other,Person2):
            return self.balance+other.balance

        if isinstance(other,(int,float)):
            return Person2(self.name,self.balance+other)

t = Person2('Tola',600)
print(t) # тут срабатывает магический метод  __repr__ при запуске команды print
print(id(t)) # 43835744
print(t+100) # создаётся новый объект
y = t+100
print(y, id(y))  # 43704960
print(t+y) # 1300










