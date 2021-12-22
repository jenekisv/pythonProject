# Обработка событий 2

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


# Обработка события изменения цвета кнопки формы при наведение мышкой на данную кнопку
# Обработка события event.widget. для всех объектов имеющих параметр фона
# Обработка события например button1. для конкретного объекта имеющиго параметр фона

def handlerenter(event):
    event.widget.config(bg="red")


# Обработка события изменения цвета кнопки формы при уведение мышки с данной кнопки
# Обработка события event.widget. для всех объектов имеющих параметр фона
# Обработка события например button1. для конкретного объекта имеющиго параметр фона

def handlerleave(event):
    event.widget.config(bg="yellow")


# root - родительский контейнер из импортируемого модуля tkinter (все для создания форм)

root = Tk()
setwindow(root)

# Создание кнопок

button1 = Button(root, text="Кнопка 1", font="Tahoma 20", bg="yellow")
button2 = Button(root, text="Кнопка 2", font="Tahoma 20", bg="yellow")

# Обработка события изменения цвета кнопки формы при наведение мышкой на данную кнопку

button1.bind("<Enter>", handlerenter)
button1.bind("<Leave>", handlerleave)
button2.bind("<Enter>", handlerenter)
button2.bind("<Leave>", handlerleave)

# Вывод кнопок на экран

button1.pack()
button2.pack()

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
