""" Функция all """

""" all(iterable, /) 
    Возвращает значение True, если значение bool(x) равно True для всех значений x в итерационной таблице.
    Если повторяемая строка пуста, верните значение True."""
"""Функция all принимает итерабельную последовательность и возвращает True , 
    когда все элементы в этой последовательности правдивы. Если хотя бы один элемент пустой, вернется False"""
"""Функция all проходит по всем объектам коллекции и преобразует их в тип данных bool. 
    И т.к. all переводится как «все», соответственно, она будет истинной только в том случае, 
    когда все входящие в коллекцию элементы являются непустыми. 
    Если же мы изменим нашу коллекцию и сделаем хотя бы один ее элемент пустым, то результат будет False"""
numbers = [1, 2, 3, 4, 5]
print(all(numbers))         # -> True
print(all([1, 2, 0, 4, 5])) # -> False


""" Функция any """

""" any(iterable, /) """
""" Она тоже принимает на вход итерабельную последовательность и возвращает True, 
    если хотя бы один из элементов коллекции будет непустым. Если все элементы пустые, вернется False"""
numbers = [1, 0, 3, 0, 0]
print(any(numbers))                 # -> True
print(any([0, 0, 0, 0]))            # -> False
print(any([False, False, True]))    # -> True
print(any([False, False, False]))   # -> False


""" Применение функций all и any """
# Эти функции очень полезны, когда вы хотите одновременно проверить выполнение нескольких условий.
a = 100
condition_1 = a % 2 != 0
condition_2 = a > 50
condition_3 = a < 1000
print(all((condition_1, condition_2, condition_3))) # -> False
print(any([condition_1, condition_2, condition_3])) # -> True
""" Обратите внимание на дополнительную пару круглых и квадратных скобок внутри функций all и any. 
    Они необходимы для создания кортежа или списка соответственно. Без них вы получили бы ошибку."""


""" Генератор списка и функции all и any """
words = ['notice', 'deter', 'west', 'brush', 'stadium', 'package', 'price', 'clothes', 'sword', 'apology']
check = [len(word) >= 4 for word in words]
print(check) # -> [True, True, True, True, True, True, True, True, True, True]
print(all(check)) # -> True
print(all([len(word) > 4 for word in words])) # -> False
print(any([len(word) > 7 for word in words])) # -> False
print(any([len(word) >= 7 for word in words])) # -> True


""" ЗАДАЧИ """

""" №1 проверить, во всех ли словах есть английская буква A"""
print(all(['a' in i.lower() for i in 'acquaintance disAgree'.split()])) # -> True

""" №2 Ваша задача вывести True, если элементы в списке отсортированы строго по убыванию. """
a = list(map(int,'8 11 6 5 4 3'.split()))
print(a == sorted(a,reverse=True) and a[0]>sorted(a,reverse=True)[-1]) #  в первой части мы сортируем список
# по убыванию и сравниваем его с изначальным списком, во второй части мы сравниваем первый элемент списка с последним,
# дабы убедиться что было именно убывание

""" №3 Программа должна вывести True , если встретилось хотя бы одно слово, заканчивающееся на ought """
print(any([i.lower().endswith('ought') for i in 'food forethought muscle stadium'.split()]))