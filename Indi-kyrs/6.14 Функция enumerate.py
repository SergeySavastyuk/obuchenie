""" метод enumerate() превращает коллекцию в пару где первый элемент индекс """

a = [10,20,30,40,50,60,70]  # обойдём список
print(list(enumerate(a))) # метод enumerate() превращает коллекцию в пару где первый элемент индекс
print('_____________')
for index,value in enumerate(a):
    print(index,value)

print('\nобойдём строку')
s = 'hello me'
for index,value in enumerate(s):  # обойдём строку
    print(index,value)

print('\nв enumerate есть особенность позволяющая установить с какого значения пойдёт отсчёт')
print('\nобойдём кортеж с указанием начального значения через enumerate(kortesh,10) - внимание на число после запятой')
kortesh = ('hello','List','mango','banan')
for index,value in enumerate(kortesh,10):  # обойдём кортеж с указанием начального значения индекса (по ум. он равен 0)
    print(index,value)
print([pair[::-1] for pair in enumerate(kortesh, 10)]) # тоже самое но в одну строку, но в кортеже меняем местами
print(*[f'Word № {word} = {index}' for word,index in enumerate(kortesh,1)],sep='\n')  # уже две переменной и другой вывод

'''Алгоритм Луна'''
n = list(map(int,input()))  # 3942682966937054
for key,value in enumerate(n):
    if key%2==0:
        if value*2>9:
            n[key]=value*2-9
        else: n[key]=value*2
print(sum(n)%10==0)   # True