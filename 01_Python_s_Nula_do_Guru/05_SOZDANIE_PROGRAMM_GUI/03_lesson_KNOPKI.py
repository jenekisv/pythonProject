# Кнопки

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


# Функция настройки окна и местоположения окна на экране

root = Tk()
setwindow(root)

# Создание кнопок: вывод текста, цвет фона, цвет шрифта, шрифт

button1 = Button(root, text="Моя кнопка 1", bg="White", fg="Green", font="Tahoma 18")
button2 = Button(root, text="Моя кнопка 2", bg="White", fg="Green", font="Tahoma 22")

# Вывод элементов кнопок на форме

button1.pack()
button2.pack()

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
