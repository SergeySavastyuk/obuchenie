# -*- coding: UTF-8 -*-
# Функция create_matrix должна возвращать квадратную матрицу размером size х size, на диагонали которой располагаются
# числа от 1 до size. Все остальные элементы заполнены согласно параметрам up_fill и down_fill.
def create_matrix(size:int = 3,up_fill: int = 0, down_fill:int = 0):
    return [[up_fill if row < column else (down_fill, row+1)[row == column] for column in range(size)] for row in range(size)]
print(create_matrix(size=4, up_fill=7, down_fill=9))