print('\n Задача БЛОК 1, Задачи 2.8.')

print('----------')

# Считать и вывести таблицу

rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))
table = [input('Введите слово для таблицы: ') for _ in range(rows * cols)]
for i in range(0, rows + cols, cols):
    print(*table[i:i + cols])

print('----------')

# Считать и вывести таблицу — 2

a = []
sta, stb = int(input('Введите количество строк: ')), int(input('Введите количество столбцов: '))
for i in range(sta):
    b = []
    for j in range(stb):
        b.append(input('Введите слово для таблицы: '))
    a.append(b)
for i in a:
    for j in range(stb - 1):
        print(i[j], end='\t')
    print(i[-1])
print()
for i in range(stb):
    for j in range(sta - 1):
        print(a[j][i], end='\t')
    print(a[-1][i])

print('----------')

# CSV

string_list = [input('Введите текст в строку: ').split(",") for _ in
               range(int(input('Введите количество рядов таблицы: ')))]
for _ in range(int(input('Введите число элементов таблицы, которые нужно будет вывести: '))):
    string_number, word_number = [int(i) for i in
                                  input('Введите разделённые запятой координаты элементов таблицы: ').split(",")]
    print(string_list[string_number][word_number])

print('----------')

# bf--

s = [0 for i in range(30001)]
pos = 0
a = input('Введите символы: ')
print(a)
i = 0
while i < len(a):
    if a[i] == ">":
        pos = pos + 1
    elif a[i] == "<":
        pos = pos - 1
    elif a[i] == ".":
        print(s[pos])
    elif a[i] == "+":
        s[pos] = s[pos] + 1
        if s[pos] > 255:
            s[pos] = 0
    elif a[i] == "-":
        s[pos] = s[pos] - 1
        if s[pos] < 0:
            s[pos] = 255
    elif a[i] == '[':
        if s[pos] == 0:
            j = i + 1
            c = 1
            while True:
                if a[j] == '[':
                    c += 1
                if a[j] == ']':
                    c -= 1
                if c == 0:
                    i = j
                    break
                j += 1
    elif a[i] == ']':
        c = -1
        j = i - 1
        while True:
            if a[j] == ']':
                c -= 1
            if a[j] == '[':
                c += 1
            if c == 0:
                i = j - 1
                break
            j -= 1
    i += 1

print('----------')

# Сборка текста

a = (map(int, input('Введите строку, содержащую номера слов через пробел: ').split()))
b = list(map(str.lower, input('Введите строку, содержащую сами слова, записанные через пробел: ').split()))
print(' '.join([b[i - 1] for i in a]).capitalize())

print('----------')

# Бактериям — бой!

n = int(input('Введите натуральное число, размер квадратного поля из клеток: '))
s = [([0] * n) for i in range(n)]
for i in range(n):
    for j in range(n):
        s[i][j] = int(input('Введите количество бактерий в каждой клетке: '))
m = int(input('Введите количество капель антибиотика: '))
for i in range(m):
    b = int(input('Введите координаты клеток: '))
    a = int(input('Введите номер ряда: '))
    if s[a][b] >= 8:
        s[a][b] -= 8
    else:
        s[a][b] = 0
    if a > 0:
        if s[a - 1][b] >= 4:
            s[a - 1][b] -= 4
        else:
            s[a - 1][b] = 0
        if b > 0:
            if s[a - 1][b - 1] >= 4:
                s[a - 1][b - 1] -= 4
            else:
                s[a - 1][b - 1] = 0
        if b < (n - 1):
            if s[a - 1][b + 1] >= 4:
                s[a - 1][b + 1] -= 4
            else:
                s[a - 1][b + 1] = 0
    if a < (n - 1):
        if s[a + 1][b] >= 4:
            s[a + 1][b] -= 4
        else:
            s[a + 1][b] = 0
        if b > 0:
            if s[a + 1][b - 1] >= 4:
                s[a + 1][b - 1] -= 4
            else:
                s[a + 1][b - 1] = 0
        if b < (n - 1):
            if s[a + 1][b + 1] >= 4:
                s[a + 1][b + 1] -= 4
            else:
                s[a + 1][b + 1] = 0
    if b > 0:
        if s[a][b - 1] >= 4:
            s[a][b - 1] -= 4
        else:
            s[a][b - 1] = 0
    if b < n - 1:
        if s[a][b + 1] >= 4:
            s[a][b + 1] -= 4
        else:
            s[a][b + 1] = 0
for i in range(n):
    for j in range(n):
        print(s[i][j], end=' ')
    print()
