# функции Словари

d = {'name': 'Alex', 'age': 35}
print(d)
d.setdefault('isWorking', True)  # Добавление элемента в словарь, новой пары, ключ - значение
print(d)
print(d.get('age'))  # Получение значения из словаря по ключю
d.pop('name')  # Удаление значения из словаря по ключю, удаляется пара: ключ - значение
print(d)

keys = list(d.keys())  # Вывод всех ключей из словаря
print(keys)
print(keys[0])

print("--------")

values = list(d.values())  # Вывод всех значений из словаря
print(values)
print(values[0])

d['age'] = 40  # Изменение значения в словаре по ключу
d['isMale'] = True  # Добавление элемента в словарь, новой пары, ключ - значение
print(d)

d.clear()  # Удаление всего словаря, очистка, словарь останется пустым
print(d)

# Домашнее задание

print('----------')

import random

slovar = {'Hello': 'Здравствуй', 'Bye': 'Пока', 'Lesson': 'Урок'}
rand_value = random.choice(list(slovar.values()))

while True:
    print(rand_value)  # вывожу рандомно значение словаря slovar
    prompt = input("Напишите перевод слова на английском: ")
    if prompt == 'show':
        print(slovar)  # если напишете show, то покажу словарь slovar
    elif prompt == 'quit':
        print('Завершение опроса')
        exit(0)
    else:
        if slovar.get(prompt.title()) == rand_value:
            print('Правильно')
            rand_value = random.choice(list(slovar.values()))
        else:
            print('Неправильный перевод слова. Попробуйте еще.')
