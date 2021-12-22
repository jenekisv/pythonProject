# Текстовое поле

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

# Создание текстовых полей: шрифт, цвет фона, цвет шрифта, ширина рамки текстового поля

entry1 = Entry(root, font="Tahoma 20", bg="Yellow", fg="Green", bd=4)

# Заменить все символы при вводе * (звёздочкой) - это show="*"

entry2 = Entry(root, font="Tahoma 20", bg="Yellow", fg="Green", bd=4, show="*")

# Предустановка текста в поле

entry1.insert(END, "Введите Имя")
entry2.insert(END, "Введите Пароль")

# Просмотр свойств элементов текстовго поля на форме

print(entry1.cget('font'))
print(entry1['font'])

# Изменение свойств элементов текстовго поля на форме

entry1['font'] = 'Tahoma 40'

# Заменить все символы при вводе на (а) - или show="а"

entry1['show'] = 'a'

# Вывод элементов текстового поля на форме

entry1.pack()
entry2.pack()

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
