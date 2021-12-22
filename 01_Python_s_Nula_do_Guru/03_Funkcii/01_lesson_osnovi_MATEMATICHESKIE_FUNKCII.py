# Математические функции
from math import *

print(e)  # Число "Е"
print(pi)  # Число "ПИ"

print("---------")

# Тригонометрия
print(sin(1))
print(cos(1))
print(tan(1))
print(1 / tan(1))  # Котангенс

print(sin(radians(30)))  # В градусах
print(cos(radians(60)))  # В градусах

print(degrees(1))

print("---------")

print(fabs(-5))  # Убирает знак "-"
print(floor(5.9))  # Округление до наибольшего целого числа, просто отбрасывая дробную часть <
print(ceil(5.1))  # Округление до наименьшего целого числа, добавляя дробные разряды до целого числа >
print(sqrt(9))  # Извлечение квадратного корня

print("---------")

# Функция не из библиотеке (модулю) 'math'
print(round(5.333))  # Округление по правилам математики
print(round(5.9))  # Округление по правилам математики
print(round(5.339, 2))  # Округление по правилам математики до двух знаков после запятой
print(round(5 / 7, 3))  # Округление по правилам математики до трёх знаков после запятой

# Домашнее задание

print("---------")

print(round(9.4756, 2))

# Выводится с шагом в 1 градус все значения синуса угла от 0 до 180 градусов в виде: «sin(УГОЛ_В_ГРАДУСАХ) = РЕЗУЛЬТАТ»
import math

for a in range(181):
    print("sin(" + str(a) + ")=" + str(math.sin(math.radians(a))))