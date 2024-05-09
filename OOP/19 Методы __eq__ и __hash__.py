""" Магические методы __eq__ и __hash__ Dunder methods в Python"""

# __hash__ преобразует объект(только у не изменяемых) в число в одну сторону, обратно не идёт.
# Используется в ключах словаря

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(2, 5)
b = Point(6, 10)
print(a.__repr__())  # <__main__.Point object at 0x0000000002995610>
print(a == b)  # False  по умолчанию сравнение идёт по айди
print(a.__hash__())  # 2737505 или другое число
print('_' * 50)


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """ после переопределения у класса  метода __eq__ то у него слетает метод __hash__ 
    чтобы он снова заработал то его нужно определить"""

    def __eq__(self, other):  # если не выполниться одна из трёх проверок - то объекты не равны
        return isinstance(other, Point2) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))  # Вернём хеширование кортежа, т.к. списки это изменяемый объект и не хешируется

d = Point2(2, 5)
e = Point2(6, 10)
print(d==e) # False
print(a.__hash__()) # 2725217
print('поместим хеш-число как ключ в словарь')
f = {}
f[d]=100
print(d) # <__main__.Point2 object at 0x00000000029DE1F0>
print(f) #  {<__main__.Point2 object at 0x00000000029CE1F0>: 100}