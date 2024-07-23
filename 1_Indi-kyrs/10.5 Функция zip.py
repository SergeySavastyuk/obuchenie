""" Функция zip """

"""# python >= 3.9

class zip(object)
 |  zip(*iterables, strict=False) --> Выводите кортежи до тех пор, пока не будут исчерпаны входные данные.
 |  
 |     >>> list(zip('abcdefg', range(3), range(4)))
 |     [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
 |  
 |  Объект zip выдает кортежи длиной n, где n - количество итераций,
 |  передаваемых в zip() в качестве позиционных аргументов. I-й элемент в каждом кортеже
 |  берется из i-го итерационного аргумента в zip(). Это продолжается до тех
 |  пор, пока не будет исчерпан самый короткий аргумент.
 |
 |  Если strict имеет значение true и один из аргументов исчерпан раньше остальных,
 |  возникает ошибка ValueError.
Если вы используете версии python <= 3.10, то в ней функция zip не поддерживает использование параметра strict. 
Он появился только начиная с версии 3.10, подробности в PEP 618"""

""" Функция zip должна принимать несколько итерабельных последовательностей и после чего возвращает zip объект. """
words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300, 400, 500]
result_zip = zip(words, numbers)
print(result_zip) # -> <zip object at 0x7f1dcb820b00>
print('-------')
print(list(result_zip)) # -> [('approach', 100), ('monstrous', 200), ('mobile', 300), ('voucher', 400), ('solid', 500)]
print(list(zip(range(5,11),range(5)))) # -> [(5, 0), (6, 1), (7, 2), (8, 3), (9, 4)]

""" Функция zip c одним аргументом """
a = [1,2,3]
print(list(zip(a))) # -> [(1,), (2,), (3,)]

""" Распаковка значений при обходе объекта zip """
words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300, 400, 500]
s = 'NaSA'
result_zip = zip(words, numbers, s)  # сначала сделаем список кортежей через zip
print(*result_zip) # -> ('approach', 100, 'N') ('monstrous', 200, 'a') ('mobile', 300, 'S') ('voucher', 400, 'A')

col1, col2, col3 = zip(*result_zip) # потом распакуем список обратно в три переменные
print(col1) # -> ('approach', 'monstrous', 'mobile', 'voucher')
print(col2) # -> (100, 200, 300, 400)
print(col3) # -> ('N', 'a', 'S', 'A')


""" Параметр strict """
"""Если у вас свежая версия питона (от 3.10), вы можете воспользоваться параметром strict. 
Он позволяет вызывать исключение в случае, если у одной из последовательностей элементы закончатся раньше чем у других. 
Или другими словами, параметр strict будет следить за соблюдением равенства длин переданных последовательностей. 
Если длина различается, получается ValueError.
Тут важно понимать, что исключение ValueError вы получите не сразу при запуске кода, а в момент обхода коллекций. 
Как только заканчиваются элементы одной из коллекций, при условии наличия значений в других, вы получите ValueError."""


"""Если не хотите отбрасывать элементы, можете воспользоваться zip_longest из модуля itertools . 
В zip_longest можно передать аргумент  fillvalue, который помогает заполнить недостающие значения. 
Если не передать значения будут заполняться None"""
from itertools import zip_longest
ids = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
countries = ('Australia', 'USA')
records = zip_longest(ids, leaders, countries)
print(list(records)) # -> [(1, 'Elon Mask', 'Australia'), (2, 'Tim Cook', 'USA'), (3, 'Bill Gates', None), (4, 'Yang Zhou', None)]
records_2 = zip_longest(ids, leaders, countries, fillvalue='Unknown')
print(list(records_2)) # -> [(1, 'Elon Mask', 'Australia'), (2, 'Tim Cook', 'USA'), (3, 'Bill Gates', 'Unknown'), (4, 'Yang Zhou', 'Unknown')]

# Можно обходить и словари при помощи zip:
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)
# name -> John
# name -> Jane
# last_name -> Doe
# last_name -> Doe
# job -> Python Consultant
# job -> Community Manager

"""Создание словарей при помощи двух коллекций. Значения первой коллекции будут помещаться в качестве ключа новой пары, 
а значением будут выступать элементы из второй коллекции. Также можно и обновлять пары существующего словаря"""
employee_numbers = [2, 9, 18]
employee_names = ["Valentin", "Leonti", "Andrew"]
numbers = dict(zip(employee_numbers, employee_names))
employees = dict(zip(employee_names, employee_numbers))
print(numbers) # -> {2: 'Valentin', 9: 'Leonti', 18: 'Andrew'}
print('------')
print(employees) # -> {'Valentin': 2, 'Leonti': 9, 'Andrew': 18}
# обновляе словаря
other_num = [50, 63]
other_names = ['Misha', 'Sergey']
numbers.update(zip(other_num, other_names))
print('------')
print(numbers) # -> {2: 'Valentin', 9: 'Leonti', 18: 'Andrew', 50: 'Misha', 63: 'Sergey'}


"""Транспонирование матрицы
Транспонирование матрицы - это процесс изменения ориентации матрицы путем перестановки строк и столбцов, 
так что строки становятся столбцами, а столбцы - строками."""
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
matrix_trans = [list(i) for i in zip(*matrix)]
print(matrix_trans) # -> [[1, 5], [2, 6], [3, 7], [4, 8]]
# В этом примере из матрицы размером 2х4 получили матрицу размером 4х2.


# Напишите определение функции zip_with_function
def zip_with_function(l: list, fuc):
    return [fuc(*i) for i in zip(*l)]
# прочие функции выполняющее действия
def combine_strings(a: str, b: str) -> str:
    return a + b
def get_sum_two_numbers(a: int, b: int) -> int:
    return a + b
def get_sum_three_numbers(a: int, b: int, c: int) -> int:
    return a + b + c
'проверочные коды:'
assert zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers) == [4, 7, 12]
assert zip_with_function([[10, 20], [30, 0]], get_sum_two_numbers) == [40, 20]
assert zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers) == [10, 15, 20]
assert zip_with_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]], get_sum_three_numbers) == [12, 15, 18]
assert zip_with_function([["a", "b"], ["1", "2"]], combine_strings) == ['a1', 'b2']