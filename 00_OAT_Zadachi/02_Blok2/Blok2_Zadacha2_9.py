print('\n Задача БЛОК 1, Задачи 2.9.')

print('----------')

# Проверка связи

t = 'Раз-1 раз-2 раз-3 как-1 меня-1 слышно-1 Повторяю-1 раз-4 раз-5 раз-6 Повторяю-2'
print(*list(filter(lambda x: x.isdigit(), t)))

print('----------')

# Толковый словарь

while True:
    N = int(input('Введите количество записей в толковом словаре Васи: '))
    if 1 <= N <= 1000:
        break
    print('1≤N≤1000 !')
slvr = {k[0]: ' '.join(k[1:]) for k in
        [input('Введите слово, а затем через пробел непустое описание его значения: ').split() for i in range(N)]}
while True:
    M = int(input('Введите количество слов, которое проверит мама: '))
    if 1 <= M <= 100:
        break
    print('1≤M≤100 !')
slov = [input('Введите слова для проверки, по одному на строке: ') for i in range(M)]
[print(slvr.setdefault(i, 'Нет в словаре')) for i in slov]

print('----------')

# Карта сокровищ

num = int(input('Введите количество точек отмеченных на карте сокровищ: '))
point = []
for i in range(num):
    num, m = input(
        'Введите пары координат через пробел (целые числа не меньше нуля и не больше 1 миллиарда) : ').split()
    point.append((int(num), int(m)))
result = []
while len(point) > 0:
    same_route = []
    a = point[0][0] // 10 * 10
    b = point[0][1] // 10 * 10
    for i in range(0, len(point)):
        x = point[i][0] // 10 * 10
        y = point[i][1] // 10 * 10
        if x == a and y == b:
            same_route.append(point[i])
    result.append(same_route)
    point = list(filter(lambda p: p not in same_route, point))
quant = [len(result[i]) for i in range(len(result))]
qmax = max(quant)
print(qmax)

print('----------')

# Телефонная книга

dct = {}
for _ in range(int(input('Введите количество номеров телефонов: '))):
    val, key = input('Введите телефоны и имена их владельцев через пробел: ').split()
    if key in dct:
        dct[key].append(val)
    else:
        dct[key] = [val]

for _ in range(int(input('Введите количество запросов от Васи: '))):
    key = input('Введите запрос — это имя какого-то друга: ')
    if key in dct:
        print(*dct[key])
    else:
        print('Нет в телефонной книге')

print('----------')

# Дни рождения – 2

sp = {}
n = int(input('Введите количество Васиных одноклассников: '))
for i in range(n):
    name = input('Введите, разделённых пробелом — имя одноклассника, дня и месяца его рождения: ').split()
    if name[2] in sp:
        sp[name[2]].append([name[0], name[1]])
    else:
        sp[name[2]] = [[name[0], name[1]]]

num = int(input('Введите количество вопросов, на которое надо ответить: '))
arr = [input('Введите вопросы — это название месяца в том же формате: ') for _ in range(num)]
for word in arr:
    if word in sp:
        arr = sorted(sp[word], key=lambda x: (int(x[1]), x[0]))
        st = ''
        for x in arr:
            st += ' '.join(x) + ' '
        print(st.rstrip())
    if word not in sp:
        print()

print('----------')


# Частотный анализ – 1

def clean(line):
    return ''.join(filter(lambda x: x.isalpha(), line)).capitalize()


dict_word = {}
for _ in range(int(input('Введите количество строк в тексте: '))):
    for key in [clean(line) for line in input('Введите сам русский текст: ').split()]:
        dict_word[key] = dict_word.get(key, 0) - 1

for i, _ in (sorted(dict_word.items(), key=lambda x: x[::-1])):
    print(i)
