print('\n Задача БЛОК 1, Задачи 2.1.')

print('----------')

# Города

n = int(input('Введите количество городов: '))
c = set()
for i in range(n):
    b = input('Введите город 1: ')
    c.add(b)
a = input('Введите город: ')
if a not in c:
    print('OK')
else:
    print('TRY ANOTHER', n)

print('----------')

# Языки – 1

n = int(input('Введите количество учеников изучающих английский: '))
m = int(input('Введите количество учеников изучающих немецкий: '))
languages = set()
surnames = set()
for i in range(n + m):
    surname = input('Введите фамилии учеников: ')
    if surname in languages:
        surnames.add(surname)
    else:
        languages.add(surname)
difference = languages - surnames
if not difference:
    print('NO')
else:
    print(len(difference))

print('----------')

# Языки – 2

people = set()
pause = set()
n = int(input('Введите количество учеников изучающих английский: '))
m = int(input('Введите количество учеников изучающих немецкий: '))
k = int(input('Введите количество учеников изучающих французский: '))
cout = 0
for i in range(n + m + k):
    name = input('Введите фамилии учеников: ')
    if name in people:
        cout += 1
        pause.add(name)
    people.add(name)
if (n == k == m) and len(people) == n:
    print('NO')
else:
    if len(pause) + cout > 0:
        if ((len(pause) + cout) % 2 != 0):
            print((len(pause) + cout) % 2)
        else:
            print((len(pause) + cout) // 2)
    else:
        print('NO')

print('----------')

# Книги на лето

home_biblion = set()
home_biblion_N = int(input('Введите количество книг, имеющиеся дома: '))
home_task = set()
home_task_M = int(input('Введите количество книг для чтения летом: '))
for i in range(home_biblion_N):
    book = input('Введите список книг, имеющиеся дома: ')
    home_biblion.add(book)
for i in range(home_task_M):
    book = input('Введите список книг для чтения летом: ')
    home_task.add(book)
    if book in home_biblion:
        print('YES')
    else:
        print('NO')

print('----------')

# Однофамильцы

sets = set()
sets2 = set()
N = int(input('Введите количество сотрудников: '))
k = 0
for i in range(N):
    sname = input('Введите фамилии сотрудников: ')
    if not sname in sets:
        sets.add(sname)
        sets2.add(sname)
    elif sname in sets2:
        k += 2
        sets2.remove(sname)
    else:
        k += 1
print(k)

print('----------')

# Новые блюда

menu = set()
use_menu = set()
menu_not_use = set()
menu_N = int(input('Введите количество блюд: '))
for i in range(menu_N):
    menu.add(input('Введите названия блюд: '))
day_menu_true = int(input('Введите число дней для которых есть списки блюд: '))
for i in range(day_menu_true):
    menu_in_day_N = int(input('Введите количество блюд в данный день: '))
    for j in range(menu_in_day_N):
        use_menu.add(input('Введите названия блюд в данный день: '))
menu_not_use = menu - use_menu
print(*menu_not_use, sep='\n')
