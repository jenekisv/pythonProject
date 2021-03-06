# функции списков и картежей

list = [1, 2, 0, 5]
print(list)
print(len(list))  # Функция получает длину массива, количество чисел в списке
list.append(9)  # Добавление элемента в конец списка
print(list)
list.extend([0, 1])  # Добавление списка в конец списка
print(list)
list.insert(1, 5)  # Добавление элемента в конкретное место списка, в примере на индекс 1 добавить число 5
print(list)
list[1] = 7  # Замена элемента списка, замена элемента с индексом 1 на число 7
print(list)

print("----------")

print(list.index(0))  # Выводит индекс элемента списка
print(list.index(0, 4))  # Выводит индекс элемента списка, начиная искать элемент с 4 индекса и далее
# print(list.index('a'))  # Выводит индекс элемента списка, если элемента нет в списке, то выходит ошибка
print(list.count('a'))  # Сколько элементов "а" находится в списке
print(list.count(0))  # Сколько элементов "0" находится в списке

print("----------")

list.reverse()  # Изменение сортировки элементов в списке, то что было в начале, стало в конце
print(list)

print("----------")

list.remove(0)  # Удаление названию элемента первого слево "0", не по индексу
print(list)
list.pop(3)  # Удаление элемента по индексу
print(list)
list.clear()  # Удаление всего списка, очистка, список останется пустым
print(list)

print("----------")

list = [1, 3, 0, 5, 1]
list.sort()  # Сортировка элементов по возрастанию
print(list)
list.sort(reverse=True)  # Сортировка элементов по убыванию
print(list)

print("----------")

# Все операции со списками так же работают и с кортежами, за исключением тех, которые меняют содержимое

t = tuple("Hello")
print(t.index("e"))
print(t.count("l"))

# Домашнее задание

# Вариант 1
k = int(input('Количество элементов: '))
print([int(input('Введите число N: ')) for i in range(k)])

# Вариант 2
k = int(input('Количество элементов: '))
spisok = []
s = 0
while s < k:
    n = int(input('Введите число N: '))
    spisok.append(n)
    s += 1
print(spisok)
