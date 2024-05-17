"""Программа принимает на вход целое положительное число n (n<=15) - количество уровней, ваша задача вывести n уровней,
 в каждом из которых стоят числа от 1 до значения уровня."""
for i in range(1,int(input())+1): # 3
    for y in range(1, i+1):
        print(y,end=' ')
    print()

"""Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки. """
print(*['*'* i for i in map(int, input().split())],sep='\n') # 3 7 1 10 8

"""Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки, в случае если элементы соседние 
совпадают менять их ненужно."""
# 7
# 8 5 3 1 4 7 9
n = int(input())
s = list(map(int, input().split()))
count = 0
for a in range(n-1):
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            s[i], s[i + 1] = s[i + 1], s[i]
            count += 1
print(*s)
print(count)

"""Ваша задача отсортировать список по возрастанию при помощи сортировки вставками, 
в случае если элементы соседние совпадают менять их ненужно."""
# 6
# 5 4 2 15 6 6
n = int(input())
s = list(map(int,input().split()))
for i in range(n):
    while i!=0 and s[i]<s[i-1]:
        s[i],s[i-1]=s[i-1],s[i]
        i-=1
print(*s)
