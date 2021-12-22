# функции Работы с датой и временем

from datetime import *
from time import *

start = time()

print(date.today())  # Вывод даты
print(datetime.today())  # Вывод даты и времени

d = date(2025, 7, 15)  # Присвоить переменной дату
print(d)

dt = datetime(2025, 7, 15, 12, 50, 30)  # Присвоить переменной дату и время
print(dt)

# Выбрать из указанной переменной (год, месяц и т.д.)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print("----------")

print(dt.strftime("%Y.%m.%d %H:%M:%S"))  # Функция получения отформатированной даты и время из переменной
print(dt.strftime("%Y/%m/%d %H:%M.%S"))  # Функция получения отформатированной даты и время из переменной

print("----------")

print(time())

dt = datetime.fromtimestamp(29116800)  # Функция получения даты и время из "секунд" (отсчет секунд с 01.01.1970)
# dt = datetime.fromtimestamp(time())  # Функция получения даты и время из time()
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print(dt.timestamp())  # Функция получения секунд из time()

i = 0
while i < 1000000:
    i += 1

print("Время выполнения скрипта:", time() - start, 'сек.')

# Домашнее задание

print('----------')

# Вариант 1
import datetime as DT

text = str(input('Введите дату своего рождения ГГГГММДД (без пробелов): '))
date = DT.datetime.strptime(text, '%Y%m%d').date()
print(date)  # 2018-08-19
d = date.today() - date  # Дней прожил
print('Вы прожили:', d)

# Вариант 2
import time

dat = str(input('Введите дату своего рождения ГГГГММДД (без пробелов): '))
dt1 = time.strptime(dat, '%Y%m%d')
dt2 = time.strftime('%Y.%m.%d', dt1)  # -> '2018-08-19'
print(dt2)
