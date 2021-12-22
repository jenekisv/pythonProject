# Отладка
a = 0
while True:
    a += 0.1
    # print(a)
    if (a >= 1):
        break
    print("Hello")

# Домашнее задание

print('----------')

# Перебрать список, выбрать все отрицательные числа и вывести их
# Произвести отладку

number = [1, 2, -5, 8, -9]
max = []
for num in number:
    if num < 0:
        max.append(num)
print(max)
