import random

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 1, 11] * 4
random.shuffle(numbers)

while True:
    answer = input('желаете ли сыграть в БлекДжек (да-1, нет -0)?: ')
    if answer == '1':
        count = 0
        bank = 0
        current2 = 0
        while True:
            choice = input('желаете ли взять карту (да-1, нет -0)?: ')
            # действия игрока
            if choice == '1':
                current = numbers.pop()
                print(f'Вы взяли карту {current}')
                count += current
                print(f'текущее значение ваших карт {count}')
                if count == 21:
                    print('ВЫ ВЫИГРАЛИ!!!!')
                if count < 21:
                    continue
                if count > 21:
                    print(f'у вас перебор - вы проиграли')
                print('-'*100)
                break
            # действия банка
            elif choice == '0':
                while True:
                    current2 = numbers.pop()
                    print(f'банк взял карту {current2}')
                    bank += current2
                    if bank < 18:
                        continue
                    if bank == 21:
                        print(f'у банка {bank}, а у вас {count} - вы проиграли')
                    if bank > 21:
                        print(f'у банка {bank}, а у вас {count} - ВЫ ВЫИГРАЛИ!!!!')
                    if 18 <= bank < 21 and count > bank:
                        print(f'у банка {bank}, а у вас {count} - ВЫ ВЫИГРАЛИ!!!!')
                    if 18 <= bank < 21 and count < bank:
                        print(f'у банка {bank}, а у вас {count} - вы проиграли')
                    if 18 <= bank < 21 and count == bank:
                        print(f'у банка и у вас поровну по {bank} - поэтому ничья')
                    print('-'*100)
                    break
                break
    else:
        print('на нет и суда нет, всего доброго')
        break
