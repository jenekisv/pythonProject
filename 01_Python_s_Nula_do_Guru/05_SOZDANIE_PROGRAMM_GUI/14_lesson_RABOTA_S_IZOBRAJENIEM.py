# Работа с изображениями

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

# Класс PhotoImage для работы с изображениями из модуля tkinter

photo = PhotoImage(file="test.png")
bgimage = photo.zoom(2, 2)  # Увеличение размера объекта (фона)

bg = Label(root, image=bgimage)

# Создание кнопки и размещение изображения на кнопке
buttonimage = photo.subsample(4, 4)  # Изменение размера объекта (фона) на кнопке
button = Button(root, image=buttonimage)

bg.place(x=0, y=0, relwidth=1, relheight=1)  # Сделать объект фоном на всю ширину и высоту

button.pack()  # Вывод кнопки с размещенным изображением на кнопке

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
