
""" Магические методы __getitem__ , __setitem__ и __delitem__ Обращение по индексу к экземпляру"""
''' по умолчанию любые классы не поддерживают индексирование '''

class Vector:
    def  __init__(self,*args):
        self.values = list(args) # вместо списка можно использовать словарь

    def __repr__(self):
        return str(self.values)  # превращает наш объект в читаемую строку

    ''' добавим классу поведение позволяющее индексировать объект '''
    def __getitem__(self, item):  #  переменная item подразумевает собой номер индекса [0],[1] и т.д
        if -len(self.values)<=item<len(self.values): # сделаем проверку, чтобы индекс вход в доступный диапазон
            return self.values[item]
        else:
            raise IndexError('индекс за границами коллекции')

    ''' добавим классу поведение позволяющее ИЗМЕНЯТЬ индексированный объект '''
    def __setitem__(self, key, value):
        if -len(self.values) <= key < len(self.values):
            self.values[key]=value
        # """ сделаем разряженный список, т.е. до нужного индекса будут проставлены нули"""
        elif key>len(self.values):
            diff = key-len(self.values) # найдём недостающее количество
            self.values.extend([0]*diff) # расширим коллекцию (extend()-метод расширяет один список за счёт другого)
            self.values[key-1] = value
        else:
            raise IndexError('индекс за границами коллекции')

    ''' добавим классу поведение позволяющее УДАЛИТЬ элемент из индексированного объекта '''
    def __delitem__(self, key):
        if -len(self.values) <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('индекс за границами коллекции')

v1 = Vector(1,2,78,'sdfg')
print(f'наш список - {v1}')
print(v1[0]) # поскольку мы определили метод __getitem__, то он автоматически сработал когда указали индекс
print(v1[-1]) #sdfg
print('-'*20)
print('добавим поведение изменения индексированного объекта')
print(f'первоначальное значение {v1[1]}')
v1[1]=10
print(f'новое значение {v1[1]}')
print('-'*20)
print('добавим поведение удаляющее элемент')
print(f'наш список - {v1}')
del v1[-1]
print(f'наш список после удаления- {v1}')
print('-'*20)
print('добавим возможность разряженного списка')
print(f'наш список - {v1}')
v1[8] = 999
print(f'наш список после добавления - {v1}')


