""" Публичные аттрибуты - это аттрибуты которые доступны внутри класса и вне класса"""
class BankAccount:
    def __init__(self,name,balance,passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self):
        print(self.name,self.balance,self.passport)
a1 = BankAccount('Bob', 100000,35416163874644)
""" получим аттрибуты из внутренней функции класса """
a1.print_public_data() # Bob 100000 35416163874644
""" получим аттрибуты запросив из вне класса """
print(a1.name) # Bob
print(a1.balance) # 100000
print(a1.passport) # 35416163874644
print('_'*50)

""" Защищённые аттрибуты (_)- это аттрибуты, которые используются на уровне согласования между разработчиками 
и желательно его использовать только из класса"""
class BankAccount2:
    def __init__(self,name,balance,passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_protected_data(self):
        print(self._name,self._balance,self._passport)
a2 = BankAccount2('Bob', 100000,35416163874644)
""" получим аттрибуты из внутренней функции класса """
a2.print_protected_data() # Bob 100000 35416163874644
""" получим аттрибуты запросив из вне класса """
print(a2._name) # Bob
print(a2._balance) # 100000
print(a2._passport) # 35416163874644
print('_'*50)

""" Приватные аттрибуты (__)- атрибуты, доступ к котором можно получить только изнутри класса"""
class BankAccount3:
    def __init__(self,name,balance,passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        print(self.__name,self.__balance,self.__passport)
    """приватная защита доступна и методам, которые можно вызвать через другой метод"""
    def __private(self):
        print(self.__name, self.__balance, self.__passport)
    def public(self):
        self.__private()

a3 = BankAccount3('Bob', 100000,35416163874644)
""" получим аттрибуты через метод изнутри класса (т.н. инкапсуляция - сокрытие обработки приватных аттрибутов) т.е. 
мы предоставляем пользователю метод(доступ) по работе с данными, какой именно доступ определяем программист """
a3.print_private_data() # Bob 100000 35416163874644

""" Попробуем получить аттрибут запросив извне класса """
print(a3.__name) # AttributeError: 'BankAccount3' object has no attribute '__name'
a3.__private # AttributeError: 'BankAccount3' object has no attribute '__private'

""" вызов приватного метода через другой метод класса """
a3.public() # Bob 100000 35416163874644

""" но можно получить аттрибуты извне через класс, а именно нужно указать объект_название класса__приватный аттрибут или метод """
print(a3._BankAccount3__name) # Bob
a3._BankAccount3__private()   # Bob 100000 35416163874644







