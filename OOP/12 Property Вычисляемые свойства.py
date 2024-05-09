
""" Вычисляемые Property """

class Square:
    def __init__(self,s):
        self.side = s
        self.__area = None  # переменная для сохранения результата из свойства

    def area(self):  # метод класса
        return self.side**2

    @property
    def area2(self):  # СВОЙСТВО класса
        return self.side ** 2

    """ вычисляемое свойство класса вычисляется каждый раз при вызове свойства, дабы этого не делать можно первый 
    результат сохранить в переменную и потом выдавать уже её, тем самым экономя ресурс"""

    @property
    def area3(self):
        if self.__area == None:
            self.__area = self.side**2
            print('None было заменено')
        return self.__area

a1 = Square(6)
print(a1.area()) # здесь вызываем метод area
a1 = Square(10)
# print(a1.area2) # здесь вызываем свойство area2
print('_'*50)
a2 = Square(13)
print(a2.__dict__)
print(a2.area3)
a2.side = 5  # Здесь ошибка т.к. мы сохраняем 5 и должны получить 25
print(a2.__dict__)
print(a2.area3) # а получаем 169, т.к. None больше нет, значит нужно сделать возврат None для этого
print('_'*50)

class Square2:
    def __init__(self,s):
        self.__side = s  # переменную делаем приватной
        self.__area = None

    @property
    def side(self):  # используя Property делаем свойство с методом get и сохраняем в первую переменную первое число
        return self.__side

    @side.setter # и свойство с методом set, который установит новое значение в первую переменную и обнулит вторую
    def side(self,value):
        self.__side = value
        self.__area = None

    @property  # сделаем метод подсчёта свойством, чтобы вызывать через имя свойства без кавычек  ()
    def area4(self):
        if self.__area == None:
            self.__area = self.side**2
            print('None было заменено')
        return self.__area

a3 = Square2(5)
print(a3.__dict__)
print(a3.area4) # 25
print(a3.side) # 5  тут срабатывает свойство side с get
a3.side = 6    #  тут уже срабатывает свойство side с методом set
print(a3.area4) # 36
print('*'*50)

"""  ДЗ написать вычитаемое свойство периметр """
class Perimeter:
    def __init__(self,quantity_sides = 1,*args):
        self.__args = args   # длинна сторон
        self.__quantity_sides = quantity_sides # количество одинаковых сторон
        self.__result = None # результат сложения

    @property
    def sides(self):
        return self.__args,self.__quantity_sides

    @sides.setter
    def sides(self,args):
        self.__args = args
        self.__result = None

    @property
    def sum(self):
        if self.__result == None:
            self.__result = sum(self.__args)*self.__quantity_sides
        return self.__result

b1 = Perimeter(2,4,3)
print(b1.__dict__)
print(b1.sides)
b1.sides = 1,4,
print(b1.__dict__)
print(b1.sides)
print(b1.sum) # 10
b1.sides = 6,3
print(b1.sum) # 18
b2 = Perimeter(3,5)
print(b2.sum) # 15
