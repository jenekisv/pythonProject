print('\n Задача БЛОК 1, Задачи 3.6.')

print('----------')


# Матрица

def matrix(n=1, m=0, a=0):
    if n == 1 and not m:
        m = 1
    elif n != 1 and not m:
        m = n
    return [[a for _ in range(m)] for _ in range(n)]


rows = matrix()
for row in rows:
    print(*row)
print()
rows = matrix(2)
for row in rows:
    print(*row)

print('----------')

# Дартс

scoring = {1: [8, 2], 2: [6, 9], 3: [42, 56], 20: [50, 3]}


def score(*args, **kwargs):
    global scoring
    if len(args) == 1:
        if args[0] == 'Яблочко':
            return 50
        else:
            return 25
    else:
        if args[0] == 'Внешнее_кольцо':
            return scoring[args[1]][0]
        else:
            return scoring[args[1]][1]


print(score("Яблочко"))
print()
print(score("Внешнее_кольцо", 1))

print('----------')

# Цезарь

llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
blst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
        'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


def encrypt_caesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x) % len(llst)
            ret += llst[(ind + shift) % len(llst)]
        elif x in blst:
            ind = blst.index(x) % len(llst)
            ret += blst[(ind + shift) % len(llst)]
        else:
            ret += x
    return ret


def decrypt_caesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind - shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind - shift]
        else:
            ret += x
    return ret


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
print()
msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)

print('----------')


# Частичные суммы

def partial_sums(*a):
    res = [0]
    for i in range(len(a)):
        res.append(res[i] + a[i])
    return res


print(partial_sums(13))
print()
print(partial_sums(1, 0.5, 0.25, 0.125))

print('----------')


# Уравнения степени не выше второй — часть 2

def roots_of_quadratic_equation(a, b, c: int):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        x.append(x1)
        if x1 == x2:
            return x
        else:
            x.append(x2)
            return x
    else:
        return x


x = []


def solve(*coefficients: int):
    global x
    if len(coefficients) == 3:
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        return roots_of_quadratic_equation(a, b, c)
    elif len(coefficients) == 2:
        b, c = coefficients[0], coefficients[1]
        x.append(-c / b)
        return x
    elif len(coefficients) == 1:
        if coefficients[0] == 0:
            return ['all']
        else:
            return x
    else:
        return None


print(sorted(solve(1, 2, 1)))
print()
print(sorted(solve(1, -3, 2)))
