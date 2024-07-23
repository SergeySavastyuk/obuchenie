''' Полиморфизм - это возможность обработки разных объектов одним методом'''


from Polimorfizm import Rectangle,Square,Circle

rect1 = Rectangle(5, 10)
rect2 = Rectangle(2, 16)
sq1 = Square(7)
sq2 = Square(13)
cirl1 = Circle(5)
cirl2 = Circle(9)

figures = [rect1,rect2,sq1,sq2,cirl1,cirl2] # список разных объектов, каждый требует своего метода обработки
for figure in figures: # Поэтому мы используем Полиморфизм т.е. название метода одно для всех, но действия разные
    print(figure,figure.get_area()) # когда питон получает объект, то он идёт в класс этого объекта, находит этот метод и запускает


