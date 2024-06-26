
# Метод __getattr__ предоставляет возможность определить поведение при обращении к несуществующим атрибутам объекта.
# Он позволяет программисту контролировать, что происходит при попытке доступа к неизвестным атрибутам и предоставлять
# альтернативное поведение или возвращать значение по умолчанию.
# Синтаксис
def __getattr__(self, item):
    pass
    # код, определяющий поведение при обращении к несуществующему атрибуту
# self - ссылка на сам объект.
# item - имя атрибута, к которому происходит обращение.


# Пример 1
# Определение поведения при обращении к несуществующему атрибуту:
class Person:
    def __getattr__(self, item):
        return f"Атрибут {item} не найден"
person = Person()
print(person.age)  # Вывод: Атрибут age не найден
# В примере мы обращаемся к атрибуту age и, так как его не существует, активируется метод __getattr__ ,
# который возвращает установленное нами сообщение "Атрибут age не найден".


# Пример 2
# Возвращение значения по умолчанию при обращении к несуществующему атрибуту:
class Person:
    def __getattr__(self, name):
        if name == "age":
            return 30
        else:
            return "Атрибут не найден"
person = Person()
print(person.age)   # Вывод: 30
print(person.name)  # Вывод: Атрибут не найден
# В примере мы объявили метод __getattr__ , который делает проверку и возвращает результат исходя из условия.
# Так как атрибута age не существует, активируется __getattr__ , который возвращает нам значение 30.
# Атрибута name тоже нет, активируется __getattr__ и он возвращает нам сообщение "Атрибут не найден".


# Пример 3
# Использование __getattr__ для доступа к словарю атрибутов:
class Person:
    def __init__(self):
        self.attributes = {"name": "John", "age": 30}
    def __getattr__(self, name):
        if name in self.attributes:
            return self.attributes[name]
        else:
            return "Атрибут не найден"
person = Person()
print(person.name)   # Вывод: John
print(person.age)    # Вывод: 30
print(person.height) # Вывод: Атрибут не найден
# С помощью __init__ мы создаём в экземплярах атрибут-словарь. При обращении к несуществующему атрибуту,
# с помощью __getattr__ мы делаем проверку, есть ли этот несуществующий атрибут в словаре (attributes) и
# возвращаем соответствующий результат.