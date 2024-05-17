""" Декоратор – функция, которая принимает одну функцию и возвращает другую функцию.
    Они нужны для того, чтобы функции добавилось новое поведение. """
def decor(func):
    def inner():
        print("start")     # start
        func()             # Hi world
        print("The end")   # The end
    return inner
def say():
    print("Hi world")
a = decor(say) # функция say сохраняется в параметр func, а в перемнную А сохраняется функция inner
print(a)       # <function decor.<locals>.inner at 0x00000000026D68B0> - подтверждает что А это ф-ия inner
a()  #  запустим её
print('1'*60)


""" декоратор c аргументом """
def decor(func):
    def inner(*args): # добавим в сам декоратор аргументы
        print("start")                                          # start
        func(*args) # и передадим их нашей главной функции        Hi world and Vasiliy Petrovjch
        print("The end")                                        # The end
    return inner
def say(name,surname):
    print(F"Hi world and {name} {surname}")
say = decor(say)
say('Vasiliy','Petrovjch')
print('2'*60)


""" несколько декораторов на одну функцию """
def decor(func):
    def inner(*args):
        print("<h1>")
        func(*args)
        print("</h1>")
    return inner
def table (func):
    def inner(*args):
        print("<table>")
        func(*args)
        print("</table>")
    return inner
def say(name,surname, age):
    print(F"Hi world and {name} {surname} {age} years")
say = table(decor(say)) # сначала выполнится фун-ия decor, а потом table
say('Vasiliy','Petrovjch',33)
# первой вызывается функция decor() и она возвращает функцию inner, результатом которой будут
# строки h1, Hi world…, /h1 и этот результат будет передаваться внутрь функции table и получим данный результат.
# <table>
# <h1>
# Hi world and Vasiliy Petrovjch 33 years
# </h1>
# </table>
print('3'*60)


""" Декораторы «навешивают» при помощи @ следующим образом: """
# вызов функции деократора без лишних слов, достаточно собачки @,
# после чего запускается указанный декоратор и нижестоящая основная функция
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner
@header        # say = header(say)
def say(name, surname, age):
    print('hello', name, surname, age)
say('Vasya', 'Ivanov', 30)

# или если их больше
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner
def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner
# say = header(table(say))
@header
@table
def say(name, surname, age):
    print('hello', name, surname, age)
say('Vasya', 'Ivanov', 30)
print('4'*60)


""" декоратор через лямбду """
text_decor = lambda x: lambda *args: (print('Hello'), x(*args), print('Good buy'))[1] # код декоратора
"""Без [1] декорированная функция вернёт не результат функции а, кортеж (null, результат функции, null). 
Так что если нет проверки того что возвращает функция всё будет работать. И если функция должна возвращать что-то, 
например число 2, и данное число используется в каких- то вычислениях, то после добавления такого декоратора без [1], 
вычисления будут давать ошибку, так как например нельзя из кортежа (null, 2, null) вычесть 1"""
@text_decor  # запуск декоратора
def multiply(num1, num2):
    print(num1 * num2)
multiply(3, 5) # основаная функция сохраняется в Х, а аргумента 3,5 сохраняются в args
print('5'*60)


'''этот декоратор возвращает удвоенное значение основной функции'''
double_it = lambda fun: lambda *args: fun(*args)*2
@double_it
def multiply(num1, num2):
    return num1 * num2
assert multiply(9, 4) == 72 # это проверка
print(multiply(9, 4)) # 72
print('6'*60)


""" для того чтобы не потерялась имя и строка документации декорированной функции используют декоратор wraps"""
from functools import wraps
def add_args(funs):
    # Навешиваем декоратор wraps на вложенную функцию inner и передаём ему исходную (главную) функцию, которая декорируется
    @wraps(funs)
    def inner(*args):
        return funs('start',*args,'the end') # параметр funs равен ', '.join(args)
    return inner
@add_args  # декоратор
def concatenate(*args): # главная функция
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)
print(concatenate('world', 'my')) # -> start, world, my, the end
print(add_args.__doc__) # None - документация на ф-ию add_args
print(concatenate.__doc__) # Возвращает конкатенацию переданных строк - документация на ф-ию concatenate
print('7'*60)


"""нужен декоратор который валидирует (проверяет на корректность) переданные аргументы"""
from functools import wraps
def validate_args(funs):
    @wraps(funs)
    def inner(*args):
        if len(args)>2:
            return 'Too many arguments'
        elif len(args)<2:
            return 'Not enough arguments'
        else:
            if type(args[0])== int and type(args[1]) == int:
                return funs(*args)
            else:
                return 'Wrong types'
    return inner
# Код ниже не удаляйте, он нужен для проверки
@validate_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y
assert add_numbers(4, 5) == 9
assert add_numbers(4) == 'Not enough arguments'
assert add_numbers('hello') == 'Not enough arguments'
assert add_numbers(3, 5, 6) == 'Too many arguments'
assert add_numbers('a', 'b', 'c') == 'Too many arguments'
assert add_numbers(4.5, 5.1) == 'Wrong types'
assert add_numbers('hello', 4) == 'Wrong types'
print('8'*60)


"""Мемоизация — это метод сохранения результатов ресурсоемких вызовов функций и возврата ранее вычисленного 
(кэшированного) результата при повторении одних и тех же входных данных. Это может значительно повысить 
производительность рекурсивных функций, которые в противном случае могут привести к многократному 
выполнению одних и тех же вычислений."""

"""Декоратор-запоминатор"""
"""декоратор становиться кешем, где храниться инфа"""
from functools import wraps
def memoize(func):
    cache = {} # создадим словарь, где будем хранить кеш
    @wraps(func)
    def inner(n):
        if n not in cache: # если переданного аргумента нет в словаре
            cache[n] = func(n) # то мы создаём ключ с этим аргументом и приравниваем его к функции фибоначи с этм аргументом
        return cache[n]  # после чего вернём значение из словаря по изначальному аргументу
    return inner
@memoize
def fibonacci(n):
    """ Возвращает n-ое число Фибоначчи """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
assert fibonacci(50) == 12586269025
assert fibonacci(100) == 354224848179261915075