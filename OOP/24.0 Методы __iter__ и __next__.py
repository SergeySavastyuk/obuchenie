
''' Магические методы __iter__ и __next__ Итерация экземпляров класса Python '''
''' Данные методы позволяют объектам класса обходиться в цикле for '''

class Students:
    def __init__(self,name,surname,marks0):
        self.name = name
        self.surname = surname
        self.marks0 = marks0

    ''' первый способ (не основной)'''
    def __getitem__(self, item):
        return self.name[item]

igor = Students('Igor','Nikolai',[2,5,9,7,1,5,6,3])
print('обход с помощью __getitem__')
for i in igor:
    print(i)
print('-'*50)


class Students2:
    def __init__(self,name,surname,marks0):
        self.name = name
        self.surname = surname
        self.marks0 = marks0

    ''' второй способ (основной, но не полный т.к. работает только для строки)'''
    def __iter__(self): # срабатывает автоматически
        print('call __iter__')
        return iter(self.surname)

igor = Students2('Igor','Nikolai',[2,5,9,7,1,5,6,3])
print('обход с помощью __getitem__')
for i in igor:
    print(i)
print('-'*50)


class Marks: # для списка оценок сделаем свой класс
    def __init__(self,values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('call __next__ Marks')
        if self.index >= len(self.values): # проверка на окончание имени и выход из цикла без ошибки
            self.index = 0 # обнуление индекса
            raise StopIteration
        letter = self.values[self.index]
        self.index+=1
        return letter


class Students3:
    def __init__(self,name,surname,marks):
        self.name = name
        self.surname = surname
        self.marks = marks # для списка сделаем свой класс

    ''' второй способ (основной, полный, требует наличие метода next)'''
    def __iter__(self):
        print('call __iter__')
        self.index = 0
        # return iter(self.surname) # при таком коде сработает __iter__ и  __next__ из этого класса

        return iter(self.marks) # а здесь сработает __iter__ и  __next__ из класса Marks

    def __next__(self):
        if self.index >= len(self.name): # проверка на окончание имени и выход из цикла без ошибки
            raise StopIteration
        letter = self.name[self.index]
        self.index+=1
        return letter

m = Marks([2,5,9,7,1,5,6,3])
igor = Students3('Igor','Nikolai',m)
print('обход с помощью __getitem__')
for i in igor:
    print(i)
print('-'*50)














