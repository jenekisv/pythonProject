# Обработка событий 1

from tkinter import *


# Функция настройки окна и местоположения окна на экране

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


# root - родительский контейнер из импортируемого модуля tkinter (все для создания форм)

root = Tk()
setwindow(root)


def handlerclick1(args):
    print(args)


def handlerclick2():
    print("Нажата кнопка")


def handlerclick3(event):
    print("Кликнули правой кнопкой мыши по кнопке: ")
    print(event.widget.cget('text'))


def handlerroot(event):
    print(event)
    print("Сработало событие")


# Обработка события посредством lambda выражения

button1 = Button(root, text="Кнопка 1", font="Tahoma 20", command=lambda: handlerclick1("Кнопка 1"))

# Обработка события посредством указания аргумента в функции

button2 = Button(root, text="Кнопка 2", font="Tahoma 20", command=handlerclick2)
button3 = Button(root, text="Кнопка 3", font="Tahoma 20")

# Обработка события клика мышкой по кнопке

handler = button2.bind("<Button-3>", handlerclick3)
button3.bind("<Button-3>", handlerclick3)

# Отмена обработка события клика мышкой по кнопке

button2.unbind(handlerclick3, handler)

# Обработка события нажатия символа на форме (горячии клавиши)

root.bind("a", handlerroot)
root.bind("<Control-c>", handlerroot)

# Вывод кнопок на экран

button1.pack()
button2.pack()
button3.pack()

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
