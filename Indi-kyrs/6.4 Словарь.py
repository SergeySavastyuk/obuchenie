from pprint import pprint # для красивого вывода словаря
person = {}
s = 'IVANOV IVAN 19 Samara SGU 4 5 5 5 4 3 5 3'
s = s.split()
print(s)
print('-'*15)
person['last_name'] = s[0]
person['first_name'] = s[1]
person['age'] = int(s[2])
person['city'] = s[3]
person['university'] = s[4]
del person['city']
print(person)
print('-'*15)
person['marks'] = []
for i in s[5:]:
    person['marks'].append(int(i))
pprint(person)

'''На вход программе поступает целое число n. Вам необходимо создать словарь, который будет включать в себя ключи от 1 до n'''
print({i:i**2 for i in range(1,int(input())+1)}) # 32

'''Напишите программу, которая печатает словарь alphabet, где ключи  - строчные английские символы, 
а значения - порядковые номера букв в алфавите начиная с 1.'''
# Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:
from string import ascii_lowercase
print(ascii_lowercase)
from string import ascii_lowercase
alphabet = {i:ascii_lowercase.index(i)+1 for i in ascii_lowercase}
print(alphabet)
""" Способы создания словаря """
# при помощи функции dict()
a = {}
b = dict()

# генератор словаря
a = {i:i**2+1 for i in range(10)}
print(a)
# При помощи генератора можно обходить и уже существующие словари.
data = {
    'Джефф Безос': '177',
    'ИлоН МаСк': '126',
    'бернар АрнО': '150',
    'БиЛл ГеЙтС': '124',}
new_data = {key.title(): int(value) for key, value in data.items()}
print(new_data) # {'Джефф Безос': 177, 'Илон Маск': 126, 'Бернар Арно': 150, 'Билл Гейтс': 124}

from string import ascii_lowercase  #  ascii_lowercase содержит перечень букв нижнего регистра
alphabet = {i:ascii_lowercase.index(i)+1 for i in ascii_lowercase}
print(alphabet)

""" Слияние словарей """
dict_1 = {'John': 15, 'Rick': 10, 'Misa' : 12 }
dict_2 = {'Bonnie': 18,'Rick': 20}
dict_3 = dict_1 | dict_2
dict_4 = dict_2 | dict_1
print(dict_3) # {'John': 15, 'Rick': 20, 'Misa': 12, 'Bonnie': 18}
print('-'*15)
print(dict_4) # {'Bonnie': 18, 'Rick': 10, 'John': 15, 'Misa': 12}

""" Методы словаря """
# Метод .clear() очищает весь словарь. В итоге после вызова получится пустой словарь

# Метод get() – позволяет получить значение ключа.  Нужно указать внутри скобок один аргумент – ключ,
# значение которого хотим получить. Если ключа в словаре нет, то выведет None, но если в метод get()
# внести второй аргумент, то вместо None будет появляться это значение:
d = {1: 'one', 2: 'two', 3: 'three'}
print(d.get(1)) # one
print(d.get(5)) # None
print(d.get(5, 'No such key')) # No such key

# Метод setdefault()  - получает значение ключа. Похож на прошлый метод get(), однако при обращении к несуществующему
# ключу он вносит в словарь новую пару ключ-значение. Значением будет второй аргумент, который был передан в этот
# метод, либо же None, если в методе только один аргумент:
d = {1: 'one', 2: 'two', 3: 'three'}
print(d) # {1: 'one', 2: 'two', 3: 'three'}
print(d.setdefault(1)) # one
print(d) # {1: 'one', 2: 'two', 3: 'three'}
print(d.setdefault(6)) # None
print(d) # {1: 'one', 2: 'two', 3: 'three', 6: None}
print(d.setdefault(7, 'семь' )) # семь
print(d) # {1: 'one', 2: 'two', 3: 'three', 6: None, 7: 'семь'}
# пример нужно посчитать все слова
def get_word_indices(strings: list[str]) -> dict:
    a = {}
    count = 0
    for string in strings:
        string = string.lower().split()
        for i in string:
            a.setdefault(i, []).append(count)
        count += 1
    return a
assert get_word_indices(['This is a string','test String','test','string'])
# -> {'this': [0], 'is': [0], 'a': [0],'string': [0, 1, 3], 'test': [1, 2]}

# Метод pop() – возвращает значение, находящееся под указанным ключом, а из самого словаря удаляется пара с данным ключом:
d = {1: 'one', 2: 'two', 3: 'three'}
print(d.pop(2)) # two
print(d) # {1: 'one', 3: 'three'}

# Метод popitem() удалит и вернет двойной кортеж (key, value) из словаря. Пары возвращаются с конца словаря, в порядке LIFO (последним пришёл - первым ушёл).
d = {1: 'one', 2: 'two', 3: 'three'}
print(d.popitem()) # (3, 'three')
print(d) # {1: 'one', 2: 'two'}

# Метод keys() позволяет получить все ключи словаря.
d = {1: 'one', 2: 'two', 3: 'three'}
print(d.keys()) # dict_keys([1, 2, 3])
print(list(d.keys())) # [1, 2, 3]

# Метод values() позволяет получить все значения словаря
d = {1: 'one', 2: 'two', 3: 'three'}
print(d.values()) # dict_values(['one', 'two', 'three'])

# Метод items() – возвращает коллекцию, в которой содержатся все пары «ключ-значение» в виде кортежей
d = {1: 'one', 2: 'two', 3: 'three'}
print(d.items()) # dict_items([(1, 'one'), (2, 'two'), (3, 'three')])

# Метод update() обновляет словарь элементами из другого словаря. Другими словами, метод сливает(мержит от
# английского «merge») один словарь в другой: добавляются новые ключи из другого словаря, при совпадении ключей
# записывается значение из переданного словаря
d = {1: 'one', 2: 'two', 3: 'three'}
w = {4: 'four', 5: 'five', 3: 'four' }
d.update(w)
print(d) # {1: 'one', 2: 'two', 3: 'four', 4: 'four', 5: 'five'}

""" Напишите код для преобразования списка из целых чисел произвольной длины в словарь, 
вложенность которого зависит от длины списка. """
sequence = map(int, input().split()[::-1]) # 45 45 66 21 94 62 50 13 96
nested_dict = next(sequence)
[nested_dict := {key: nested_dict} for key in sequence]
print(nested_dict) # {45: {45: {66: {21: {94: {62: {50: {13: 96}}}}}}}}

""" поступает на вход строка, вам необходимо подсчитать сколько раз встретилась каждая буква в этой строке """
s = input() # ZZzzzZ34 WWw777
base = {}
for i in s.lower():
    if i.isalpha():
        base[i] = base.get(i, 0) + 1
print(base) # {'z': 6, 'w': 3}
# Второй способ
s = input().lower()
d = {i: s.count(i) for i in s if i.isalpha()}
print(d)

""" Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов. """
s1 = input().lower() # abracadabra
s2 = input().lower() # cadabraabra
print(('NO','YES')[{i:s2.count(i) for i in s2 if i.isalpha()}=={i:s1.count(i) for i in s1 if i.isalpha()}])
# второй способ
print('YES' if sorted(input()) == sorted(input()) else 'NO')

""" Азбука Морзе """
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
stroka = input().split() # Houston we have a problem
for word in stroka:
    for i in word.lower():
        print(morze[i], end=' ')
    print()