print('\n Задача БЛОК 1, Задачи 1.6.')

print('----------')

# Факториал

res = 1
n = int(input('Введите число: '))
for i in range(1, n + 1):
    res *= i
print('Факториал числа:', n, 'будет число:', res)

# Ждём потепления

i = 0.0
n = 0
while i < 22.0:
    i = float(input('Вводите максимальную дневную температуру: '))
    n += 1
print('До появления температуры, выше 22 градусов, прошло:', (n - 1) // 7, 'полных недель.')
print('----------')

# Делители

k = int(input('Введите число: '))
n = 1
r = []
while n <= k:
    if k % n == 0:
        r.append(n)
    n = n + 1
print('Делители числа', k, ':', r)
print('----------')

# Пирамида

rid = int(input('Введите высоту пирамиды: ')) - 1
chis = 1
while rid > -1:
    print(' ' * rid + '*' * chis)
    chis += 2
    rid -= 1
print('----------')

# Обратный отсчёт

import time

count = int(input('Введите число отсчёта: '))
for i in range(count, 0, -1):
    print('Осталось %d секунд' % i)
    time.sleep(1)
print('Пуск!!!')
print('----------')

# Дзета-функция Римана

n = int(input('Введите Натуральное число: '))
a = 0
p = 3.141592653589793
for i in range(1, n + 1):
    a += 1 / (i ** 2)
print('Сумма обратных квадратов:', (p ** 2) / a)
print('----------')

# Шварценеггер против Годзиллы

from fractions import Fraction  # Несократимые дроби

n = int(input('Введите количество дробинок: '))
print(sum(
    Fraction(int(input('Введите урон от дробинки числитель: ')), int(input('Введите урон от дробинки знаменатель: ')))
    for i in range(n)))