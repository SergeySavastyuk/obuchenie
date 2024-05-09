
""" Практика с Property. Property нужно, чтобы отловить постороннее обращение к атрибуту и установку неверных данных"""

from string import digits  # импортируем из модуля строки только цифры

class User:
    def __init__(self, login, password):
        self.login = login
        # self.__password = password при таком коде наш пароль сначала сохраняем в базу, а потом уже идёт проверка,
        # но нам надо наоборот, поэтому вместо переменной пишем наше свойство
        self.password = password  # !!!! важный момент, при запуске мы полученное значение сохраняем в свойство,
        # таким образом, сначала пройдёт проверка, а потом уже сохранение
        self.__secret = 'Вход разрешён'

    @property
    def secret(self): # создадим свойство проверки пароля на входе с сохранённым
        if self.__password == input('Введите ваш пароль: '):
            return self.__secret
        raise ValueError('Пароль не верен')

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod  # чтобы функция не становилась методом класса - вешается декоратор  @staticmethod,
    # он позволяет вызывать функцию не только через класс, но и через экземпляр
    def is_include_number(password):
        return bool([i for i in password if i in digits])

    @password.setter  # обработка присвоения этому аттрибуту значения
    def password(self, value):  # функция содержит проверки для пароля
        if not isinstance(value, str):  # если пароль не строка
            raise TypeError('Пароль должен быть строкой')
        if len(value) <= 4:
            raise ValueError('Длинна пароля должна быть больше четырёх символов')
        if len(value) >= 12:
            raise ValueError('Длинна пароля должна быть меньше двенадцати символов')
        if not User.is_include_number(value):  # если функция вернёт False
            raise ValueError('В пароле должны быть цифры')
        print('setter called')
        self.__password = value


# a1 = User('bob',1233) # такой объект не пройдет т.к. пароль не пройдёт проверку
a2 = User('bob', 'aasda123')
print(a2.secret)

