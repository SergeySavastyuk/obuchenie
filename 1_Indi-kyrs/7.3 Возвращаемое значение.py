""" Инструкция assert или проверка"""

"Итак, глагол assert с английского переводится как «утверждать». Утверждения в любом языке " \
"программирования — это инструмент отладки, который помогает обеспечить дальнейший поток кода в случае, " \
"когда утверждение верно."

print('Начало проверок')
assert 2 + 2 == 4
assert 2 ** 5 == 32
assert 100 < 300
assert 'HeLLo' != 'hello'
assert 'HeLLo'.upper() == 'hello'.upper()
assert [1, 2, 3] == [1, 2] + [3]
print('Конец проверок')

def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr *= i
    return pr
assert factorial(1) == 1, '1! должен быть равен 1'
assert factorial(2) == 2, '2! должен быть равен 2'
assert factorial(3) == 3, '3! должен быть равен 6'
assert factorial(4) == 24, '4! должен быть равен 24'
assert factorial(5) == 120, '5! должен быть равен 120'
print('Тесты пройдены')
print('-'*50)

# сначала создаём список дубликатов, потом преобразуем  в множество и сортируем с ключом,
# где ключ - индекс в исходном списке либо в списке дубликатов
def find_duplicate(lst):
    tmp = [i for i in lst if lst.count(i) > 1]
    return sorted(set(tmp), key=tmp.index)
find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8])
# другое решение
find_duplicate = lambda nums: list(dict.fromkeys([i for i in nums if nums.count(i) > 1]))
find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8])