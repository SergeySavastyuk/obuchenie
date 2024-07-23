""" Property. getter-метод и setter-метод
методы позволяющие доставать и устанавливать значения приватных аттрибутов, а также свойство класса (Property)"""

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_balance(self): # метод возвращает значение приватного аттрибута
        return self.__balance

    def set_balance(self,value): # метод проставляет/обновляет значение в приватном аттрибуте
        if not isinstance(value,(int,float)): # сделаем проверку чтобы не прошли НЕ числа
            raise ValueError('balance должен быть числом')
        self.__balance = value

    def get_balance2(self): # метод возвращает значение приватного аттрибута
        return self.__balance

    def set_balance2(self,value): # метод проставляет значение в приватный аттрибут
        if not isinstance(value,(int,float)): # сделаем е проверку чтобы не прошли НЕ числа
            raise ValueError('balance должен быть числом')
        self.__balance = value

    def del_balance(self): # метод удаления аттрибута
        print('del balance')
        del self.__balance

    # внутри класса создадим свойство с именем balance
    # вызовем функцию property() которая вернёт экземпляр класса
    balance = property(fget=get_balance2,fset=set_balance2,fdel=del_balance)

a1 = BankAccount('vasya',950)
# print(a1.__balance) # напрямую к приватному аттрибуту мы не можем обратиться, получим ошибку
# AttributeError: 'BankAccount' object has no attribute '__balance'
print(a1.get_balance())  # но можем обратиться к методу из класса, который вернёт нужное значение, а именно 950
a1.set_balance(1050) # через другой метод установим новое значение приватному аттрибуту
print(a1.get_balance()) # и при повторном запросе получим 1050
a1.set_balance('123')
# print(a1.get_balance()) # ValueError: balance должен быть числом
print('_'*20)

""" методы получения и установки значений приватных аттрибутов можно использовать через свойство класса """
a1.balance = 113 # при такой записи будет срабатывать метод set_balance2
print(a1.balance) # при такой записи будет срабатывать метод get_balance2, который поместили в свойство класса

'''удалим приватный аттрибут '''
del a1.balance

""" и его можно заново создать """
a1.balance = 555
print(a1.balance) # 555

