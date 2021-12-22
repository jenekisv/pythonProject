# Словари

mydict = dict()  # Объявление переменной словарём
print(mydict)
mydict = {'Name': 'John', 'Age': 35}  # Создание словаря, первый способ
print(mydict)

print('----------')

mydict = dict(Name='John', Age=35, isMale=True)  # Создание словаря, второй способ
print(mydict)

print('----------')

print(mydict['Age'])  # Вывод значения с индексом 'Age'

print('----------')

for key in mydict:
    print(key, '=', mydict[key])  # Вывод всех значений словаря по ключу

print('----------')

mytuple = ('Name', 'Age', 'isMale')  # Объявление кортежа
for key in mytuple:
    print(key, '=', mydict[key])  # Вывод всех значений словаря по ключу кортежа

print('----------')

mydict = {i * 2: i for i in range(1, 10)}  # Генератор словаря
print(mydict[2])
mydict = {str(i * 2): i for i in range(1, 10)}  # Генератор словаря, правильнее использовать строковый индекс
print(mydict)

# Домашнее задание

print('----------')

slv = {'Name': '', 'Age': -1}
name = str(input('Введите своё имя: '))
ag = int(input('Введите свой возраст: '))
slv['Name'] = name
slv['Age'] = ag
for key in slv:
    print(key, '=', slv[key])  # Вывод всех значений словаря по ключу
