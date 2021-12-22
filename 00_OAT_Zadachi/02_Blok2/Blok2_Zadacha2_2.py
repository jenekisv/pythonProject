print('\n Задача БЛОК 1, Задачи 2.2.')

print('----------')

# Игра в города: один раунд

city = input('Введите название города: ')
town = input('Введите название второго города: ')
if city[-1] == town[0]:
    print('ВЕРНО')
elif city[-1] == 'ь':
    if city[-2] == town[0]:
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')
else:
    print('НЕВЕРНО')

print('----------')

# Игра в города

s1 = input('Введите название города: ').lower()
while True:
    s2 = input('Введите название города: ').lower()
    if s1[-1] != s2[0]:
        print('Введён неверный города:', s2)
        break
    s1 = s2

print('----------')

# Какая-то там буква

s = input('Введите сообщение: ')
n = int(input('Введите номер буквы в слове: '))
if 0 < n <= len(s):
    print('Это буква:', s[n - 1])
else:
    print('ОШИБКА')

print('----------')

# Цезарь его знает

n = int(input('Введите шаг шифрования: '))
message = input('Введите сообщение для зашифровки: ')
for i in message:
    if not i.isalpha():
        print(i, end='')
        continue
    if 1071 >= ord(i) + n > 1071 or 1103 >= ord(i) + n > 1103:
        i = chr(ord(i) - 32)
    i = chr(ord(i) + n)
    print(i, end='')

print('----------')

# Ползём вниз

s = ".>>>VV<<V"
line = ""
i, snail_pos = 1, 0
while (i < len(s)):
    if s[i] == 'V':
        print(line[:snail_pos] + ('V' if s[0] == ' ' else s[0]) + line[(snail_pos + 1):])
        line = ' ' * snail_pos
    elif s[i] == '>':
        line += '>' if s[0] == ' ' else s[0]
        snail_pos += 1
    elif s[i] == '<':
        line = line[:snail_pos] + ('<' if s[0] == ' ' else s[0]) + line[(snail_pos + 1):]
        snail_pos -= 1
        if snail_pos < 0:
            break
    i += 1
if snail_pos >= 0:
    if line != "":
        print(line[:snail_pos] + ('O' if s[0] == ' ' else s[0]) + line[(snail_pos + 1):])
else:
    print(line)
