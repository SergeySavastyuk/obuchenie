"""Напишите программу, которая  принимает на вход три целых числа в одной строке через пробел
и выводит их последовательно через запятую как в примерах ниже"""
print(*list(map(int, input().split())), sep=',')
# другой способ
print(input().replace(' ',','))
# третий способ
print(*input().split(), sep=',')  # * - убирает ковычки и рамки  !!!!!!!!!!!!!!!

"""Программа, считывает натуральное число n, после чего выводит двойное неравенство этого числа с его соседними числами."""
print(x := int(input())-1, x + 1, x + 2, sep='<')

"""Программа принимает на вход строку - разделитель,
вам необходимо распечатать числа от 1 до 5, выводя между ними введенный разделител"""
print(*range(6), sep=input())  # * - распаковывает список !!!!!!!!!!!!!!!!!!