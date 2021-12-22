# Множества

import random  # Определение импортирования функции random

print('----------')

print(int(random.random() * 10))  # * 10 - чтобы был вывод не только дробей, а int - вывод только целых чисел

print('----------')

print('Создание множества двумя способами:')
myset = set()  # Первый способ
print(myset)
myset = {}  # Второй способ
print(myset)

print('----------')

myset = {'1', 4, 2, 1, '1'}  # В созданном множестве, при выводе, элементы не повторяются
print(myset)

print('----------')

lister = [int(random.random() * 10) for i in range(0, 10)]  # Создаём массив с помощью random в пределах range
print(lister)
myset = set(lister)  # Преобразование массива (списка) в множество
print(myset)
b = list(myset)  # Преобразование множества в массив (список)
print(b)

# Домашнее задание

print('----------')

sps = [int(i) for i in input('Введите числа через пробел ').split()]  # Ввод чисел пользователем с клавы
print(sps)

print('----------')

listr = [int(random.random() * 100) for i in range(0, 100)]  # Создаём массив (список) из целых, случайных чисел
i = 0
while i < len(listr):
    i += 1
print(listr)  # Вывод массива случайных чисел

print('----------')

mas = set(listr)  # Преобразование массива в множество для удаления повторяющихся чисел
print(mas)

print('----------')

ls = list(mas)  # Преобразование множества в массив (ПЕРВЫЙ СПОСОБ)
print(ls)

print('----------')

for n in mas:  # Преобразование множества в массив (ВТОРОЙ СПОСОБ)
    a = list(mas)
print(a)
