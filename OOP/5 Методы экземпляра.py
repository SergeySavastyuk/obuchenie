""" Функция как аттрибут класса """
class Car:
    models = ['BMW', 'AUDI', 'TOYOTA']
    @staticmethod  # этот декоратор позволяет вызывать функцию через экземпляр класса
    def drive():  # функция является аттрибутом этого класса
        print("Let's go")
Car.drive()  # для вызова функции из класса, нужно написать сам класс.название функции с вызовом, это ()
getattr(Car, 'drive')()  # другой способ вызова
F = Car()
F.drive()  # Let's go


""" Методы экземпляра """
class Cat():
    def hello(self):  # Функция стала методом т.к. её можно вызвать только через экземпляр класса
        # (также как методы типа a.sort() )
        print('Hello Cat')
bob = Cat()  # создадим экземпляр
bob.hello()  # здесь bob передаётся в аргументы функции hello()


class Cat():
    breed = 'pers'
    def show_breed(instanse):  # здесь в переменную instanse мы передаём walt,
        # у которого есть классовый аттрибут со значением pers
        print(f'my breed is {instanse.breed}')
walt = Cat()
walt.show_breed()  # my breed is pers
walt.breed = 'siam' # siam стал аттрибутом экземпляра
walt.show_breed()  # my breed is siam
bob = Cat()  # новый экземпляр
bob.show_breed()  # my breed is pers


""" если вызываемого аттрибута нет """
class Cat():
    def show_name(self):
        if hasattr(self,'name'): # метод hasattr() позволяет проверить есть ли у экземпляра (self) атрибут ('name')
            print(f'my name {self.name}')
        else:
            print('Nothing')
mary = Cat()
mary.name = 'MARY' # здесь у класса нет такого аттрибута, но он есть у экземпляра, поэтому вызов метода работает
mary.show_name() # my name MARY
bob = Cat()
bob.show_name() # Nothing


""" метод установки аттрибута """
class Cat():
    def set_value(koshka,value, AGE = 10): # в метод мы передаём экземпляр класса и значение
        koshka.name = value # после у этого экземпляра создаём аттрибут и привязываем переданное значение
        koshka.age = AGE
mari = Cat()
mari.set_value('tom') # создадим аттрибут экземпляра со значением через метод
print(mari.name) # вызвав атрибут name у экземпляра mari получим tom(который ранее передали)
jerry = Cat()
jerry.set_value('JERRY')
print(jerry.age) # 10
jerry.set_value('JERRY',30)
print(jerry.age) # 30









