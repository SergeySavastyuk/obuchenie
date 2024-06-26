

""" lambda функции необходимы в использовании в тех случаях, когда необходимо написать функцию в одну строчку """
# Lambda заменяет только те функции, которые содержат return. После двоеточия указывается значение,
# которое будет возвращено из lambda функции.

""" Условный оператор if может быть применен в анонимных функциях, но с небольшой натяжкой. """
def f(x):
    if x > 0:
        return 'positive'
    return 'negative'
# или
a = lambda x: 'positive' if x>0 else 'negative'


""" Lambda функция как ключ сортировки """
# У метода sort() есть именованный аргумент key, который должен принимать функцию. Здесь можно создать обычную функцию,
# а можно анонимную. Отсортируем наш список по последней цифре в числе.
a = [72, 4, 39, 100, 200, 5, 28, 123, 44]
a.sort(key=lambda x: x%10)
print(a) # -> [100, 200, 72, 123, 4, 44, 5, 28, 39]

sq = lambda x, y:  x**2 + y**2
print(sq(10.0,1.5)) # -> 102.25

"""Напишите lambda функцию, которая принимает произвольное количество числовых аргументов 
    и выводит их среднее арифметическое."""
average = lambda *args: sum(args)/len(args)
print(average(4,5,6)) # -> 5.0

