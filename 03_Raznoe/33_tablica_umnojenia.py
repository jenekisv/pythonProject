print('----------')

# Таблица умножения

k = int(input('Введите, до какого разряда считать таблицу умножения: '))
for j in range(1, k + 1):
    for i in range(1, 10):
        print(i, '*', j, '=', j * i, sep='', end='\t')
    print()
