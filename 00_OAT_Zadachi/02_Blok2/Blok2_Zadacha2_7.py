print('\n Задача БЛОК 1, Задачи 2.7.')

print('----------')

# Комментарии в программе

a = []
for i in range(int(input('Введите количество строк программы со знаком #: ')[1:])):
    b = input('Введите строку программы: ')
    if '#' in b.split():
        f = b.index('#')
        b = ''.join(b[:f])
    a.append(b)
for i in range(len(a)):
    print(a[i])

print('----------')

# Польский калькулятор

s = input('Введите строку, содержащая разделённые пробелами целые числа и знаки операций +, -, *: ')
stack = []
for i in s.split(' '):
    try:
        stack.append(int(i))
    except ValueError:
        if i == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif i == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        else:
            raise NotImplementedError
    print(stack)

assert (len(stack) == 1)
print(stack[0])

print('----------')

# Маленький частотный анализ

string = ''.join(input('Введите строку: ').lower().split())
letter = list()
big = 0
for x in string:
    letter.append(x)
letter.sort()
for y in letter:
    if letter.count(y) > big:
        big = letter.count(y)
        let = y
print(let)

print('----------')

# Знаков без пробелов

s = input('Введите строку: ')
c = 0
for a in s:
    if a != ' ' and a != '\t':
        c += 1
print(c)

print('----------')

# Пристраиваемся в очередь

n = int(input('Введите количество событий: '))
q = []
for _ in range(n):
    s = input('Введите событие: ').split()
    if 'встал' in s[1]:
        q.append(s[0])
    elif s[0] == 'Привет,':
        q.insert(q.index(s[1][:-1]) + 1, s[2])
    elif s[1] == 'хватит':
        q.remove(s[0][:-1])
print(*q, sep='\n')
