print('\n Задача БЛОК 1, Задачи 1.8.')

print('----------')

# Таблица деления

i = int(input('Введите количество колонок: '))
j = int(input('Введите количество строк: '))
for x in range(1, j + 1):
    print(*(y / x for y in range(1, i + 1)), sep=' ')

print('----------')

# Рисуем прямоугольник

b = int(input('Введите количество высоту (в строках): '))
a = int(input('Введите количество ширину (в знаках): '))
simb = input('Введите символ, из которого строить прямоугольник: ')
print(simb * a)
for i in range(b - 2):
    print(simb, ' ' * (a - 2), simb, sep='')
print(simb * a)

print('----------')

# Обратный отсчёт: серия пусков

for i in range(1, int(input('Введите количество пусков: ')) + 1):
    start = i
    while i:
        print(f'Осталось секунд: {i - 1}')
        i -= 1
    print(f'Пуск {start}')

print('----------')

# Логистический максимин

number = int(input('Введите количество дорог: '))
m = int(input('Введите высоту гузовика: '))
maximum = 0
road = 1
for element in range(number):
    tunnel = int(input('Введите количество тунелей дороги: '))
    #    m = int(input('Введите высоту гузовика: '))
    for element_2 in range(tunnel):
        height = int(input('Введите максимально допустимую высоту грузовика этих тунелей: '))
        if m > height:
            m = height
    if maximum < m:
        maximum = m
        road = element + 1
print('Подходит:', road, 'дорога для грузовика высотой:', maximum)

print('----------')

# Простые числа на миллион долларов

num = int(input('Введите одно натуральное число: '))
lst = []
k = 0
for i in range(2, num):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
for x in lst:
    print('Введено:', num, 'Простое число, меньшие введённого числа: ', x)

print('----------')

# Начинающий фермер

credit = int(input('Выделяемая субсидия: '))
livestock = int(input('Количество голов: '))
for b in range(1, min(livestock, credit // 20) + 1):
    for k in range(0, min(livestock, credit // 10) + 1):
        for t in range(0, min(livestock, credit // 5) + 1):
            if b * 20 + k * 10 + t * 5 == credit:
                if b + k + t == livestock:
                    print('Возможно купить быков:', b, 'коров:', k, 'телят:', t)
