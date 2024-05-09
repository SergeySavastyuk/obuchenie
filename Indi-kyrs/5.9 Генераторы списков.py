
print([i for i in range(1,int(input())+1)])

'''При помощи list comprehension создайте список, состоящий из нечетных натуральных чисел в интервале n:n**2'''
[print([i for i in range(n,n**2+1) if i%2!=0]) for n in [int(input())]] # 7

'''Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b включительно и вывести 
его на экран.
Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно, 
двигаясь в порядке убывания, и затем вывести его.'''
# 10 13
a, b = map(int, input().split())
print([i**2 for i in range(a, b + 1)] or [i**3 for i in range(a, b - 1, -1)])

'''При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита'''
from string import ascii_uppercase
print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
from string import ascii_uppercase
print([ascii_uppercase[i].upper() for i in range(int(input()))]) # 9

'''При помощи генератора-списков создайте список, состоящий из слов,  начинающихся с буквы 't' или 'T'. 
Слова возьмите из переменной phrase, также не забывайте про метод split()'''
phrase = 'Take only the words that start with t in this sentence'
print([i for i in phrase.split() if i.startswith(("T", "t"))])





