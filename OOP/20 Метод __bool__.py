
''' Магический метод __bool__ Правдивость объектов в Python '''
''' если метода __bool__ нет, то питон смотрит в метод __len__ (если количество больше 0 то True), 
если и __len__ то все экземпляры будут правдивы '''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ call')
        return abs(self.x-self.y)

p1 = Point(4,9)
p2 = Point(2,2)
print(bool(p1)) # True
print(bool(p2)) # False т.к. x-y = 0
print('-'*50)

class Point2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __bool__(self):
        print('__bool__ call')
        return self.x !=0 or self.y !=0

p3 = Point2(0,0)
p4 = Point2(9,-5)
print(bool(p3)) #False
print(bool(p4)) #True



