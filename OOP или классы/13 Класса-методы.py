
"Классовые методы (class method) и статические методы (static method)"

class Example:
    a = 'red'

    def hello(self):
        print('hello')

    @staticmethod  # статический метод это метод к которому можно обратиться не только через класс, но и через экземпляр
    # так же он нужен, чтобы не выносить функцию из класса
    def static_hello():
        print('static_hello')

    @classmethod  # такие методы нужны когда обработка нужна не над экземплярами, а над целым классом вместе
    def class_hello(cls): # в cls автоматически сохраняется название нашего класса, со всеми аттрибутами и методами
        print(f'class_hello {cls}')
        print(cls.a)

a = Example()
a.hello()
a.static_hello()
Example.static_hello()
print('-'*60)
a.class_hello()
Example.class_hello()









