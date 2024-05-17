""""""
""" Встроенная функция isinstance """
""" Функция isinstance позволяет проверить к какому типу объектов относится ваше значение."""

a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
sum_list = []
for i in a:
    if isinstance(i, list):
       sum_list = sum_list + i
print(sum_list) # -> [3, 4, 5]

# передать в isinstance в качестве второго параметра кортеж из типов (int, float)
# и если переменная i будет подходить под один из этих типов, то условие выполнится и функция вернёт да.
a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
sum_nums = 0
for i in a:
    if isinstance(i, (int, float)):
       sum_nums += i
print(sum_nums) # ->18.5

""" ЗАДАЧИ """
""" №1 Функция должна среди всех переданных значений найти только строки, 
    найти их количество и  вернуть в качестве результата."""
def count_strings(*args):
    return sum([1 for i in args if isinstance(i, str)])
print(count_strings(1, 2, 'hello', [2, 3, 4], True, 'as')) # -> 2

""" №2 Ф-ия должна отобрать только те имена параметров, у которых значения являются списками или кортежами"""
def find_keys(**kwargs):
    return sorted([k for k,v in kwargs.items() if isinstance(v,(list,tuple))],key=lambda x:x.lower())
print(find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2))) # -> ['Also', 'marks']
assert find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]) == ['A', 'b', 't', 'W']