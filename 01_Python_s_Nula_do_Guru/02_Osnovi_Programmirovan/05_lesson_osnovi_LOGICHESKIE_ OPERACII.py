# Логические операции

b1 = True
b2 = False
print('b1 =', b1)
print('b2 =', b2)
print('b1 or b2', b1 or b2)  # Это ИЛИ это
print('b1 and b2', b1 and b2)  # Это И это
print('not b1 =', not b1)  # Изменение на противоположное значение (это равно 1; это не равно 1)
print('b1 != b2 =', b1 != b2)  # Исключающее ИЛИ (это не равно этому)
print('b1 == b2 =', b1 == b2)  # Проверка на равенство
print()
# Операторы сравнения
x = 5
y = 7
print('x =', x)
print('y =', y)
print('x > y =', x > y)
print('x < y =', x < y)
print('x >= y =', x >= y)
print('x <= y =', x <= y)
print('7 < 7 =', 7 < 7)
print('7 <= 7 =', 7 <= 7)
print('x and b1 or (x < 10) =', x and b1 or (x < 10))
print('x > 10 or y < 7 =', x > 10 or y < 7)
print('x > 10 or y <= 7 =', x > 10 or y <= 7)

# Домашнее задание
print(True and (True or (False and True or False) and True or True != False))
print(15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18))
print(True or True)
