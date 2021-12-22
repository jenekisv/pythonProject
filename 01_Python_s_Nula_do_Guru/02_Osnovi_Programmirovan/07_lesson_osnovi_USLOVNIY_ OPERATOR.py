# Условный оператор

print('Введите 0, 1 или 2:')
a = int(input())
if a == 0:
    print('Вы ввели ноль.')
    if 5 == 5:
        print('5 = 5')
    else:
        print('5 != 5')
elif a == 1:
    print('Вы ввели один.')
elif a == 2:
    print('Вы ввели два.')
else:
    print('Вы ввели не корректное число.')

cond = a == 0 or a == 1 or a == 2  # Альтернативная запись
print()  # True / False

print(cond)
if cond:
    x = 1
else:
    x = 0
print('x =', x)

x == 1 if cond else 0  # Альтернативная запись
print('x =', x)

# Домашнее задание
a = int(input('Введите первое число: '))
b = int(input('Введите второе число ( не "0"): '))
c = a / b
if b == 0:
    print('Не корректное второе число.')
else:
    print(a, '/', b, '=', c)
