print('\n Задача БЛОК 1, Задачи 3.8.')

print('----------')

# Словарный порядок

print(*sorted(input('Введите слова: ').split(), key=str.lower))

print('----------')

# Средний рост

x = int(input('Введите количество записей: '))
sum = 0
l = 0
try:
    for j in range(0, x):
        sum += (int(input('Введите рост: ')))
        l += 1
    answer = sum / l
    print(answer)
except ZeroDivisionError:
    print('-1')

print('----------')

# Гематрия по-английски

lst = []

while True:
    word = input("Введите английские слова для завершения q: ")
    if word == 'q':
        break
    lst.append(word)

print(*sorted(lst, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')

print('----------')

# Ох уж эти анаграммы

dic = {}
n = int(input('Введите количество исходных слов: '))
for i in range(n):
    e = input('Введите исходное слово: ').lower()
    s = ''.join(sorted(e))
    dic[s] = dic.get(s, set())
    dic[s].add(e)
new_words = [' '.join(sorted(i)) for i in dic.values() if len(i) > 1]
print('\n'.join(sorted(new_words)))
