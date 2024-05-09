# __delattr__ -  позволяет определить поведение при удалении атрибута объекта. Он вызывается каждый раз,
# когда происходит попытка удалить атрибут объекта. Метод __delattr__ может быть использован для определения
# дополнительных действий или запрета удаления определенных атрибутов. В __delattr__ также нужно использовать
# функцию super() для удаления объекта.

# Синтаксис
def __delattr__(self, name):
    super().__delattr__(name) # удаление атрибута name
# self - ссылка на сам объект
# name - имя атрибута


# Пример 1
# Определение дополнительных действий при удалении атрибута:
class Person:
    def __delattr__(self, name):
        print(f"Атрибут {name} удален")
        super().__delattr__(name)
person = Person()
person.name = "Vasya"
del person.name  # Атрибут name удален
# В примере, мы объявляем метод __delattr__, который выводит на экран текст и удаляет объект при помощи команды:
# super().__delattr__(name) . В момент удаления объекта класса, мы получаем сообщение "Атрибут name удален".


# Пример 2
# Запрет удаления атрибутов объекта:
class Immutable:
    def __delattr__(self, name):
        raise AttributeError(f"Запрещено удалять атрибут {name}")
immutable_obj = Immutable()
immutable_obj.age = 18
del immutable_obj.age  # AttributeError: Запрещено удалять атрибут age
# В примере, метод __delattr__ не производит удаление объекта, потому что нет команды super().__delattr__(name).
# Вместо этого мы вызываем исключение AttributeError и сообщение об ошибке.

# Назначение
# Определение дополнительных действий при удалении атрибута.
# Запрет удаления определенных атрибутов объекта.

# Пример 3 удаление из __init__
class Number:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.s = a+b
        del self.s
    def __delattr__(self, name):
        if self.s<10:
            super().__delattr__(name)
# код проверки:
number1 = Number(4, 5)
print('s' in number1.__dict__) # False
number2 = Number(6, 11)
print('s' in number2.__dict__) # True