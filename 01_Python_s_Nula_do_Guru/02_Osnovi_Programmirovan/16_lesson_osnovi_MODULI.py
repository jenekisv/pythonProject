# Подключение модулей

# import random
# import math as m
from random import *
from math import sin, cos
import math, cmath as cm
import calc

# print(random.randint(0, 10))
# print(m.sin(1))
print(randint(0, 10))
print(sin(1))
print(cos(1))

print(math.ceil(10.3))
print(cm.log10(1000))

print("Используем наш модуль")
print(calc.x)

while True:
    print("1 - Сложение; 2 - Вычитание; 3 - Умножение; 4 - Деление; 0 - Выход")
    code = input("Введите команду: ")
    if code == "0":
        exit(0)  # Выход из программы
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if code == "1":
        r = calc.sum(a, b)
    elif code == "2":
        r = calc.sub(a, b)
    elif code == "3":
        r = calc.mult(a, b)
    elif code == "4":
        r = calc.div(a, b)
    print("Результат:", r)

# Домашнее задание

print('----------')

print("Домашнее задание в файле: 16_lesson_osnovi_MODULI_DOMASHKA.py")
