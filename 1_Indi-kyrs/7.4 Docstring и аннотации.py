''' Docstring - документируем свои функции '''
def add_binary(a, b):
    """Возвращает сумму чисел a и b в двоичном виде"""
    binary_sum = bin(a+b)[2:]
    return binary_sum


'''Аннотации'''
'''Аннотации – инструмент, позволяющий сделать код более информативным и избавиться от некоторых проблем, 
связанных с динамической типизацией. '''
def add_numbers(a: int, b: int) -> int:
    return a + b
print(add_numbers.__annotations__)


'''Модуль typing
Встроенный модуль typing позволяет создавать аннотации в более сложных случаях, например если вы хотите 
проаннотировать переменную сразу несколькими типами или указать аннотацию для элементов списка.'''

# При помощи объекта Optional мы можем разрешить хранить в одной переменной не только указанный тип, но и значение None
from typing import Optional # обязательно после Optional тип указывается в квадратных скобках
num: Optional[int] = None
word: Optional[str] = None
# (python >=3.9)
num: int | None = None
word: str | None = None

# Any - Например вы хотите указать при помощи аннотаций, что в переменной можно сохранить любой тип переменной.
from typing import Any
value: Any
value = 10
print(value)
value = [1, 2, 3]
print(value)
value = {'hi': 'привет'}
print(value)

# Union
# C помощью этого объекта можно указывать сразу несколько типов данных, которые могут быть приняты.
from typing import Union
param: Union[int, float, str] = 3
# При такой аннотации в переменной param могут хранится вещественные и целые числа, а также строки
# Union полезна в версиях python до 3.10, поскольку в этой версии появилась короткая запись данной функции через вертикальную черту:
param: int| float| str

# Аннотация элементов списков и множеств
from typing import List
words: List[str] = ["hello", "world"]
# (python >=3.9)
words: list[str] = ["hello", "world"]

from typing import Set, FrozenSet
words: Set[str] = {"hello", "world"}
numbers: FrozenSet[int] = frozenset([1, 2, 2, 1])

# Аннотация элементов кортежа
from typing import Tuple
words: Tuple[str, int, int] = ("hello", 300, 50) # на каждый элемент пишется тип в анатации
words: Tuple[str, ...] = ("hello", "world", '!') # неизвестное количество ТОЛЬКО строк

# Аннотация словарей
from typing import Dict
person: Dict[str, str] = { "first_name": "John", "last_name": "Doe"}
# (python >=3.9)
person: dict[str, str] = { "first_name": "John", "last_name": "Doe"}


# Давайте взглянем на более сложный пример
from typing import Dict, Optional, Union
def foo(bar: Dict[Union[str, int], Optional[str]]) -> bool:
   return True
# (python >=3.9)
def foo(bar: dict[str | int, str | None]) -> bool:
   return True
# Здесь функция foo принимает один аргумент bar, он должен являться словарем, у которого ключи могут быть
# либо строкой, либо целым числом, а значения могут быть либо пустыми (тип None), либо строкой


MIN_DRIVING_AGE = 18
def allowed_driving(name: str, age: int) -> None:
    print([f'{name} еще рано садиться за руль',f'{name} может водить'][age>=MIN_DRIVING_AGE])