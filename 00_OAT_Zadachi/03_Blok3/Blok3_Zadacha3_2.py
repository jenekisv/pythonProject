print('\n Задача БЛОК 1, Задачи 3.2.')

print('----------')


# Мелочь оставь себе

def take_large_banknotes(arr):
    return list(filter(lambda x: x > 10, arr))


print(*take_large_banknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]))

print('----------')


# Месяц/Month

def month_name(num, lang):
    en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
          'october', 'november', 'december']
    ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
          'октябрь', 'ноябрь', 'декабрь']
    if lang == 'en':
        return en[num - 1]
    else:
        return ru[num - 1]


print(month_name(3, "en"))
print(month_name(3, "ru"))

print('----------')


# Среднее значение – 2

def average(arr):
    print(0 if not arr else sum(arr) / len(arr))


print(average([1, 2, 3, 4, 5]))
print(average([-5, 2]))

print('----------')


# Секретные материалы

def print_document(pages):
    a = []
    for i in pages:
        if "Секрет" not in i:
            a.append(i)
        if "Секрет" in i:
            a.append("Дальнейшие материалы засекречены")
            break
    print(*a, sep='\n')
    if "Секрет" not in pages:
        print('Напечатано без купюр')


print_document(["Обычная страница", "И еще страница", "Секретно Вот этот вот текст не показывать", "Никому", "Никогда"])
print()
print_document(["Пустой трёп", "который", "никому не интересен"])

print('----------')


# Ход конём

def t2c(f):
    a = f[:1]
    b = f[1:]
    r = int(b)
    c = 'ABCDEFGH'.find(a) + 1
    return c, r


def c2t(k):
    (c, r) = k
    return 'ABCDEFGH'[c - 1] + str(r)


def possible_turns(f):
    (c, r) = t2c(f)
    tmp = []
    tmp.append((c + 2, r + 1))
    tmp.append((c + 2, r - 1))
    tmp.append((c - 2, r + 1))
    tmp.append((c - 2, r - 1))
    tmp.append((c + 1, r + 2))
    tmp.append((c - 1, r + 2))
    tmp.append((c + 1, r - 2))
    tmp.append((c - 1, r - 2))
    res = []
    for (a, b) in tmp:
        if (a > 0) & (b > 0) & (a <= 8) & (b <= 8):
            res += [c2t((a, b))]
    return sorted(res)


print(possible_turns("B1"))
print()
print(str(possible_turns("H8")))

print('----------')


# Опоздание

def late(now, classes, bus):
    now = now.split(':')
    now[0], now[-1] = int(now[0]), int(now[-1])
    _now = now[0] * 60 + now[-1]
    classes = classes.split(':')
    classes[0], classes[-1] = int(classes[0]), int(classes[-1])
    _classes = (classes[0] * 60 + classes[-1]) - _now
    _answ = []
    for time in bus:
        if _classes - 15 >= time >= 5:
            _answ.append(time)
    if _answ == []:
        return 'Опоздание'
    else:
        return 'Выйти через ' + str(max(_answ) - 5) + ' минут(ы)'


print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
print(late('9:20', '9:35', [4, 25, 30]))

print('----------')


# Поиски возвышенного

def find_mountain(heightsMap):
    row = -1
    maxValue = 0
    for i in heightsMap:
        if max(i) > maxValue:
            maxValue = max(i)
    for i in heightsMap:
        row += 1
        column = -1
        for j in i:
            column += 1
            if j == maxValue:
                return row, column


a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
print(find_mountain(a))
print()
a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])
