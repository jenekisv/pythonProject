# Минимальное, Максимальное и Сумма из списка
print("Модуль - Минимальное, Максимальное и Сумма из списка")


def chislomax(chislo):  # Максимальное число из списка
    max = chislo[0]
    for n in chislo:
        if n > max:
            max = n
    return max
# print(chislomax([int(i) for i in input('Введите числа через пробел ').split()]))


def chislomin(chislo):  # Минимальное число из списка
    min = chislo[0]
    for n in chislo:
        if n < min:
            min = n
    return min
# print(chislomin([int(i) for i in input('Введите числа через пробел ').split()]))


def chislosum(chislo):  # Сумма чисел из списка
    sum = chislo[0]
    for n in chislo:
        sum += n
    return sum
# print(chislosum([int(i) for i in input('Введите числа через пробел ').split()]))
