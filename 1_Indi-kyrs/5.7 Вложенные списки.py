'''Вам нужно посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.'''
# 3
# 1 2 3
# 4 5 6
# 7 8 9
n = int(input())
tabel = []
s = 0
for i in range(n):
    tabel.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i == j:
            s+=tabel[i][j]
print(s)

'''Необходимо обойти элементы этой матрицы сверху вниз слева направо и вывести элементы именно в таком порядке в виде таблицы. '''
# 5
# 3 4 9 1 2
# 8 2 0 5 1
# 4 7 4 8 7
# 7 1 3 3 8
# 5 6 3 7 0
n = int(input())
tabel = []
s = 0
for i in range(n):
    tabel.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        print(tabel[j][i],end=' ')
    print()

'''Необходимо обойти элементы этой матрицы снизу вверх справа налево и вывести элементы именно в 
таком порядке в виде таблицы. '''
# 5
# 3 4 9 6 2
# 8 2 0 5 1
# 4 7 4 8 7
# 7 1 3 3 8
# 5 6 3 7 0
n = int(input())
tabel = []
for i in range(n):
    tabel.append(list(map(int,input().split())))
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        print(tabel[j][i],end=' ')
    print()

'''Требуется вычислить сумму элементов в каждой строке и в каждом столбце.'''
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
n,m = map(int, input().split())
table = [list(map(int, input().split())) for i in range(n)]
for i in table:
    print(sum(i),end=' ')
print()
for i in range(m):
    s = 0
    for j in range(n):
        s+=table[j][i]
    print(s,end=' ')

'''Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. 
Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
Программа должна вывести  2 числа: сумму и номер строки, для которой эта сумма достигается. 
Если таких строк несколько, то выводится номер наименьшей из них.'''
# 3 4
# 1 2 3 4
# 9 10 11 12
# 5 6 7 8
n,m=map(int,input().split())
s=[list(map(int,input().split())) for i in range(n)]
print(max(s:=[sum(s[i][j] for j in range(m)) for i in range(n)]), s.index(max(s)), sep='\n')

'''Программе поступает на вход 4 строки по 4 символа «W» или «B» в каждой, описывающие узор из плиток. 
Символ «W» обозначает плитку белого цвета, а «B» - черного.
Ваша задача вывести «Yes», если узор является симпатичным и «No» в противном случае.'''
# BWBW
# BBWB
# WWBB
# BWWW
s = [input() for i in range(4)]
is_True = True
for i in range(3):
    for j in range(3):
        if s[i][j] == s[i+1][j] == s[i][j+1] == s[i + 1][j + 1]:
            is_True = False
if is_True:
    print('Yes')
else:
    print('No')

'''Вывести самой большой элемент на побочной диагонали '''
# 3
# 1 2 3
# 4 5 6
# 7 8 9
print(max((input().split()[~i] for i in range(int(input()))), key=int))

'''Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в матрицы, 
а затем на новой строке три целых числа  A, B и C. Данные числа используются для заполнения
Заполните и распечатайте матрицу'''
# 5
# 7 2 1
n = int(input())
s = list(map(int, input().split()))
tabel = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            tabel[i][j]=s[-1]
        elif i<j:
            tabel[i][j] = s[0]
        else:
            tabel[i][j] = s[1]
for i in tabel:
    print(*i)

'''Программа считывает два числа: N и M (1 ≤ N, M ≤ 100). Последующие N строк описывают игровое поле - каждая из 
них содержит M символов. Символом «.» (точка) обозначена свободная клетка, символом «*» (звездочка) - занятая кораблем.'''
# 4 4
# ****
# **..
# *...
# *...
n, m = map(int, input().split())
matrix = []
count = 0
for i in range(n):
    matrix.append('.' + input() + '.') #заполняем матрицу по строкам с "виртуальными" точками по бокам, чтобы проще было обходить циклом
