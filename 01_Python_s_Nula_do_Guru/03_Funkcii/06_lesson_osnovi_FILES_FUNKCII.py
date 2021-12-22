# функции Работы с файлами

# Открытие файла:
# 1) с модификатор "w" - для записи (содержимое файла будет удалено), если файла не существует, то будет создан
# 2) с модификатор "x" - для записи (содержимое файла будет удалено), если файла не существует, то исключение (ошибка)
# 3) с модификатор "a" - для записи (содержимое файла будет сохранено), если файла не существует, то будет создан
# 4) с модификатор "rt" - для чтения, открытие текстового файла, если файла не существует, то исключение (ошибка)
# 4) с модификатор "rb" - для чтения, открытие байтового файла (mp3..), если файла не существует, то исключение (ошибка)

handler = open('a.txt', 'w')  # Открыть файл для записи
handler.write("abc 123\n890")  # Функция записи строк в открытый файл
handler.close()  # Закрыть файл

print("------------")

handler = open('a.txt', 'r')  # Открыть файл для чтения
print(handler.read(2))  # Прочесть первые 2 символа из файла
print(handler.read())  # Продолжить чтение всего остального, начиная со 2 символа из файла

print("------------")

handler.seek(0)  # Сбросить указатель на начало строки
print(handler.read())  # Прочесть все из файла, весь файл

print("------------")

handler.seek(0)  # Сбросить указатель на начало строки
for line in handler:  # Читать весь файл построчно
    print(line)
handler.close()  # Закрыть файл

print("------------")

file = "b.txt"

while True:
    print("1 - Записать в файл; 2 - Прочитать файл; 0 - Выход")
    inp = input("Введите команду: ")
    if inp == "0":
        break
    elif inp == "1":
        text = input("Введите строку: ")
        handler = open(file, 'w')
        handler.write(text)
        handler.close()
    elif inp == "2":
        try:
            handler = open(file, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print("Файла ещё не существует!")
    else:
        print("Неизвестная команда")

# Домашнее задание

print('----------')

while True:
    print("write - Записать в файл; read - Прочитать файл; quit - Выход")
    inp = input("Введите команду: ")
    if inp == "quit":
        exit(0)
    elif inp == "write":
        filew = input('Напишите путь к файлу, который Вы хотите изменить: ')
        text = input("Введите строку которую надо записать в файл: ")
        handler = open(filew, 'w')
        handler.write(text)
        handler.close()
    elif inp == "read":
        filer = input('Напишите путь к файлу, содержимое которого Вы хотите посмотреть: ')
        try:
            handler = open(filer, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print("Файла ещё не существует!")
    else:
        print("Неизвестная команда")
