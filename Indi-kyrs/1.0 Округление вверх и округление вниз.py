"""
Функция trunc выполняет отсечение дробной части и оставляет только целую часть числа
Функция floor выполняет округление вниз до ближайшего целого числа
Функция ceil выполняет округление вверх до ближайшего целого числа
"""

import math
print(math.ceil(int(input()) / 10)) # 203->21

# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов (числа не превышают 1000).
# Выведите наименьшее число парт, которое нужно приобрести для них.
print(sum((int(input()) + 1) // 2 for _ in "___")) # 5 6 7 -> 10



# Программа получает на вход три натуральных числа L, W, H – длину, ширину и высоту офиса в метрах соответственно,
# каждое из которых не превышает 1000.
# Выведите на экран одно целое число – минимальное количество банок краски, необходимых для покраски стен в офисе.
print((lambda l, w, h: ((l * h * 2 + w * h * 2) + 15) // 16)(*map(int, input().split()))) # 8 8 2 ->4