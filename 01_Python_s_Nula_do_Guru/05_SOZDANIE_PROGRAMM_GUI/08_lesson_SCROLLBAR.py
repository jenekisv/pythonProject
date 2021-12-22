# Скролбар

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

# 1. Создание Текстового поля: ширина рамки текстового поля, шрифт, цвет фона, цвет шрифта, длина текстовой области

text = Text(root, bd=2, font="Tahoma 20", bg="Yellow", fg="Green", width=40)

# 2. Создание Scrollbar: Привязка его по оси У, расположение - по вертикали

scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)

# 3. Привязка текстовой области к Scrollbar

text['yscrollcommand'] = scrollbar.set

# Вывод элементов Скролбар на форме

text.pack(side='left')  # Расположение текстовой области слево от края формы
scrollbar.pack(side='left', fill=Y)  # Расположение Scrollbar слево от текстовой области и растянуть на длину области

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
