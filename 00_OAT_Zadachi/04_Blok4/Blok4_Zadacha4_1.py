print('\n Задача БЛОК 4, Задачи 4.1.')

print('----------')

# Выбор тайного друга

# Иван Иванов
# Саша Самойлов
# Юля Северная


group = []
x1 = 1
countStudents = int(input("Введите количество друзей: "))

for times in range(0, countStudents):
    students = input("Введите имена и фамилии друзей:")
    group.append(students)

for main in range(0, len(group)):
    if main == len(group) - 1:
        print(group[main], ' - ', group[0])
    else:
        print(group[main], ' - ', group[x1])
        x1 += 1

print('----------')

# Генератор визуально различимых паролей (базовый)

from random import sample
import string

symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'


def generate_password(m):
    return ''.join(sample(symbols, m))


def main(n, m):
    a = set()
    while len(a) < n:
        a.add(generate_password(m))
    return a


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")