# Магические методы сравнения
# __eq__ - отвечает за ==
# __ne__ - отвечает за !=
# __lt__ - отвечает за <
# __le__ - отвечает за <=
# __gt__ - отвечает за >
# __ge__ - отвечает за >=
# все методы не пишутся

""" Сравним прямоугольники """
class Rectangle: # прямоугольник
    def __init__(self,a,b):
        self.a = a  # высота
        self.b = b  # ширина

    @property
    def area(self): # свойство возвращает площадь переданного прямоугольника
        return self.a*self.b

    def __eq__(self, other):  # сравнение ДВУХ прямоугольников
        print('__eq__ call')
        if isinstance(other,Rectangle):  # если второй объект относиться к нашему классу
            return self.a == other.a and self.b == other.b # то мы сравниваем их стороны по отдельности


    def __lt__(self, other): # сравним площади прямоугольников
        print('__lt__ call')
        if isinstance(other,Rectangle):
            return self.area < other.area   # сравнение двух площадей
        elif isinstance(other,(int,float)):
            return self.area<other          # сравнение площади и переданного числа

    def __le__(self,other): # метод меньше или равно
        print('__le__ call')
        return self==other or self<other # первая часть запустит метод __eq__, а вторая - __lt__

a = Rectangle(1,2)
b = Rectangle(2,2)
c = Rectangle(2,1)
print(a==b) # False
print(a==c) # False
print(a<b) # True
print(a<5) # True
print(a>b) # False
print(c<=b) # True сначала запуститься __le__, потом __eq__ и __lt__
print(a!=c) # True __eq__
print(c>=b) # False __le__ - __eq__ - __lt__



