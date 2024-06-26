""" примеры функций """


def fun_2(c,d,a=3,b=7,**e): # функция с параметрами, сначала позиционные, потом по умолчанию параметры
    return a+b+c+d, e
print(fun_2(2,4,e=50)) #аргумент задается сразу
'''c и d - позиционные аргументы
a и b - аргументы по умолчанию
е - именные аргументы'''
#fun_2(int(input(':')),int(input(':')))  # или спрашивается
print('-'*50)

function = lambda x:print(f'{x} говорит hello world!')
function('Ivan')
print('-'*50)

list1 = [i for i in range(11)]#  создадим список из диапазона
print(list(filter(lambda x:x%2==0,list1))) # отфильтруем через лямдо-функцию чётные числа из списка list1 и вернём список
print(lambda x:x%2==0, list1) # -> <function <lambda> at 0x00000000026D6790> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('-'*50)

def summa_n(t):
    S= sum([i for i in range(t+1)])
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {S}')
summa_n(10)
print('-'*50)

sum_num = lambda x: print(f'сумма цифр в строке {x} равна {sum([int(i) for i in x if i.isdigit()])}')
sum_num('-123.78')
print('-'*50)

def get_body_mass_index(w, h): # нужен рост и вес
    bmi = 10_000 * w / h ** 2
    print(('Недостаточная масса тела', 'Норма', 'Избыточная масса тела')[(bmi > 18.5) + (bmi > 25)])
get_body_mass_index(180,78)
print('-'*50)

def check_password(s): # проверка пароля
    a = len([i for i in s if i.isdigit()]) > 2
    b = len([i for i in s if i.isupper()]) > 0
    c = len([i for i in s if i in '!@#$%*']) > 0
    d = len(s) > 9
    print('Perfect password' if a and b and c and d else 'Easy peasy')
check_password('Ss1111163561f')
print('-'*50)

def count_letters(s):
    print(f'Количество заглавных символов: {len([i for i in s if i.isupper() and i.isalpha()])}')
    print(f'Количество строчных символов: {len([i for i in s if i.islower() and i.isalpha()])}')
count_letters('Привет, Старина')
print('-'*50)

""" Шифр цезаря """
# Этот шифр брал каждую букву исходной фразы и смещал ее на значение ключа, это так раз был на сдвиг.
# В пределах кодирования одной фразы значение сдвига всегда постоянно.
# caesar_cipher('leave out all the rest', -1) => 'kdzud nts zkk sgd qdrs'
# caesar_cipher('one more light', 3) => 'rqh pruh oljkw'
def shift_letter(letter:str,shift :int)-> str:
    """Функция сдвигает символ letter на shift позиций"""
    return chr(((ord(letter) - 97 + shift ) % 26) + 97)
def caesar_cipher(text: str, step: int) -> str:
    """Шифр цезаря"""
    return ''.join(shift_letter(i, step) if i.isalpha() else i for i in text)

'''Обход вложенных списков'''
x = [1, [57, [12, 36], 78], 2, [3, 4, [5, 6, [7, 8], [9, 10]], [11, 12]], [13, 14], 15]
def f(spisok, level=1):
    print(*spisok, '- level = ', level)
    for i in spisok:
        if type(i) == list:
            f(i, level + 1)
print(f(x))