""" Функция filter """

"""filter(function or None, iterable) --> filter object
 |  
 |  Возвращает итератор, возвращающий те элементы iterable, для которых функция(item)
 | имеет значение true. Если значение function равно None, возвращает элементы, которые имеют значение true.
 
Видим, что filter() должна принимать другую функцию(function) или если передать вместо функции значение None, 
функция filter оставит только «правдивые» элементы, и  итерабельный(iterable) объект.
В итоге выполнения функции filter() мы получим filter object, который  будет представлять собой итератор и в него 
войдут только те элементы итерабельной последовательности, для которых функция function вернёт значение True. 
Отсюда сразу идёт ограничение нашей для передаваемой функции function- она должна возвращать булево значение:  
True либо False. Другие функции для работы с filter() не подойдут."""

def greater_10(x): return x>10 # ф-ия возвращает значение больше 10
numbers = [14, 0, 5, -79, 645, 7952, 18, 0, -192, 471]
print(list(filter(greater_10, numbers))) #-> [14, 645, 7952, 18, 471]

# И точно так же, как и с функцией map, функцию filter можно заменить при помощи генератора списка:
def is_two_digit(x): return x > 9 and x < 100
numbers = [14, 0, 5, -79, 645, 7952, 18, 0, -192, 471]
num_filters = list(filter(is_two_digit, numbers)) # фильтруем через filter
num_list_comp = [n for n in numbers if n > 9 and n < 100] # фильтруем через генератор списка
print(num_filters) #-> [14, 18]
print(num_list_comp) #-> [14, 18]

"""В функцию filter можно также передавать не только собственные функции, но и встроенные функции python, 
но не стоит забывать, что эта встроенная функция должна возвращать True/False. 
Одной из таких функций является функция bool, которая преобразует переданные ей значения к логическому типу. 
Преобразует она по следующему принципу: если значение не является пустым, то получим True, если значение пустое – False
Все значения, которые преобразуются в False (пустые строки, пустые списки, ноль и т.д.), будут отброшены функцией filter."""
values = ['Hi', [], 1, 0, 0.0, False, True, [1,2], {}]
values_not_empty = list(filter(bool, values))
print(values_not_empty) #-> ['Hi', 1, True, [1, 2]]


""" Анонимные функции и filter """
""" filter(lambda x: <действие>, <последовательность>) """
words = ['word', 'hello', '3243', 'potato', 'carrot', 'hi']
words_len_gt_4 = list(filter(lambda x: len(x) > 4, words))
print(words_len_gt_4) #-> ['hello', 'potato', 'carrot']


""" Методы объектов внутри filter """
""" Внутрь filter в качестве функции можно также передавать и методы объектов. Но метод должен возвращать True/False. """
phrase = 'IphonE 12 cost 645,89$'
only_digits = list(filter(str.isdigit, phrase))
print(only_digits) #-> ['1', '2', '6', '4', '5', '8', '9']
only_alpha = list(filter(str.isalpha, phrase))
print(only_alpha) #-> ['I', 'p', 'h', 'o', 'n', 'E', 'c', 'o', 's', 't']


""" Фильтрация словаря """
cities = {
    'moscow': 800,
    'boston': 750,
    'LA': 400,
    'SF': 900,
    'Chicago': 650,
    'SP': 600,
}
more_700 = list(filter(lambda x: cities[x] > 700, cities))
print(more_700) #-> ['moscow', 'boston', 'SF']

""" ЗАДАЧИ """

""" №1 отфильтрует список numbers так, чтобы в нем остались только четные значения"""
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x:x%2==0,numbers))) #-> [0, 2, 4, 6, 8, 10]

""" №2 отфильтровать по отрицательные значения, нулевые значения,положительные - Вывести значения в том же порядке"""
numbers = [54, 71, 65, 51, 36, -82, -32, 61, -61, 92, 17, -68, -62, 40, 16, -49, -51, -38, 60, -24, -61, 3, -26]
print(len(list(filter(lambda x:x<0,numbers))), len(list(filter(lambda x:x==0,numbers))),
      len(list(filter(lambda x:x>0,numbers)))) #-> 11 0 12

""" №3 отфильтровать список days так, чтобы в нем остались только дни, 
названия которых состоят из четырех символов или начинаются с буквы S"""
days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
print(*sorted([*filter(lambda x:len(x)==4 or x[0]=='S',days)]),sep='\n') # *filter распаковывает объект filter,
# иначе нужно преобразовывать в список, *sorted - распаковывает конечный список


