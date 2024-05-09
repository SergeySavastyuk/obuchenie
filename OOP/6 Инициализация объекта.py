""" Магические методы или методы начинающиеся на __"""

class Cat():
    def __init__(self,name,age = 25): # метод __init__ будет срабатывать ВСЕГОДА при создании экземпляра этого класса,
        # а в self будет сохраняться экземпляр. Данный метод используется для заполнения аттрибутов экземпляра
        self.name = name
        self.age = age
        print(f'Hello объект {self}, твоё имя - {name} и возраст {age}')
tom = Cat('Tom') # создадим экземпляр и в обязательном порядке нужно указать его аттрибуты т.к. это требует __init__
print(tom.__dict__) # {'name': 'Tom', 'age': 25}
mari = Cat('mari',40)
print(mari.__dict__) #{'name': 'mari', 'age': 40}


# Практика. Класс Point(x,y)
class Point:
    def __init__(self,coord_x = 0,coord_y = 0):
        self.x = coord_x
        self.y = coord_y
    def move_to(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
    def go_home(self):
        self.x = 0
        self.y = 0

p1 = Point(3,4)
p2 = Point(-2,-10)
p3 = Point()
p3.move_to(5,4)

# изменим методы класса, чтобы убрать дублирующие строчки
# в  __init__ также можно вызывать другой метод через self
class Point:
    list_point = [] # создадим аттрибут класса
    def __init__(self,coord_x = 0,coord_y = 0):
        self.move_to(coord_x,coord_y)
        Point.list_point.append(self) # и через __init__ и методы класса и списка будем добавлять все новые точки в список
    def move_to(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
    def go_home(self):
        self.move_to(0,0)
    # создадим метод для более красивого вывода экземпляра, а не  <__main__.Point object at 0x00000000027A53A0>
    def print_point(self):
        return f"точка с координатами ({self.x},{self.y})"
    # напишем метод, который будет работать с несколькими экземплярами
    def calc_dist(self,another_point): # обязательным аргументом должна быть другая точка
        if not isinstance(another_point,Point): # делаем проверку, если аргумент НЕ принадлежит классу Point
            raise ValueError("аргумент не принадлежит классу") # То возбудим исключение с передачей сообщения
        y=(self.x - another_point.x)**2+(self.y - another_point.y)**2 # расстояние найдём через теорему Пифагора
        return y**0.5

p4 = Point(10,-5)
print(p4.__dict__) # {'x': 10, 'y': -5}
p5 = Point(5)
print(p5.__dict__) # {'x': 5, 'y': 0}
p5.move_to(-5,6)
print(p5.__dict__) # {'x': -5, 'y': 6}
p5.go_home()
print(p5.__dict__) # {'x': 0, 'y': 0}
p5.move_to(-3,7)
print(p5) # <__main__.Point object at 0x00000000027A5670>
print(p5.print_point()) # точка с координатами (-3,7)
print(p4.__dict__) # {'x': 10, 'y': -5}
print(f'расстояние между точками p4 и p5 равно {p4.calc_dist(p5)}')
print(Point.list_point) # [<__main__.Point object at 0x00000000027856A0>, <__main__.Point object at 0x0000000002785640>]

