print('\n Задача БЛОК 1, Задачи 1.5.')

print('----------')

# "Ним-пасьянс"
a = int(input('Введите количество камней в куче: '))
while a != 0:
    c = int(input('Сколько камней забрать: '))
    if a >= c:
        a -= c
        print('Осталось камней в куче:', a)
    elif a == 0:
        print('В куче осталось:', a, 'Конец игры.')
        break
    else:
        print('Не корректно,в куче осталось:', a, 'камней, нельзя взять больше камней, чем есть в куче.')

print('----------')

# Псевдоним-пасьянс
a = int(input('Введите количество камней в куче: '))
b = 0
while a != 0:
    c = int(input('\nСколько камней забрать (не больше трёх камней): '))
    if c <= 3 and c <= a:
        a -= c
        print('Отлично. Осталось камней в куче:', a)
    else:
        print('Ошибка, вы ввели более трёх или в куче меньше камней, повторите ввод. Осталось камней в куче:', a)

print('----------')

# Фибоначчи
n = int(input('Введите натуральное число: '))
print()
if n == 0:
    print('\nКоличество циклов Фибо менее одного.')
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        print(a, '+', b)
        a, b = b, a + b
    print(a, '+', b)
    print('\nВыполнено:', n, 'циклов (итераций).')

print('----------')

# Остров невезения
d = int(input('Введите день рождения: '))
m = int(input('Введите месяц рождения: ')) - 2
y = int(input('Введите год рождения: '))
if m < 1:
    m = m + 12
    y = y - 1
c = y // 100  # Количество столетий
y = y % 100  # Год в столетии
n = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7  # День недели
if n == 1:
    n = '1, Понедельник.'
if n == 2:
    n = '2, Вторник.'
if n == 3:
    n = '3, Среда.'
if n == 4:
    n = '4, Четверг.'
if n == 5:
    n = '5, Пятница.'
if n == 6:
    n = '6, Суббота.'
if n == 0:
    n = '0, Воскресенье.'
print('День недели:', n)

print('----------')

# "Цирк, цирк, цирк!"
n = int(input('Введите начальное количество камней: '))
kshag = 0
while n > 1:
    kshag += 1 + n % 2
    n //= 2
print('Необходимое количество шагов: ', kshag)

print('----------')

# "Ним2-пасьянс"
a = int(input('\nВведите количество камней в 1-ой куче: '))
b = int(input('Введите количество камней в 2-ой куче: '))
while a != 0 or b != 0:
    n = int(input('\nУкажите цифрами, какая куча (1 или 2): '))
    c = int(input('Сколько камней забрать: '))
    if n == 1:
        if a >= c:
            a -= c
            print('Осталось камней в 1-ой куче:', a, ', во 2-ой куче:', b, '.')
        else:
            print('\nНельзя взять больше камней, чем есть в куче.')
            print('Осталось камней в 1-ой куче:', a, ', во 2-ой куче:', b, '.')
    if n == 2:
        if b >= c:
            b -= c
            print('Осталось камней в 1-ой куче:', a, ', во 2-ой куче:', b, '.')
        else:
            print('\nНельзя взять больше камней, чем есть в куче.')
            print('Осталось камней в 1-ой куче:', a, ', во 2-ой куче:', b, '.')
else:
    print('Игра закончена.')
    print('Осталось камней в 1-ой куче:', a, ', во 2-ой куче:', b, '.')
