# Обработка событий 3

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


# Функция счёта с обработкой исключений

def handlerbutton(event=False):
    global en1
    global en2
    global result
    if event:  # Вывод посредством нажатие клавиши Enter
        print(event)
    try:
        r = str(float(en1.get()) + float(en2.get()))
        result.config(text="Сумма чисел равна: " + r)
    except ValueError:
        if not en1.get() or not en2.get():
            result.config(text="Вы ничего не ввели!")
        else:
            result.config(text="Вы ввели не числа!")


# root - родительский контейнер из импортируемого модуля tkinter (все для создания форм)

root = Tk()
setwindow(root)

# Создание меток, полей ввода, кнопки

header = Label(root, text="Суммирование чисел", font="Tahoma 20")
en1 = Entry(root, font="Tahoma 20")
en2 = Entry(root, font="Tahoma 20")
button = Button(root, text="Сумма", font="Tahoma 20", command=handlerbutton)
result = Label(root, font="Tahoma 20")

# Обработка событий полей ввода через нажатие клавиши Enter

en1.bind("<Return>", handlerbutton)
en2.bind("<Return>", handlerbutton)

# Вывод объектов на экран

header.place(relx=0.5, rely=0.01, anchor="n")
en1.place(relx=0.5, rely=0.1, anchor="n")
en2.place(relx=0.5, rely=0.2, anchor="n")
button.place(relx=0.5, rely=0.3, anchor="n")
result.place(relx=0.5, rely=0.4, anchor="n")

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
