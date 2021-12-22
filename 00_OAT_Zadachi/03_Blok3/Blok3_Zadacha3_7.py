print('\n Задача БЛОК 1, Задачи 3.7.')

print('----------')


# Набор юного арифметика

def arithmetic_operation(op):
    if op == '+':
        return lambda x, y: x + y
    elif op == '-':
        return lambda x, y: x - y
    elif op == '*':
        return lambda x, y: x * y
    elif op == '/':
        return lambda x, y: x / y
    else:
        return lambda x, y: print('bad operation!')


operation = arithmetic_operation('+')
print(operation(1, 4))

print('----------')


# Просто map

def simple_map(transformation, values):
    return list(map(transformation, values))


values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))

print('----------')

# Мимикрия

transformation = lambda x: x

values = [1, 23, 42, "asdfg"]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')

print('----------')


# Самая далёкая планета

def find_farthest_orbit(orb):
    sp = []
    for i in orb:
        sp.append(i[0] * i[1])
    ind = sp.index(max(sp))
    return orb[ind]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1]))

print('----------')


# Все равны, как на подбор

def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
print()
values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
