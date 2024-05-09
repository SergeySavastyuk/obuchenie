""" При изменении одного аттрибута будут изменены и другие экземпляры(объекты) """

class Cat: # создадим приватный(__) словарь аттрибутов, которые будем навешивать всем экземплярам
    __shared_attr = {
        'breed':'pers',
        'color':'black'
    }
    def __init__(self): # запускаем init (срабатывает при оздании экземпляра)
        self.__dict__ = Cat.__shared_attr # приравниваем экземпляр.метод __dict__
        # (который показывает все аттрибуты объекта) к названию класса.его аттрибут (наш словарь)
a = Cat()
b = Cat()
print(a.__dict__) # {'breed': 'pers', 'color': 'black'}
b.breed = 'siam' # изменим один аттрибут в объекте
print(a.__dict__) # {'breed': 'siam', 'color': 'black'} видно что в другом объекте этот аттрибут тоже изменился
a.name = 'bob' # добавим новый аттрибут к экземпляру
print(b.__dict__) # {'breed': 'siam', 'color': 'black', 'name': 'bob'}








