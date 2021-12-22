print('\n Задача БЛОК 1, Задачи 3.4.')

print('----------')

# Счёт за обед

daily_food = [0, 150, 150]


def count_food(lst: list):
    return sum([daily_food[i - 1] for i in lst])


print(count_food([1]))
print(count_food([2, 3]))

print('----------')

# Электронный попугай

import re

l = set()


def parrot(phrase):
    assert type(phrase) == str
    tempo = re.split('!, ?', phrase)
    global l
    for i in tempo:
        if i in l:
            print(i)
        else:
            l.add(i)


parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")
print()
parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")

print('----------')


# Числа в строке

def from_string_to_list(string, container):
    return container + list(map(int, string.split()))


a = [1, 2, 3]
print(from_string_to_list('1 3 99 52', a))
print()
a = [77, 'abc']
from_string_to_list('', a)
print(*a)

print('----------')


# Обмен личностями

def swap(first, second):
    first[:], second[:] = second[:], first[:]


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)
print()
first = [1, 2, 3]
second = [4, 5, 6, 7]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)

print('----------')


# Фрактальный список – 2

def defractalize(fractal):
    return [x for x in fractal if x is not fractal]


fractal = [2, 5]
fractal.append(3)
defractalize(fractal)
print(fractal)
print()
fractal = [2, 5]
fractal.append(3)
fractal.append(9)
defractalize(fractal)
print(fractal)

print('----------')


# Транспонирование

def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]
    matr[:] = res


matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)
print()
matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)

print('----------')


# Печать фрактала

def fractal_print(obj):
    print('[' + ', '.join(map(str, obj)) + ']')


fractal = [3]
fractal.append(fractal)
fractal_print(fractal)
print()
fractal = [3]
fractal.append(fractal)
fractal.append(2)
fractal_print(fractal)
