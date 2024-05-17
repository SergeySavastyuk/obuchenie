""" Замыкание (closure) — функция, которая находится внутри другой функции и ссылается на переменные объявленные
    в теле внешней функции (свободные переменные). """
""" Примеры """
def main_func():
    name = 'Ivan'
    def inner_func():
        print('hello my friend', name) # hello my friend Ivan
    return inner_func()
main_func()
print('-'*60)

def adder(value):
    def inner(a):
        return value+a
    return inner
a2 = adder(2) # двойка сохраняется в переменную value, что становится областью видимости
print(a2)     # <function adder.<locals>.inner at 0x00000000026D68B0>
print(a2(5))  # теперь при вызове а2 мы вызываем функцию inner
print(a2(57)) # 59
print('-'*60)

""" Счётчик """
def counter():
    count = 0  # переменная из области видимости функции counter()
    def inner(): # вложенная функция, которая считает
        nonlocal count # nonlocal позволяет изменить переменную из вышестоящей зоны видимости
        count+=1
        return count
    return inner
a3 = counter() # сохраним в переменную функцию inner
print(a3())  # 1 - теперь при вызове будет выводиться счётчик
print(a3())  # 2
print(a3())  # 3
print('-'*60)


""" Счётчик номер 2"""
def add(a,b):  # функция возведения в степень
    return a**b
def counter(funs):
    count = 0
    def inner(*args,**kwargs):  # счётчик с дополнительными параметрами для другой функции
        nonlocal count          # nonlocal позволяет изменить переменную из вышестоящей зоны видимости
        count +=1
        print(f"наша функция {funs.__name__} исполнилась {count} раз(а)")
        return funs(*args,**kwargs)
    return inner # запуск счётчика
a = counter(add)  # теперь функция add равна параметру funs
print(a(5,5)) # а эти аргументы станут параметрами функции inner
print('-'*60)


""" Счётчик номер 3"""
def multiply(x):
    count = x
    def inner(y):
        a = count*y
        return a
    return inner
a = multiply(5) # 5 сохраняем в х
print(a(6))     # 6 сохраняется в y
print('-'*60)


""" Счётчик номер 4"""
def average_numbers():
    numbers = []  # в пустой список будут добавляться все числа что будут передоваться в счётчик
    def inner(number):
        numbers.append(number)
        return sum(numbers)/len(numbers)
    return inner
a = average_numbers()
print(a(7))  # 7.0
print(a(25)) # 16.0
print('-'*60)


""" Счётчик номер 5 время"""
from datetime import datetime
print(datetime.now())  # время сейчас при старте кода 2024-05-17 20:44:01.645928
def time():
    start = datetime.now()
    def inner():
        return datetime.now()-start
    return inner
t = time()
print(t()) # 0:00:00
print('-'*60)


"""Несколько функций в замыкании"""
def create_counter():
    count = 0
    def increment(value: int = 1): # Функция, что прибавляет к счётчику
        nonlocal count
        count += value
        return count
    def decrement(value: int = 1): # Функция, что ОТНИМАЕТ от счётчика
        nonlocal count
        count -= value
        return count
    return increment, decrement
""" здесь не стоит забывать про порядок перечисления этих функций. В данном случае мы возвращаем сперва инкремент, 
    потом декремент. Поэтому и переменные названы соответствующим образом, в которые записывается результат вызова"""
inc_1, dec_1 = create_counter()  # обе функции получают область видимости функции create_counter
print(inc_1())  # увеличиваем на 1
print(inc_1(2))  # увеличиваем на 2
print(inc_1(3))  # увеличиваем на 3
print(dec_1())  # уменьшаем на 1
print(dec_1())  # уменьшаем на 1
print('-'*60)


""" Задача """
""" Функция должна сохранять в себе все значения, которые ей будут переданы причем в виде словаря. 
    Ключами данного словаря должны быть натуральные числа, равные номеру вызова данной функции """
def creat_dict():
    count = 0
    base = {}
    def inner(value):
        nonlocal count
        count+=1
        base[count]=value
        return base
    return inner
f = creat_dict()
print(f(150))   # {1: 150}
print(f('444')) # {1: 150, 2: '444'}
print(f('asd')) # {1: 150, 2: '444', 3: 'asd'}


