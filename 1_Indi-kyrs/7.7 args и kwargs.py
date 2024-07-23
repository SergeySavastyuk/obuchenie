""" Множественное присвоение и оператор * """

""" Оператор * распаковывает объект """
print(list(range(1,5))) # -> [1, 2, 3, 4]
a = [4, 10]
# при использовании оператора * значения из списка 4 и 10 станут аргументами в функции range
print(list(range(*a))) # -> [4, 5, 6, 7, 8, 9]
# другое применение
a = [1, 2, 3, 4]
print(a, sep=',') # -> [1, 2, 3, 4]
print(*a, sep=',') # -> 1,2,3,4
print(1,2,3,sep='@') # -> 1@2@3


""" '*args' все переданные значения упаковались в виде кортежа. 
И сколько бы значений вы не передали, все они сохранятся в переменной args обязательно в виде кортежа"""
def fun(*args,**kwargs): # Опертор * и **
    print(args) #возвращает кортеж неименованный аргументов
    print(kwargs)  #возвращает словарь именованных  аргументов
fun(1,2,3,4,5,666,7,a=30,b=50)

def check_sum(*args):
    print(['not enough','verification passed'][sum(map(int,args))>=50])
check_sum(20,20,10)

def print_goods(*elements) -> None:
    answer = [i for i in elements if type(i) is str and i]
    if not answer:
        print(f'Нет товаров')
    else:
        for i, v in enumerate(answer, 1):
            print(f'{i}. {v}')
print_goods(1, True, 'Грушечка', '', 'Pineapple')

def info_kwargs(**kwargs):
    for key,value in sorted(kwargs.items()):
        print(f'{key} = {value}')
info_kwargs(first_name="John", last_name="Doe", age=33)
""" данный вызов печатает следующие строки
age = 33
first_name = John
last_name = Doe
"""

def create_actor(name= 'Райан',surname= 'Рейнольдс',age= 46,**kwargs)->dict:
    b = {}
    b['name'] = name
    b['surname'] = surname
    b['age']=age
    for key in kwargs:
        b[key]=kwargs[key]
    return b
create_actor(name='Jack', age=20)

def f (a,b,*c,**d):
    print(f"значение переменной а - {a}\n" # -> 123
          f"значение переменной b - {b}\n" # -> 555
          f"значения переменной *с - {c}\n" # -> ([12, 74, 96], ('45687', 55596, {'b': 60}), 89, 11111111, {'a': '30'})
          f"значения переменной **d - {d}") # -> {'e': 5637}
    for key,value in d.items():
        print(f'данные словаря - {key},{value}') # -> данные словаря - e,5637
a = [123,'555',[12,74,96], ('45687',55596,{'b': 60}),89,11111111,{'a': '30'}]
# оператор * распаковывает наш список по неименованным аргументам, после отдельно добавляем именованный аргумент
f(*a, e=5637)





