# Синтаксис
# По умолчанию __getattribute__ выглядит так:

def __getattribute__(self, item):
    return object.__getattribute__(self, item)  # возвращает значение атрибута
# self - это экземпляр класса, для которого вызывается метод.
# item - это имя атрибута, к которому происходит обращение.


# Пример 1. Дополнительное поведение
class User:
    name1 = 'Vasya'
    name2 = 'Masha'
    def __getattribute__(self, item):
        return f'Привет {object.__getattribute__(self, item)}'
user = User()
print(user.name1) # Привет Vasya
print(user.name2) # Привет Masha
# Команда object.__getattribute__(self, item) возвращает значение атрибута.
# Но мы изменили поведение и добавили слово 'Привет'.
# И при каждом вызове атрибута через точку, мы будем получать слово "Привет", а потом значение атрибута.


# Пример 2. Контроль доступа к атрибутам объекта
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __getattribute__(self, item):
        if item == 'password':
            raise AttributeError("Доступ к паролю запрещён")
        return object.__getattribute__(self, item)
user = User("Vasya", "secret")
print(user.username)  # Vasya
print(user.password)  # AttributeError: Доступ к паролю запрещён
# В примере мы создаём атрибуты username и password с помощью __init__.
# Затем создали метод __getattribute__ , который выполняет проверку.
# И если через точку будет вызываться атрибут password, то будет выбрасываться исключение,
# запрещая доступ к этому атрибуту. Своего рода защита данных.