print('\n Задача БЛОК 4, Задачи 4.4.')

print('----------')

# Склоняй меня полностью

import pymorphy2

morph = pymorphy2.MorphAnalyzer()
a = input()
word = morph.parse(a)[0]
if 'NOUN' in word.tag.POS:
    print('Единственное число:')
    print('Именительный падеж:', word.inflect({'nomn'}).word)
    print('Родительный падеж:', word.inflect({'gent'}).word)
    print('Дательный падеж:', word.inflect({'datv'}).word)
    print('Винительный падеж:', word.inflect({'accs'}).word)
    print('Творительный падеж:', word.inflect({'ablt'}).word)
    print('Предложный падеж:', word.inflect({'loct'}).word)
    print('Множественное число:')
    print('Именительный падеж:', word.inflect({'nomn', 'plur'}).word)
    print('Родительный падеж:', word.inflect({'gent', 'plur'}).word)
    print('Дательный падеж:', word.inflect({'datv', 'plur'}).word)
    print('Винительный падеж:', word.inflect({'accs', 'plur'}).word)
    print('Творительный падеж:', word.inflect({'ablt', 'plur'}).word)
    print('Предложный падеж:', word.inflect({'loct', 'plur'}).word)
else:
    print('Не существительное')

print('----------')

# 99 бутылок кваса

import pymorphy2

i = 99
w = pymorphy2.MorphAnalyzer().parse('бутылка')[0]

while i:

    print(f'В холодильнике {i} {w.make_agree_with_number(i).word} кваса.\n'
          f'Возьмём одну и выпьем.')
    i -= 1
    if i % 10 == 1 and i != 11:
        o = 'Осталась'
    else:
        o = 'Осталось'
    print(f'{o} {i} {w.make_agree_with_number(i).word} кваса.')