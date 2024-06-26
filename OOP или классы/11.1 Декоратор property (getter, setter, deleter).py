
"""Getter (геттер)"""
# Метод класса, перед которым будет стоять декоратор @property называется геттером, от слова "get" - "получить".
# Getter - это метод, который возвращает значение защищённого или приватного атрибута.
# Но вызывается геттер как атрибут. Посмотрите на пример ниже:

class Person:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):            # метод стал свойством геттером
        return self.__name
person = Person("Vasya")
print(person.name)  # Vasya
# В примере, мы создали класс Person, который имеет приватный атрибут __name. Мы создали метод name и сделали его
# геттером, используя декоратор @property. Теперь мы можем обратиться к приватному атрибуту __name с помощью кода:
# print(person.name).
# Обратите внимание, что name без вызова, без скобок в person.name. Это потому что name здесь вызывается как атрибут
# за счёт декоратора. Вот почему property имеет такое название, потому метод создаёт иллюзию атрибута.

"""Setter (сеттер)"""
# Setter - это метод, который позволяет устанавливать значение атрибута, от слова "set" - "установить".
# Setter может быть определен, только если создан геттер. Setter создаётся с помощью декоратора в котором
# указывают имя геттера и слово setter через точку (@name.setter в примере).
# После декоратора объявляется метод, с тем же именем, что и у геттера (name в примере), важно чтобы имя было таким же.
# Метод принимает аргумент и изменяет значение атрибута на указанный нами аргумент (self.__name = name в примере).

class Person:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):            # геттер
        return self.__name
    @name.setter               # name - потому что, имя геттера - "name"
    def name(self, value):     # имя метода такое же как и у геттера - "name"
        self.__name = value
person = Person("John")
print(person.name) # John      # использовали геттер
person.name = "Vasya"          # использовали сеттер
print(person.name) # Vasya
# В примере, мы создали геттер, с помощью декоратора @property. Далее создаём сеттер, с помощью @name.setter
# и метода name, который имеет такое же имя, как и у геттера (это важно). Внутри сеттера мы изменяем атрибут
# __name на значение аргумента value.

# Обратите внимание, что в декораторе @name.setter, name - это имя метода геттера, и это важно.
# Слово setter после точки - говорит о том, что этот декоратор создаёт сеттер.
# Deleter (делитер)
# Deleter - это метод, который удаляет защищённый или приватный атрибут. Он похож по синтаксису на сеттер,
# отличается лишь словом deleter вместо setter, и тем что метод удаляет атрибут. Метод deleter может быть определен,
# только если создан геттер (это важно).

class Person:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):                   # имена методов одинаковые
        return self.__name.title()
    @name.deleter
    def name(self):                   # имена методов одинаковые
        del self.__name
person = Person("john")
print(person.__dict__) # {'_Person__name': 'john'}
del person.name        # использовали делитер
print(person.__dict__) # {}
# В этом примере мы создали класс Person, который имеет приватный атрибут __name. Мы определили getter и deleter
# для атрибута __name, используя декораторы @property и @name.deleter. Мы также использовали функцию del для
# удаления атрибута __name, хотя удаляли командой del person.name.

"""Заключение"""
# Сеттеры, геттеры и делиттеры созданы лишь для удобства работы с приватными атрибутами.
# Они выглядят как методы с декораторами, но на деле используют синтаксис обращения, как у атрибутов.
# Отсюда и их название - property (свойство, атрибут). С их помощью мы можем взаимодействовать с приватными атрибутами,
# не нарушая принципов инкапсуляции.
