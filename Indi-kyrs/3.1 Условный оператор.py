'''Если это строка «Python», программа выводит ДА, в противном случае программа выводит НЕТ'''
print('НДЕАТ'[input() == 'Python'::2]) # через срез строки 'НДЕАТ'
print("ДА" if input() == "Python" else "НЕТ") # условный оператор
print(['НЕТ', 'ДА'][input() == 'Python']) # через срез списка

"""подоходный налог"""
print(n if (n := int(input())) < 20000 else n * 0.87)

'''Вводятся два целых числа, каждое в отдельной строке. Ваша задача вывести наибольшее из данных чисел.'''
print(a if (a := int(input())) > (b := int(input())) else b)
# другой способ
(lambda x,y : print(x if x>y else y))(int(input()),int(input()))

'''на вход три натуральных числа A, B и C через пробел. 
необходимо вывести YES в том случае, если A + B = C и вывести NO в противном случае.'''
a,b,c = map(int,input().split())
print('YES' if a+b==c  else 'NO')
# другой способ
print(['NO', 'YES'][(lambda a, b, c: a + b == c)(*map(int, input().split()))])

'''на вход список из целых чисел, нужно удалить из этого списка числа 3, 5, 7 и 9'''
a = list(map(int, input().split()))
[a.remove(i) for i in (3, 5, 7, 9) if i in a]
print(a)
# другой способ
print([int(i) for i in input().split() if i not in '3579'])

'''число N палиндромом, т.е. числом, которое одинаково читается слева направо и справа налево'''
print(['NO', 'YES'][(n:=input())[::-1] == n])

''' Треугольник '''
print((lambda a, b, c: "YNEOS"[a + b <= c::2])(*sorted([int(input()) for _ in "abc"])))
# другой способ
a, b, c = sorted([int(input()) for i in '___'])
print(['NO', 'YES'][a + b > c])

''''Программа получает на вход одно целое число N (0 ≤ N < 106) и должна вывести «YES»,
если билет с номером N счастливый и «NO» в противном случае'''
print('YES' if sum((n := [*map(int, f'{input():>06}')])[:3]) == sum(n[-3:]) else 'NO')
# другой способ
print(['NO', 'YES'][sum((n := [*map(int, f'{input():>06}')])[:3]) == sum(n[-3:])])
# очень хороший код через срез с 0 до -числа, берёт какбы не достающие цифры!!!!!!!!!!!!!!!!!!!!!111
n = [int(i) for i in input()] #если число 2011
print(('NO', 'YES')[sum(n[:-3]) == sum(n[-3:])]) # берет [2] и [0,1,1] через срез

'''На вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами'''
letter = ' abcdefgh'
print(['NO', 'YES'][(letter.find((a := list(map(str, input())))[0]) + int(a[1])) % 2 ==
                    (letter.find((b := list(map(str, input())))[0]) + int(b[1])) % 2])
# другой способ через Юникод, очень красиво  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(('YES', 'NO')[sum(map(ord, input() + input())) % 2])

""" Два вещественных числа в каждой отдельной строчки. На третьей строке вводится символ операции 
Необходимо посчитать значение операции «+», «-», «*», «/». Если ввели символ, который не относится к данным операциям, 
необходимо вывести «Неизвестно». «Неизвестно» также выводится при попытке деления на ноль"""
a,b,n = [input() for i in '___']
a,b = float(a),float(b)
print(f'{a+b}' if n=='+'
      else f'{a-b}' if n=='-'
      else f'{a*b}' if n=='*'
      else f'{a/b}' if n=='/' and b!=0
      else 'Неизвестно' if b==0
      else 'Неизвестно')