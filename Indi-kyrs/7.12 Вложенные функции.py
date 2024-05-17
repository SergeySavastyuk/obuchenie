
""" ЗАДАЧИ """

""" №1 функция Калькулятора """
def calculate(x:float, y:float, operation:str='a') -> None:
    def addition():
        print(x+y)
    def subtraction():
        print(x-y)
    def division():
        if y == 0:
            print('На ноль делить нельзя!')
        else:
            print(x/y)
    def multiplication():
        print(x*y)
    if operation == 'a': addition()
    elif operation == 's': subtraction()
    elif operation == 'd': division()
    elif operation == 'm': multiplication()
    else: print('Ошибка. Данной операции не существует')
calculate(10,4,'s')
calculate(10,0,'d')


""" Возврат вложенных функций в качестве результата """
def get_math_func(operation="+"):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    if operation == "+":    # если сработает условие
        return add          # то запускается нужная функция
    elif operation == "-":
        return subtract
print('---Или можно сразу использовать двойной вызов---')
print(get_math_func('+')(3, 4))
print(get_math_func('-')(3, 4))

# или
def get_user_data_handler(user_role):
    def admin_user_data_handler():
        print('Обработка данных для администраторов')
    def regular_user_data_handler():
        print('Обработка данных для обычных пользователей')
    def guest_user_data_handler():
        print('Обработка данных для обычных гостей')
    # Возвращаем соответствующую обработчику функцию в зависимости от роли пользователя
    if user_role == "admin":
        return admin_user_data_handler()
    elif user_role == "regular":
        return regular_user_data_handler()
    return guest_user_data_handler()
get_user_data_handler("admin")


""" как проаннотировать саму функцию """
from typing import Callable
def get_math_func(operation: str) -> Callable[[int, int], int]:
    def add(a: int, b: int) -> int:
        return a + b
    def subtract(a: int, b: int) -> int:
        return a - b
    if operation == "+":
        return add
    elif operation == "-":
        return subtract
# В записи Callable[[int, int], int]:
# обратите внимание на выделенный список: здесь указывается что функция, возвращаемая get_math_func,
# принимает два целочисленных аргумента (a и b).
# А следующий int в записи Callable[[int, int], int]: указывает на тип возвращаемого значения.
# Подсказка типа Callable[[int, int], int] указывает, что первый аргумент — это кортеж из двух целых чисел,
# а второй аргумент — одно целое число.

