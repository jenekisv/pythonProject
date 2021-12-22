# Домашнее задание 16

# Подключение модуля

# from minmaxsum import *  # Чтобы не указывать модуль-точка-функция в модуле, только функция в модуле.

import minmaxsum

print("Используем модуль minmaxsum.py")
print(minmaxsum)

while True:
    print("1 - Максимальное; 2 - Минимальное; 3 - Сумма; 0 - Выход")
    code = input("Введите команду: ")
    if code == "0":
        break  # Выход из модуля
    if code == "1":
        r = minmaxsum.chislomax([int(i) for i in input('Введите числа через пробел ').split()])
    elif code == "2":
        r = minmaxsum.chislomin([int(i) for i in input('Введите числа через пробел ').split()])
    elif code == "3":
        r = minmaxsum.chislosum([int(i) for i in input('Введите числа через пробел ').split()])
    print("Результат:", r)
