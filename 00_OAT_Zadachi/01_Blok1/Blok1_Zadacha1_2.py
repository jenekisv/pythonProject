print('\n Задача БЛОК 1, Задачи 1.2.')

print('----------')

# "Python"
lst = 'python'
if lst == 'python':
    print('\n ДА.')
else:
    print('\n НЕТ.')

print('----------')

# "Да или Нет"
a = 'нет'
b = 'нет'
if a == 'да' and b == 'да' or a == 'нет' and b == 'нет':
    print('\n ВЕРНО.')
else:
    print('\n НЕ ВЕРНО.')

print('----------')

# "Ёлочка, гори!"
a = 'Раз'
b = 'Два'
c = 'Три'
if a == 'Раз' and b == 'Два' and c == 'Три':
    print('\n ГОРИ.')
else:
    print('\n НЕ ГОРИ.')

print('----------')

# "Ёлочка 2"
a = 'Раз'
b = 'Два'
c = 'Три'
if a == 'Раз' and b == 'Два' and c == 'Три' or a == '1' and b == '2' and c == '3':
    print('\n ГОРИ.')
else:
    print('\n НЕ ГОРИ.')

print('----------')

# "Ёлочка 3"
a = 'Один'
b = 'Два'
c = 'Три'
if a == 'Раз' and b == 'Два' and c == 'Три' or a == '1' and b == '2' and c == '3' or a == 'Один' and b == 'Два' and \
        c == 'Три':  # Обратный слэш при переносе - обязателен
    print('\n ГОРИ.')
else:
    print('\n НЕ ГОРИ.')

print('----------')

# "Регистрация Почты"
nik = 'evgen'
mail = 'evgen@mail.ru'
indexn = nik.find('@')
indexm = mail.find('@')
if indexn >= 0:
    print('\n Не коректный Логин.')
elif indexm == -1:
    print('\n Не коректный Адрес.')
else:
    print('\n Ваш Логин:', nik, 'и Адрес:', mail, 'Ок.')
