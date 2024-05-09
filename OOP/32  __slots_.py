""" Slots нужен для ограничения аттрибутов в экземпляре, по количеству и по имени. также уменьшает вес и увеличивает скорость"""
""" при наследовании Slots можно расширять новыми значениями """
""" и Slots убирает магический метод __dict__  """

class Rectangle:
    __slots__ = ('heigth','width')
    def __init__(self,x,y):
        self.width=x
        self.heigth = y
    @property
    def perimetr(self):
        return (self.heigth+self.width)*2
    @property
    def area(self):
        return self.heigth*self.width
a = Rectangle(10,5)
print(a.perimetr)

class Rectangle2:
    __slots__ = ('heigth','__width')
    def __init__(self,a,b):
        self.width=a
        self.heigth = b
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        print('setter call')
        self.__width = value
z = Rectangle2(10,5)
z = 60
print(z)

class Square(Rectangle2):
    __slots__ = ('color') # можно оставить пустой кортеж ()
    def __init__(self,a,b,color):
        super().__init__(a,b)
        self.color = color
c = Square(5,6,'red')
# print(c.__dict__) 'Square' object has no attribute '__dict__'