print('\n Задача БЛОК 1, Задачи 1.4.')

print('----------')

# "Скидки"
itog = 0
print('\n Вводите цены. Для остановки введите "-1"')
vvod = float(input('\n Введите цену: '))
while vvod > 0:
    if vvod >= 1000:
        itog += vvod - (vvod / 100 * 5)
        print('\n Сумма к оплате (скидка 5 %): ', round(float(itog), 2))
        vvod = float(input('\n Введите цену: '))
    else:
        itog += vvod
        print('\n Сумма к оплате: ', round(float(itog), 2))
        vvod = float(input('\n Введите цену: '))

print('----------')

# "Password123"
a = input('\n Введите Новый Пароль: ')
b = input('\n Повторите Новый Пароль: ')
if len(str(a)) <= 7:
    print('\n У Вас короткий пароль')
elif a != b:
    print('\n Пароли не совподают')
else:
    print('\n Ok')

print('----------')

# "Учитель"
ostalos = int(input('\n У учителя всего было монет: '))
vvod = int(input('\n Введите остаток монет, столько, сколько и было: '))
bedn = 7
while vvod > 8:
    if vvod >= 8:
        ostalos -= (vvod // 8) * bedn
        print('\n Было монет: ', vvod, '\n Осталось монет: ', ostalos)
        vvod = ostalos
    else:
        Print()
print('\n У учителя всего осталось монет: ', ostalos)

print('----------')

# "Таких берут в космонавты"
a = input('Вводите рост космонавтов (для завершения ввода > введите "!": ')
b = 0
min = 190
max = 150

while a != '!':
    a = int(a)
    if a >= 150 and a <= 190:
        b += 1
        if a >= max:
            max = a
        if a <= min:
            min = a
    a = input('Вводите рост космонавтов (для завершения ввода > введите "!": ')
print('Подобрано в космонавты:', b)
print('Минимальный рост космонавта:', min, 'Максимальный рост космонавта:', max)

print('----------')

# "1024 и все-все-все"

k = int(input('Введите натуральное число: '))
i = 0
while (k % 2 == 0):
    k = k / 2
    i += 1
if k == 1:
    print('Это число равно 2 в степени: ', i)
else:
    print('НЕТ, не является степенью двойки')

print('----------')

# "Ищем клад — 1"
minshag = 0
print('Введите координаты ниже.')
x = int(input('Коотдинаты по оси Х: '))
y = int(input('Коотдинаты по оси У: '))
x1 = 0
y1 = 0
if x == x1 and y == y1:
    print('Клад по координатам:', x, y, 'Вы находимся по координатам:', x1, y1)
    print('Вы уже на месте.)))')
    print('Было выполнено шагов: ', minshag, '.')
    exit(0)
napravlen = input('Укажите направление (вперёд, направо, налево, разворот или стоп - для выхода): ')
while x != 0 and y != 0:
    minshag += 1
    if napravlen == 'стоп':
        print('Выход. Приложение закрыто.')
        exit(0)
    elif napravlen == 'вперёд':
        steps = int(input('Укажите количество шагов: '))
        y1 += steps
        if x == x1 and y == y1:
            print('Клад по координатам:', x, y, 'Вы находимся по координатам:', x1, y1)
            print('Вы уже на месте.)))')
            print('Было выполнено шагов: ', minshag, '.')
            break
    elif napravlen == 'направо':
        steps = int(input('Укажите количество шагов: '))
        x1 += steps
        if x == x1 and y == y1:
            print('Клад по координатам:', x, y, 'Вы находимся по координатам:', x1, y1)
            print('Вы уже на месте.)))')
            print('Было выполнено шагов: ', minshag, '.')
            break
    elif napravlen == 'налево':
        steps = int(input('Укажите количество шагов: '))
        x1 -= steps
        if x == x1 and y == y1:
            print('Клад по координатам:', x, y, 'Вы находимся по координатам:', x1, y1)
            print('Вы уже на месте.)))')
            print('Было выполнено шагов: ', minshag, '.')
            break
    elif napravlen == 'разворот':
        steps = int(input('Укажите количество шагов: '))
        y1 -= steps
        if x == x1 and y == y1:
            print('Клад по координатам:', x, y, 'Вы находимся по координатам:', x1, y1)
            print('Вы уже на месте.)))')
            print('Было выполнено шагов: ', minshag, '.')
            break
    napravlen = input('Укажите направление (вперёд, направо, налево, разворот или стоп - для выхода): ')