matrix.insert(0, '.' * (m + 2)) #добавляем в матрицу виртуальный потолок
matrix.append('.' * (m + 2)) #добавляем в матрицу виртуальный пол
for i in range(1, n+1):                 #пробегаемся циклом по всем свободным точкам с проверкой, свободны ли соседние
    if '.' in matrix[i]:
        for j in range(1, m+1):
            dot = matrix[i][j]
            if dot == '.':
                if dot == matrix[i+1][j] and dot == matrix[i-1][j] and dot == matrix[i][j+1] and dot == matrix[i][j-1]:
                    count += 1
print(count)

'''Треугольник Паскаля'''
'''Вывести заполненную матрицу'''
# 5 4
# 1 1 1 1
# 1 0 0 0
# 1 0 0 0
# 1 0 0 0
# 1 0 0 0
n, m = map(int, input().split())
tabel = [list(map(int, input().split())) for i in range(n)]
for i in range(1,n):
    for j in range(1,m):
        tabel[i][j]=tabel[i][j-1]+tabel[i-1][j]
for i in tabel:
    print(*i)

'''Заполнение змейкой'''
# 4 10
n, m = map(int, input().split())
tabel = [[int(i+j*m) for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        print(tabel[i][j] if i%2==0 else tabel[i][abs(j-(m-1))] ,end=' ')
    print()

'''Спираль'''
'''Программа должна вывести матрицу, заполненную числами от 1 до N2 по спирали, при этом между числами может быть 
любое количество пробелов. Не допускается начинать спираль в ином, кроме верхнего левого, углу, закручивать спираль 
против часовой стрелки или изнутри наружу.'''
rows = cols  = int(input())  # 5
tabel = [[0]*cols for i in range(rows)]
tabel[0] = [i+1 for i in range(cols)] # первая строка
col = 0; row = cols-1; index = cols; radius1 = rows; radius2 = cols
while index<rows*cols:
    radius1-=1
    for _ in range(radius1): #цикл проходит по правой стороне
        index+=1
        col +=1
        tabel[col][row]=index
    radius2-=1
    for _ in range(radius2): #цикл проходит по нижней стороне
        index += 1
        row -= 1
        tabel[col][row] = index
    if index>=rows*cols:  #проверка на конец змеи
        break
    radius1 -=1
    for _ in range(radius1): #цикл проходит по левой стороне
        index+=1
        col-=1
        tabel[col][row] = index
    radius2-=1
    for _ in range(radius2): #цикл проходит по верхней стороне (кроме первой строки)
        index+=1
        row+=1
        tabel[col][row] = index
[print(*i)for i in tabel]

# Функция create_matrix должна возвращать квадратную матрицу размером size х size, на диагонали которой располагаются
# числа от 1 до size. Все остальные элементы заполнены согласно параметрам up_fill и down_fill.
def create_matrix(size:int = 3,up_fill: int = 0, down_fill:int = 0):
    return [[up_fill if row < column else (down_fill, row+1)[row == column] for column in range(size)] for row in range(size)]
print(create_matrix(size=4, up_fill=7, down_fill=9))


'''Обход вложенных списков'''
x = [1, [57, [12, 36], 78], 2, [3, 4, [5, 6, [7, 8], [9, 10]], [11, 12]], [13, 14], 15]
def f(spisok, level=1):
    print(*spisok, '- level = ', level)
    for i in spisok:
        if type(i) == list:
            f(i, level + 1)
print(f(x))


""" треугольник паскаля """
n = 4 #int(input('количество уровней: '))
treygolnik =[]
for i in range(n+1):
    treygolnik.append([1]+[0]*n) # создаём таблицу
for i in treygolnik:
    print(i)
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
print('-----------------------------------------------------')

n = 4 #int(input('количество уровней: '))
treygolnik =[]
for i in range(n+1):
    treygolnik.append([1]+[0]*n) # создаём таблицу

for i in range(1,n+1): # перебираем строки
    for j in range(1,n+1): # перебираем столбцы
        treygolnik[i][j] = treygolnik[i-1][j]+treygolnik[i-1][j-1]

for i in range(n+1):
    for j in range(i+1):
        print(treygolnik[i][j], end=' ')
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1











