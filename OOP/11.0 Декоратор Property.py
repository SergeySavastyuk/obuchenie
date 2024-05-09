""" Делаем декоратор Property, помещая внутрь методы класса, ставшие свойством """

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    # my_balance = property(my_balance) # наш метод получения значения через property() стал свойством класса (т.е декораторатом)
    @property
    def my_balance(self): # теперь это уже не метод, а свойство
        print('get_balance')
        return self.__balance
    # my_property_balance = my_balance # дабы не потерять свойство (которое выше), сохраним в другую переменную

    @my_balance.setter # таким образом вызываем наше свойство и у него вызываем метод setter
    def my_balance(self,value): # теперь это уже не метод с таким же именем, а свойство
                                # и теперь к этой функции нельзя будет обратиться извне
        if not isinstance(value,(int,float)):
            raise ValueError('balance должен быть числом')
        print(f"set_balance {value}")
        self.__balance = value

    @my_balance.deleter # с методом deleter то же самое
    def my_balance(self):
        print('del balance')
        del self.__balance

    # my_balance = my_property_balance.setter(my_balance) # перезапишем в свойство метод setter
    # с добавлением метода getter из переменной my_property_balance

a1 = BankAccount('Toli',500)
print(a1.my_balance)
a1.my_balance = 900
print(a1.my_balance)
print(a1.__dict__)
del a1.my_balance
print(a1.__dict__)
"""  в итоге мы получаем свойство my_balance хранящее в себе все наши функции(которое уже не функции 
и к которым уже не обратиться напрямую) getter, setter, delete """


