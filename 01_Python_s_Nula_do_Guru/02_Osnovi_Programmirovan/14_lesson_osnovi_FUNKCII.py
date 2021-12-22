# Функции

def printpython():
    print('Python')


printpython()


def sum(x, y):
    return x + y


s = sum(5, 7)
print(s)


def sub(x, y):
    return x - y


print(sub(10, 15))
print(sub(y=10, x=15))


def summaprint(x, y, r=False):
    s = sum(x, y)
    if r:
        return s
    else:
        print(s)


summaprint(15, 7)
print(summaprint(15, 7, True))


def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s


print(bigsum(1, 5, 7, 0, 1))


def printdict(**dict):
    for key in dict:
        print(key, '=', dict[key])


printdict(name='Alex', age=15)


def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max


print(getmax([5, 7, 0, 12, 1]))
print(getmax([-5, -7, 1, 10, 50, 99]))

print('----------')

print('Анонимные функции')
lambdafunc = lambda x, y: print(x + y)
lambdafunc(5, 7)

result = (lambda x, y: x + y)(1, 3)
print(result)

# Домашнее задание

print('----------')


def chetda(number):  # Чётное или Нечётное
    number = int(number)
    if number % 2 == 0:
        print('Чётное?:', True)
    if number % 2 == 1:
        print('Чётное?:', False)


a = int(input("Введите число: "))
chetda(a)

print('----------')


def chislomax(chislo):  # Максимальное число из списка
    max = chislo[0]
    for n in chislo:
        if n > max:
            max = n
    return max


print(chislomax([5, 7, 0, 12, 1, 75]))

print('----------')


def srednee(*nums):  # Среднее арифметическое число списка
    kolvo = len(nums)
    sum = 0
    for n in nums:
        sum += n
    sred = sum / kolvo

    print("Sum: ", sum, 'Kolvo: ', kolvo, 'Sred: ', sred)


srednee(3, 5)
srednee(4, 5, 6, 7)
srednee(1, 2, 3, 5, 6)
