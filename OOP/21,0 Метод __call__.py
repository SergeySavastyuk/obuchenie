
""" Магический метод __call__ Делаем экземпляры вызываемыми """
""" сам класс является вызываемым, а вот объекты нет, но им можно добавить такую способность через метод __call__"""

class Counter:
    def __init__(self):
        print('init object', self)
        ''' сделаем замыкание как счётчик'''
        self.counter = 0 # наш счетчик, который хранит количество вызовов объекта

    def __call__(self, *args, **kwargs):
        print('object call', self)
        self.counter += 1
        print(f' наш экземпляр вызывался {self.counter} раз')

print(Counter())    # init object <__main__.Counter object at 0x0000000002795610>
                    # <__main__.Counter object at 0x0000000002795610>
print('_'*10)
a = Counter()
'вызовем объект '
a()     # init object <__main__.Counter object at 0x0000000002795610>
        # object call <__main__.Counter object at 0x0000000002795610>
a()
a()
print('_'*50)

class Counter2:
    def __init__(self):
        ''' Сделаем замыкание как среднеарифметическое'''
        self.counter = 0  # счётчик обращений
        self.summa = 0  # сумма
        self.length = 0 # длина последовательности

    def __call__(self, *args, **kwargs):
        self.length += len(args)
        self.summa+=sum(args)
        self.counter += 1
        print(f' средне арифметическое из {self.length} чисел равно {self.summa/self.length}')
        print(f' наш экземпляр вызывался {self.counter} раз')

b = Counter2()
b(3,4,6)
b(50,6,7,9)
b(0,9)
print('_'*50)
""" использование метода __call__ как декоратор """

from time import perf_counter
class Timer:
    def __init__(self,func):
        self.fn = func
    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'вызывается функция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        end = perf_counter()
        print(f'функция отработала за {end-start}')
        return result

@Timer # приравнивается к fact = Timer(fact) и таким образом мы декорируем всю функцию
def fact(n):
    pr = 1
    for i in range(1,n+1):
        pr*=i
    return pr

def fibonachi(n):
    if n<=2:
        return 1
    return fibonachi(n-1)+fibonachi(n-2)

print(fact(7))
print(Timer(fibonachi)(7)) # таким образом мы задекорировали не всю функцию, а только результат

