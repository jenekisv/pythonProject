print('\n Задача БЛОК 1, Задачи 1.1.')

print('----------')

# "Привет, Яндекс"
print('"Привет, Яндекс!" \n"Приятно познакомиться."')

print('----------')

print('\n "Памятка начинающего программиста:"')
print('''\n 1 бит - минимальная единица информации. \n 1 байт = 8 бит. \n 1 Килобит = 1024 бита.
 1 Килобайт = 1024 байта.''')

# (1 Килобайт = ХХХХ бит.) - Рассчет в строке выполнялся непосредственно перед ее выводом и подставлялся вместо ХХХХ
bit = 8
byt = 1024
print(' 1 Килобайт =', byt * bit, 'бит.')

print('----------')

# "Гороскоп"
n = input('Введите своё Имя: ')
f = input('Введите свою Фамилию: ')
k = input('Введите своё любимое Животное: ')
z = input('Введите свой Знак по гороскопу: ')
print('\n Гороскоп для пользователя', n, f, '\n В прошлой жизни Вы были:', k, ', \n а так как Вы по гороскопу', z,
      ', \n то Вы добьетесь в жизни всего.')

print('----------')

# "Бронь билетов"
film = 'Железный Человек 2'
teatr = 'Восток'
tim = '12:00'
n = input('Вы подтверждаете Бронь билета? да\\нет: ')
if n == 'да':
    print('\n Билет на \"', film, '\" в кинотеатре \"', teatr, '\" на', tim, 'забронирован.')
else:
    print('\n Ваш заказ анулирован.')