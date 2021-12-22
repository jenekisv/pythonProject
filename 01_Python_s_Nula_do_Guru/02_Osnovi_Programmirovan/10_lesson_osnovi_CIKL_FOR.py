# Цикл for и генераторы списков

array = [1, 5, 0, -5, 2.5]
for n in array:  # Перебор массива (списка)
    print(n)

print('----------')

str = 'Python'
print(str[0])  # Вывод символа с индексом "0"

print('----------')

for s in str:  # Перебор массива (строки)
    print(s)

print('----------')

for s in str:
    if s == 'Y':  # Если в массиве строки есть символ "Y", то завершить процесс
        break
else:  # В противном случае вывести print
    print('Символа Y в строке', str, 'нет.')

print('----------')

array = list(range(2, 15))  # Конвертация range в список
print(array[2])  # Вывод элемента с индексом "2"

print('----------')

for n in array:
    print(n)  # Вывод элементов списка 'array' для переменной 'n'

print('----------')

array = [i for i in range(1, 10)]
print(array)  # Вывод переменной array от 1 до 9
array = [i * 2 for i in range(1, 10)]
print(array)  # Вывод переменной array от 1 до 9 с умнодением каждого элемента на 2
array = [i for i in range(1, 10) if i % 2 == 0]
print(array)  # Вывод переменной array, только четных чисел

# Домашнее задание

print('----------')

sps = [1, 4, 8, -7, 2.2]
print(sps)
sum = 0
for r in sps:
    sum += r
print('Сумма списка sps: ', sum)
print('Среднее арифметическое число списка sps: ', sum / 2)
