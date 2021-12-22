print('\n Задача БЛОК 1, Задачи 2.4.')

print('----------')

# Список покупок

a = int(input('Введите количество покупок: '))
s = []
for i in range(a):
    s.append(input('Введите наименование покупки: '))
for a in s:
    print(a)

print('----------')

# Пра-пра-пра-Яндекс

data_count = int(input('Введите количество строк с данными: '))
data = [input('Введите строки с данными: ') for _ in range(data_count)]
search_data_count = int(input('Введите количество поисковых строк: '))
search_data = [input('Введите поисковые строки: ') for _ in range(search_data_count)]
for data_item in data:
    substring_index = 0
    for search_data_item in search_data:
        substring_index = data_item.find(search_data_item)
        if substring_index == -1:
            break
    if substring_index != -1:
        print('\nНайдено:', data_item)

print('----------')

# Не бином Ньютона

numbers = []
n = int(input('Введите количество членов исходной последовательности: '))
for i in range(n):
    numbers.append(int(input('Введите сами члены последовательности: ')))
for i in range(n - 1):
    print(numbers[i] + numbers[i + 1])

print('----------')

# Белый список

n = int(input('Введите количество пунктов белого списка: '))
right = list()
left = list()
for i in range(n):
    white = input('Введите пункты белого списка: ')
    right.append(white)
nn = int(input('Введите количество запросов, которые нужно проанализировать: '))
for i in range(nn):
    answer = input('Введите запросы для анализа: ')
    left.append(answer)
for i in range(nn):
    if left[i] in right:
        print(left[i])

print('----------')

# Проверка чека

s = input('Введите количество позиций и общую сумму (3   2300): ')
n, total = int(s[:4]), int(s[4:])
errors, true_total = [], 0
for i in range(n):
    s = input('Введите цену позиции * на количество и = общая сумма по позиции (99     *2   =199): ')
    price, amount, cost = int(s[:7]), int(s[8:12]), int(s[13:])
    if price * amount != cost:
        errors.append(i + 1)
    true_total += price * amount
print(total - true_total)
for x in errors:
    print(x, end=' ')

print('----------')

# Периодическая десятичная дробь

n = int(input('Введите натуральное число: '))
r = 1
rr = []
dd = []
while r not in rr:
    rr.append(r)
    dd.append(10 * r // n)
    r = 10 * r % n
print('\nПериод разложения числа в бесконечную десятичную дробь: ', *dd[rr.index(r):], sep="")
