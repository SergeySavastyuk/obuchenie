"""Сегодня научимся писать функции, которые могут возвращать по одному значению,
при этом «замораживая» своё выполнение, и при новом вызове функции она будет выполняться с того места,
на котором она остановилась. Такая функция называется функцией генератором."""

# обычная функция
def func() -> list:
   return [1, 2, 3]
print(func()) # [1, 2, 3]
print(func()) # [1, 2, 3]

# функция-генератор
def gen_func():
    for i in [1, 2, 3]:
        yield i
f = gen_func()
print(f) # <generator object gen_func at 0x0000023CA5AF0510>
print(next(f)) # 1
print(next(f)) # 2
# Таким образом, наша функция генератор всегда запоминает какой элемент она возвращала при помощи инструкции yield
# и какой элемент нужно вернуть следующим.


""" Пример использования функции генератора """
# Разберем простую функцию get_factorial, которая по натуральному числу n определяет его факториал
def get_factorial(n: int) -> int:
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr
# При вызове функции
print(get_factorial(10))
# мы сразу увидим конечный результат 10! = 3628800. Если нам необходимо получить помимо конечного значения факториала
# числа n еще и все промежуточные факториалы, мы можем завести список и складывать в него внутри цикла for текущие
# значения переменной pr.
def get_factorial(n: int) -> list:
    pr = 1
    a = []
    for i in range(1, n + 1):
        pr *= i
        a.append(pr)
    return a
print(get_factorial(10)) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
# Минусом такой функции является то, что она требует выделения памяти для хранения всех этих значений: чем больше
# число n, тем больше размер списка нужно создавать для хранения результата вычисления.

"""Функция генератор поможет избавиться от необходимости хранения всех промежуточных значений в списке."""
def get_factorial(n: int) -> int:
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr
fact_10 = get_factorial(10)
print(next(fact_10)) # 1
print(next(fact_10)) # 2
print(next(fact_10)) # 6
print(next(fact_10)) # 24

"""В переменной pr при первом вызове next сохранится факториал единицы и далее значение вернутся из функции генератора, 
а значения переменных pr и i заморозятся. При втором вызове next() мы перейдем к следующему обходу цикла for и получим 
факториал двойки. После каждого следующего значения мы будем получать текущий факториал числа.
Чтобы не вызывать каждый раз функцию next проще будет обходить все значения функции генератора при помощи цикла for:"""
def get_factorial(n: int) -> int:
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr
for f in get_factorial(10):
    print(f, end=' ') # 1 2 6 24 120 720 5040 40320 362880 3628800


"""  Аннотация функции генератора   """
# Generator[yield_type, send_type, return_type]
""" yield_type - тип значения, который будет возвращаться из генератора по средствам ключевого слова yield 
    send_type - тип значения, который будет приниматься в функцию генератор
    return_type тип значения, который возвращается в конце функции генератора через оператор return"""
from typing import Generator
def echo_round() -> Generator[int, float, str]:
    res = yield
    while res:
        res = yield round(res)
    return 'OK'
# Если ваша функция-генератор ничего не возвращает и не принимает, то аннотация должна выглядеть следующим образом:
from typing import Generator
def infinite_sequence() -> Generator[int, None, None]:
    num = 0
    while True:
        yield num
        num += 1

""" примеры """
"""  Генератор квадратов  """
def gen_squares(n):
    for i in range(1,n+1):
        yield i**2
for i in gen_squares(3):
    print(i)

"""  Генератор последовательности Фибоначчи  """
def gen_fibonacci_numbers(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
for i in gen_fibonacci_numbers(5):
    print(i)

"""  Копия range  """
def my_range_gen(*args):
    if len(args) == 1:
        start = args[0]
        count = 0
        while count < start:
            yield count
            count += 1
    elif len(args) == 2:
        start, stop = args[0], args[1]
        while start < stop:
            yield start
            start += 1
    else:
        start, stop, step = args[0], args[1], args[2]
        if start < stop and step > 0:
            while start < stop:
                yield start
                start += step
        elif start > stop and step < 0:
            while start > stop:
                yield start
                start += step
for i in my_range_gen(8, 5, -1):
    print(i)

