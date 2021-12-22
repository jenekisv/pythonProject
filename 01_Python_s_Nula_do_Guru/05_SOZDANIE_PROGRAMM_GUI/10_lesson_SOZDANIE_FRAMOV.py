# Создание фреймов

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

# 1. Создание фреймов: цвет и ширина рамки
# root - родительский контейнер

frame1 = Frame(root, bg="Red", bd=1)
frame2 = Frame(root, bg="Blue", bd=10)

# 2. Создание меток внутри фреймов: текст и шрифт
# frame1, frame2 - родительский контейнер

label1 = Label(frame1, text="Метка 1", font="Tahoma 20")
label2 = Label(frame2, text="Метка 2", font="Tahoma 20")
label3 = Label(frame2, text="Метка 3", font="Tahoma 20")

# Вывод фреймов и меток в них на форме

frame1.pack()
frame2.pack()
label1.pack()
label2.pack()
label3.pack()

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
