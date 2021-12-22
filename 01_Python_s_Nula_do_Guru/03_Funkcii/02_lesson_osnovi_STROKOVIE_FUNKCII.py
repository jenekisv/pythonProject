# Строковые функции

s1 = "str_1"
print(len(s1))  # Длина строки, количество знаков в строке
print(s1[1])  # Вывод знака из строки по индексу
print(s1[-1])  # Вывод последнего знака из строки по индексу
print(s1[-2])  # Вывод предпоследнего знака из строки по индексу
print(s1[1:3])  # Вывод знаков из строки по индексу, с 1 до 3, не включая 3

s1 = "abc\nnxyz"  # Перенос на другую строку
s2 = r"abc\nxyzx"  # "r" - перед сторкой - это отмена в строке всех спец символов, чтобы не экраниорвать знаком "\"
print(s1)
print(s2)

print("------")

s1 = "hello"
s2 = s1 * 3  # Пример сохранения результат вычислений, конкретно в переменной
print(s1 * 3)  # print - только выводит результат вычислений, не сохраняет его
print(s1)  # Вывод значения переменной
print(s2)  # Вывод значения переменной

print(s1.find("l"))  # Поиск подстроки в строке до нахождения первого совпадения
print(s1.find("l", 3))  # Поиск подстроки в строке, начинать с 3 индекса, до нахождения первого совпадения

print("593".isdigit())  # Проверяет, является ли вся строка числовой, только целые числа, булевая
print(s1.isalpha())  # Проверяет, является ли вся строка в переменной "s1" текстовой, булевая
print(s1.upper())  # Конвертирует всю строку в верхний регистр
print(s1.lower())  # Конвертирует всю строку в нижний регистр

print("------")

print(ord("a"))  # Выводит код заданного символа
print(chr(98))  # Выводит символа заданного кода

s1 = "          hello           "
print(s1)
print(s1.strip())  # Функция обрезки всех пробелов, табуляций

print("------")

s1 = "Здравствуйте, {0}. Вам {1} лет!"  # Шаблон для подстановки значений
print(s1.format('Alex', 30))  # Формат подстановки значений в шаблон

# Тоже, что и в предыдущем, но понятнее
s1 = "Здравствуйте, {name}. Вам {age} лет!"
print(s1.format(name='Alex', age=30))

data = ('Alex', 30)  # Кортеж
s1 = "Здравствуйте, {0[0]}. Вам {0[1]} лет!"  # Шаблон для подстановки значений из кортежа
print(s1.format(data))

s1 = "int: {0:d}; bin: {0:b}"  # Преобразовать число в десятичную систему и в двоичную систему счисления
print(s1.format(5))

s1 = "Round (150 / 47) = : {0:.3}"  # Округление до 3 цифр, всего, до и после запятой
print(s1.format(150 / 47))

# Домашнее задание

# Выводим коды всех символов строки, введённой пользователем.
strok = str(input('Введите любой набор символов в строку: '))
print(list(map(lambda x: (ord(x), x), strok)))

# Проверка строки, числовая или нет
while True:  # Бесконечный цикл
    chisl = input('Введите любые числа через запятую: ')
    try:  # Пытаться
        chisl = chisl
        if chisl == chisl.isdigit():
            raise Exception("Не числовая строка!")  # Выдвинуть (создать) своё исключение
    except Exception as exp:  # Присвоить (укоротить) имя исключения
        print(exp)
        print(chisl.isdigit())
    else:  # Иначе
        print("Спасибо за корректный ввод!")
        break  # Завершить цикл


# Функция проверки строки на соответствие виду (классу), конкретно "float"
def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
