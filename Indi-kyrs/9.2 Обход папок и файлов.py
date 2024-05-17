import os
# распечатать все файлы и папки рекурсивно
for dirpath, dirnames, filenames in os.walk("../../восстановленное"):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))


import os
path = r'D:\питон старое\python_obuchenie\файлы' # запишем путь
print(f'выводит все наименования по данному адресу: {os.listdir(path)}')
print('-----------')
for i in os.listdir(path):
    print(f'выведем саму строку и её тип: {i} - {type(i)}')
    print('выведи её адрес через конкатенацию, он состоит из нашего пути + "\\" + наша строка')
    print(path+'\\'+i) # выведи её адрес через конкатенацию, он состоит из нашего пути + '\\' + наша строка
    print('-----------')
    print('метод определения папок')
    print('система.путь.проверка на папку(полный путь до папки с именем) - возвращает True или False')
    print(i,'-', os.path.isdir(path+'\\'+i)) # система.путь.проверка на папку(полный путь до папки с именем)
    print('-----------')
    print('метод определения файлов, похож на метод с папками')
    print(i,'-', os.path.isfile(path+'\\'+i))
print('++++++++++++++++')
print('++++++++++++++++')

print('напишем через рекурсию функцию обхода всех папок с указанием глубины')
path = 'D:\\питон старое\python_obuchenie\файлы'
def obxod(path,level=1):
    name= os.listdir(path) or ' !!!No name!!! '
    print(f'уровень: {level}, имя: {name}')
    for i in os.listdir(path):
        if os.path.isdir(path +'\\'+i):
            print('спускаемся в %s' %path +'\\'+i)
            print('cнова вызываем нашу функцию')
            obxod(path +'\\'+i, level+1)
            print(f'возвращаемся в {path} ')
obxod(path)
print('_________________________________________________')

name = '1.txt'
def obxod2(path, level=1,name=None):
    names = os.listdir(path) or ' !!! NO NAME !!! '
    print(f'имя - {names}, уровень - {level}   ')
    for i in os.listdir(path):
        if i == name:
            print(f'наш файл {name} найден на уровне {level} по адресу {path}')
        if os.path.isdir(path+'\\'+i):
            print(f'спускаемся в %s ' %path+'\\'+i)
            obxod2(path+'\\'+i, level+1, name)
            print(f'возвращаемся в %s ' %path)
obxod2(path,name=name)
print('_________________________________________________')

'''Рекурсивный обход файлов'''
import os
path = 'E:\\док' #  путь к нашей корневой папке
def scan_dir(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path): # обойдём все папка в указанном пути
        if os.path.isdir(path + '\\' + i): # os.path.isdir(путь и имя папки нужно) если это папка то будет True
            print('Спускаемся', path + '\\' + i)
            scan_dir(path + '\\' + i, level + 1) # повторный вызов функции с указанием нового адреса и уровня
            print('Возвращаемся в', path)
scan_dir(path)