print('\n Задача БЛОК 1, Задачи 2.6.')

print('----------')

# Горизонтальная диаграмма

a = input('Введите несколько натуральных чисел разделённых пробелами: ').split()
for i in a:
    print('*' * int(i))

print('----------')

# /etc/passwd ???

a = []
b = []
c = []
d = []
while True:
    d.clear()
    e = input()
    if e == '':
        break
    else:
        d = e.split(':')
        f = d[4].split(',')
        b.append(d[0])
        a.append(f[0])
        c.append(d[1])
g = input().split(';')
for i in range(len(c)):
    if c[i] in g:
        print('To:', b[i])
    print(a[i], ', ваш пароль слишком простой, смените его.', sep='')

print('----------')

# Только без лука!

print(', '.join(filter(lambda x: 'лук' not in x, [input('Введите пункты рецепта: ') for _ in
                                                  range(int(input('Введите количество пунктов рецепта: ')))])))

print('----------')

# Вертикальная диаграмма

n = list(map(int, input('Введите несколько натуральных чисел: ').split()))
xmax = len(n)
ymax = max(n)
print('*' * (xmax + 2))
print('*' + ' ' * xmax + '*')
for y in range(1, ymax + 1):
    print(end='*')
    for nk in n:
        if nk >= ymax - y + 1:
            print(end='*')
        else:
            print(end=' ')
    print('*')

print('----------')

# Джек-Победитель-Великанов

n = int(input('Введите количество титулов: '))
dignity = []
while n:
    temp = []
    while True:
        text = input('Введите название титула, конец титула отметьте * на отдельной строке: ')
        if text == '*':
            break
        else:
            temp += text.strip().split()
    n -= 1
    dignity.append('-'.join(temp))
    temp = []
print(', '.join(dignity[::-1]))
