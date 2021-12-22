# Кортежи

mytuple = tuple()  # Объявление кортежа, первый способ
print(mytuple)
mytuple = ()  # Объявление кортежа, второй способ
print(mytuple)

print('----------')

# При создании кортежа из одного элемента, ставить запятую обязательно
mytuple = (1,)
print(mytuple)

print('----------')

mytuple = (1, '3', '5')
print(mytuple)
# mytuple[1] = '5'  # При попытке изменить элемент, выдаётся ошибка
print(mytuple[1])
mytuple = tuple('Python')
print(mytuple)

# Домашнее задание

print('----------')

strok = str(input('Введите произвольную строку: '))
print(strok)
tup = tuple(strok)  # Конвертация строки в кортеж
print(tup)

print('----------')

s = tuple(strok)  # Конвертация строки в кортеж

print(s)
