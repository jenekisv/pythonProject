print('\n Задача БЛОК 1, Задачи 2.5.')

print('----------')

# Произведение

a = []
c = 0
for i in range(int(input('Введите количество чисел в наборе: '))):
    a.append(int(input('Введите целое число из набора: ')))
n = int(input('Введите целое число, которое является или не является произведением двух каких-то чисел из набора: '))
for i in a:
    for j in a:
        if i != j and i * j == n:
            c += 1
if c == 0:
    print('НЕТ')
else:
    print('ДА')

print('----------')

# Отбор

cnt = int(input('Введите количество школьников: '))
inp = []
ok = []
for i in range(cnt):
    new_ = input('Введите фамилию школьника и его оценку через табуляцию: ')
    new_spl = new_.split()
    if new_spl[1] in ('4', '5'):
        ok.append(new_)
    inp.append(new_)
print('\n'.join(inp))
print()
print('\n'.join(ok))

print('----------')

# Сортировка по алфавиту

n = int(input('Введите количество строк: '))
a = []
for i in range(n):
    a.append(input('Введите строки: '))
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
for i in range(n):
    print(a[i])

print('----------')

# Сортировка по длине

print(*sorted([input('Введите строки: ') for _ in range(int(input('Введите количество строк: ')))], key=len), sep='\n')

print('----------')

# Напёрстки

n = int(input('Введите изначальное количество напёрстков: '))
li = [''] * n
for i in range(n):
    li[i] = input('Введите, что положено под напёрсток: ')
k = int(input('Введите количество перестановок напёрстков: '))
for i in range(k):
    x = int(input('Введите описание перестановок: '))
    tmp = [''] * x
    for j in range(x):
        tmp[j] = li[int(input()) - 1]
    li = tmp
for i in range(len(li)):
    print(li[i])

print('----------')

# Сортировка в обратном порядке

num = int(input('Введите количество чисел: '))
alf = [int(input('Вводите чисела: ')) for i in range(num)]
for i in range(num - 1):
    for j in range(num - 1 - i):
        if alf[j] < alf[j + 1]:
            alf[j], alf[j + 1] = alf[j + 1], alf[j]
[print(alf[i]) for i in range(num)]
