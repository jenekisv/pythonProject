# Чекбокса

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

choice = IntVar()  # Переменная Чекбокса (галочка вкл\выкл):

# Создание Чекбокса: ширина рамки текстового поля, текст, определение переменной, определение вкл и выкл галочки

check = Checkbutton(root, bd=20, text="Согласие на обработку данных", variable=choice, onvalue=1, offvalue=0)

# check.select()  # Включить Чекбокс, поставить галочку
# check.deselect()  # Выключить Чекбокс, снять галочку
choice.set(1)  # Включить Чекбокс, поставить галочку, используя переменную

# Чтение параметров Чекбокса на форме вкл или выкл.

print(choice.get())

check.pack()  # Вывод элемента Чекбокса на форме

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
