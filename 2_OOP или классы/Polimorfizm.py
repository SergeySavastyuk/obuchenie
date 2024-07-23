''' Полиморфизм - это возможность обработки разных объектов одним методом'''
'''возможность использовать один и тот же метод для экземпляров из разных классов. 
Когда говорят один и тот же метод, имеют в виду методы с одинаковым именем.'''

class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'это прямоугольник {self.x}х{self.y}'

    def get_area(self):
        return self.x*self.y

class Square:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return f'это квадрат {self.x}х{self.x}'

    def get_area(self):
        return self.x**2

class Circle:
    def __init__(self,r):
        self.r = r

    def __str__(self):
        return f'это круг, радиус {self.r}, площадью {self.r**2*3.14}'

    def get_area(self):
        return self.r**2*3.14

a = Rectangle(5,8)
b = Square(6)
c = Circle(5)
print(a) # это прямоугольник 5х8
print(b) # это квадрат 6х6
print(c) # это круг, радиус 5, площадью 78.5

