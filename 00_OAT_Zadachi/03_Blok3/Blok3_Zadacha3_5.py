print('\n Задача БЛОК 1, Задачи 3.5.')

print('----------')


# Длина списка

def recursive_len(some_list):
    if not some_list:
        return 0
    return 1 + recursive_len(some_list[:-1])


print(recursive_len([1, 2, 3]))

print('----------')


# косипсьтунревереП

def recursive_reverse(some_list):
    if not some_list:
        return []
    return [some_list.pop()] + recursive_reverse(some_list)


print(recursive_reverse([1, 2, 3]))

print('----------')


# Трибоначчи

def tribonacci(n, c=1, p=0, pp=0):
    if n == 0:
        return pp
    if n == 1:
        return p
    if n == 0:
        return c
    else:
        return tribonacci(n - 1, c + p + pp, c, p)


print(tribonacci(0))

print('----------')


# Сумма элементов списка

def rec_linear_sum(items):
    if len(items) < 2:
        return items[0]
    return items[0] + rec_linear_sum(items[1:])


print(rec_linear_sum([1, 3, 5, 9]))

print('----------')


# Линеаризация списка

def linear(lst):
    r = []
    for a in lst:
        if type(a) == list:
            r += linear(a)
        else:
            r += [a]
    return r


print(*linear([]))
print()
print(*linear([[1, 2], 4, [[2, 4, 8, [-4, "er", [0], [{2: "primer"}], []]]]]))
