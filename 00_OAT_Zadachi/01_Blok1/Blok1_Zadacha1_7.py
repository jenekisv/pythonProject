print('\n Задача БЛОК 1, Задачи 1.7.')

print('----------')

# 1984

e = True
o = False
num = int(input('Введите натуральное число (количество запросов): '))
for i in range(num):
    w = input('Введите запрос ("С кем война?" или "С кем мир?"): ')
    if w == 'С кем война?':
        if e:
            print('Евразия')
        else:
            print('Остазия')
    elif w == 'С кем мир?':
        if not o:
            print('Остазия')
        else:
            print('Евразия')
    else:
        e, o = o, e
print('----------')

# Найди кота (break)

nol = int(input('Введите натуральное число: '))
for i in range(nol):
    txt = input('Введите слово: ')
    if txt.lower().find('кот') >= 0:
        print('МЯУ')
        break
else:
    print('НЕТ')
print('----------')

# Найди кота — 2 (break)

flag = False
string = input('Введите строки, для остановки введите "СТОП": ')
cout = 1
number = 0
while string != 'СТОП':
    if 'Кот' in string or 'кот' in string:
        flag = True
        number = cout
        break
    else:
        flag = False
    cout = cout + 1
    string = input('Введите слово: ')
if flag:
    print(number)
else:
    print(-1)
print('----------')

# Найди кота — 3

word = ''
n = 0
cat = -1
i = 1
while word != 'СТОП':
    word = input('Введите строки, для остановки введите "СТОП": ')
    if 'Кот' in word or 'кот' in word:
        n += 1
    if ('Кот' in word or 'кот' in word) and cat == -1:
        cat = i
    i += 1
print('Номер слова в строке:', n, 'Номер строки:', cat)
print('----------')

# Биржевой робот

price1 = int(input('Введите начальная цена акции: '))
price2 = int(input('Введите цену покупки акции, для прекращения ввода "0": '))
in_stock = False
while price2 != 0:
    if in_stock == False:
        if price1 < price2:
            inprice = price2
            in_stock = True
    if in_stock == True:
        if price1 > price2:
            outprice = price2
            break
    price1 = price2
    price2 = int(input('Введите изменение стоимости акции, для прекращения ввода "0": '))
print('\nЦена покупки акции:', inprice, 'Цена продажи акции:', outprice, 'Выгода:', outprice - inprice)

print('----------')

# Школа танцев

num = int(input('Введите число, запас терпения учителя: '))
onetwo = ['раз', 'два', 'три', 'четыре']
jum = 0
while num > 0:
    for i in range(4):
        word = input('Вводите отсчёт (раз, два, три или четыре): ')
        if word != onetwo[i]:
            print('Правильных отсчётов было', jum, ', но теперь вы ошиблись.')
            jum = 0
            num -= 1
            break
        jum += 1
print('На сегодня хватит.')
print('----------')

# Проверка блокчейна

n = int(input('Введите количество блоков: '))
p = 0
bad = - 1
for i in range(n):
    b = int(input('Введите число: '))
    h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
    t = ((m + r + p) * 37) % 256
    if t != h or h >= 100:
        bad = i
        break
    p = h
print('\nРезультат проверки блоков ("-1" всё верно, "0" ошибка блока, его номер).', bad)
