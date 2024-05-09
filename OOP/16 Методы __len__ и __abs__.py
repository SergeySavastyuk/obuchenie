
""" Магические методы __len__ и __abs__ """

class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __len__(self): # Магические методы __len__ позволяет применить len и к числам тоже
        return len(self.name+self.number)

a = Person('bob','25')
print(len(a)) # 5

class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __abs__(self): # тоже как и abs
        return abs(self.x1-self.x2)

b = Otrezok(5,-10)
print(abs(b)) # 15
