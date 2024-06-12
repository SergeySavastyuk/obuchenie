"""Декоратор @private делает метод приватным, то есть доступным только внутри класса,
а декоратор @protected делает метод защищенным, то есть доступным только внутри класса и его наследников.
Эти декораторы позволяют реализовать инкапсуляцию в Python и улучшить защиту данных в классах."""

# Декоратор @private позволяет сделать метод приватным, то есть доступным только внутри класса.
from accessify import private
class MyClass:
    a = 2
    b = 3
    @private
    def private_sum_ab(self):
        print(f"{self.a + self.b}")

    def public_sum_ab(self):
        self.private_sum_ab()
obj = MyClass()
obj.public_sum_ab()   # 5
obj.private_sum_ab()  # AttributeError
# Здесь мы использовали декоратор @private, чтобы сделать метод private_sum_a приватным.
# Метод public_sum_ab вызывает приватный метод private_sum_ab. Запуск метода private_sum_ab напрямую извне,
# приводит к ошибке.
# Имя метода private_sum_ab на практике лучше использовать с двумя подчёркиваниями __private_sum_ab,
# в примере без подчёркиваний, чтобы показать, что именно декоратор создал приватный метод.


# Декоратор @protected позволяет сделать метод защищённым, то есть доступным только внутри класса и его наследников,
# в отличие от обычного защищённого метода с одним подчёркиванием, который можно вызвать извне.
from accessify import protected
class MyClass:
    @protected
    def protected(self):
        print("Это защищённый метод")

    def _public(self):
        self.protected()
obj = MyClass()
obj._public()        # Это защищённый метод
obj.protected()     # AttributeError:
# Здесь мы использовали декоратор @protected, чтобы сделать метод protected защищенным. В примере мы видим,
# что защищенный метод protected, не может быть вызван напрямую, но может быть вызывать через публичный метод _public.

