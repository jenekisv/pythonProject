print('\n Задача БЛОК 1, Задачи 3.1.')

print('----------')


# Формальное приветствие

def hello():
    name = input('Введите Имя: ')
    surname = input('Введите Фамилию: ')
    print('Здравствуйте,', name, surname + '.')


if __name__ == '__main__':
    print(hello())

print('----------')


# Привет, как тебя там?

def hello1():
    x = input('Введите Имя: ')
    while not all((x.isalpha(), x.istitle(), len(x) > 1)):
        x = input('Введите Имя: ')
    print('Привет, {}!'.format(x))


if __name__ == '__main__':
    print(hello1())

print('----------')


# Какая четверть?

def quoters(x, y):
    if (x > 0) and (y > 0):
        print('I')
    elif (x < 0) and (y > 0):
        print('II')
    elif (x < 0) and (y < 0):
        print('III')
    elif (x > 0) and (y < 0):
        print('IV')
    return (x, y)


if __name__ == '__main__':
    x, y = map(float, input('Введите координаты через пробел: ').split())
    quoters(x, y)

print('----------')


# Золотое сечение

def golden_ratio(i):
    count = 1
    fi1 = 1
    fi2 = 1
    fi3 = 0
    while i != count:
        fi3 = fi1
        fi1 = fi2
        fi2 = fi2 + fi3
        count += 1
    one = fi1
    while i + 1 != count:
        fi3 = fi1
        fi1 = fi2
        fi2 = fi2 + fi3
        count += 1
    two = fi1
    result = two / one
    print(result)


if __name__ == '__main__':
    i = int(input('Введите число золотого сечения: '))
    print(golden_ratio(i))

print('----------')


# Скажи «пароль» и проходи

def ask_password():
    for i in range(0, 3):
        s = input('Введите пароль: ')
        if s == 'password':
            print('Пароль принят.')
            break
        else:
            print('В доступе отказано')
    return


if __name__ == '__main__':
    print(ask_password())

print('----------')


# Статистики

def print_statistics(arr):
    mediana = None
    number = None
    if not len(arr):
        print('Список пустой или не предоставлен')
    else:
        arr = sorted(arr)
        number = len(arr)
        number1 = (number - 1) // 2
        if number % 2 == 0:
            mediana = (arr[number1] + arr[number1 + 1]) / 2
        else:
            mediana = arr[number1]

        print(f'Длина списка - {number}, Среднее - {sum(arr) / number}, '
              f'Минимальное значение - {min(arr)}, Максимальное значение - {max(arr)}, '
              f'Медиана списка - {mediana}')


print_statistics([5, 3, 4, 8])
print_statistics([5, 4, 3, 8, 9])
print_statistics([22])
print_statistics([])

print('----------')

# Правильная скобочная последовательность

# s = '())(()'
s = input('Введите скобки для проверки: ')
k = 0
for b in s:
    k += [-1, 1][b == '(']
    if k < 0:
        break
print(['NO', 'YES'][k == 0])
