print('\n Задача БЛОК 1, Задачи 2.3.')

print('----------')

# Быки и коровы

s1 = 'питон'
s2 = 'пилот'
bulls = 0
cows = 0
for i in set(s1) & set(s2):
    if s1.index(i) == s2.index(i):
        bulls += 1
    else:
        cows += 1
print('Быки:', bulls, 'Коровы:', cows)

print('----------')

# Шах и мат, программисты

n = int(input('Введите число не от 1 до 8: '))
a = []
s = "ABCDEFGHI"
if n < 10:
    a = [[j + 1 for j in range(9)] for i in range(9)]
for i in range(n - 1, -1, -1):
    for j in range(n):
        print(s[j] + str(a[j][i]), end=' ')
    print()

print('----------')

# Розенкранц и Гильденстерн меняют профессию

s = input('Введите произвольно "р" - решко и "о" - орёл: ')
maxx = 0
temp = 0
for i in s:
    if i == 'о':
        temp += 1
        if temp > maxx:
            maxx = temp
    else:
        temp = 0
print('Максимальное количество выпавших орлов:', maxx)

print('----------')


# Фильтр

def filter_(line):
    for z, x in enumerate(line):
        if x == '#':
            return ''
        elif x != '%':
            return line[z:]


for _ in range(int(input('Введите строки для фильтрации: '))):
    print('\n', filter_(input()))

print('----------')

# Минификатор

n = int(input('Введите количество строк в программе, далее саму программу: '))
mark = False
slash = False
char = 0
result = []
for i in range(n):
    string = input()
    while string[char] == " ":
        result.append(" ")
        char += 1
    for i2 in range(char, len(string)):
        if not slash:
            if string[i2] == "'":
                result.append(string[i2])
                mark = not mark
            elif string[i2] == "\\":
                result.append(string[i2])
                slash = True
            elif string[i2] == "#":
                if mark:
                    result.append(string[i2])
                else:
                    break
            elif string[i2] == " ":
                if mark:
                    result.append(string[i2])
                else:
                    if i2 + 1 != len(string):
                        if string[i2 + 1] == " ":
                            result.append("")
                        else:
                            result.append(string[i2])
            else:
                result.append(string[i2])
        else:
            slash = False
            result.append(string[i2])
    print("".join(result))
    result = []
    mark = False
    slash = False
    char = 0
