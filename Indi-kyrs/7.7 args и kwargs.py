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







