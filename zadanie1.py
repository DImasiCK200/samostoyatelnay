n = int(input())
s1 = input()

print('Ключ действия:', str(n) + s1)

if s1 == 'usr':
    print('Подтвердите свой id-номер')
    n1 = int(input())
    if n1 == n:
        print('Пользователь подтверждён')
    else:
        print('Неверный id-номер')

if s1 == 'clc':
    print('Введите три любые числа:')
    x1 = float(input())
    x2 = float(input())
    x3 = float(input())
    print('Произведение модулей = ', abs(x1 * x2 * x3))
    sumx = x1 + x2 + x3
    print('Сумма чисел = ', sumx)
    maxx = max(x1, x2, x3)
    minx = min(x1, x2, x3)
    print('Наибольшее = ', maxx)
    print('Наименьшее = ', minx)
    print('Деление = ', maxx / minx)
    print('Вычитание = ', maxx - minx - (sumx - maxx - minx))

if s1 == 'adm':
    print('Введите строку:')
    s = input()
    lens = len(s)
    if (lens >= 5 and s.count('.exe') >= 1) or (s.count('.cmd') >= 1):
        print('Исполняемое действие')
    else:
        print('Неисполняемое действие')
