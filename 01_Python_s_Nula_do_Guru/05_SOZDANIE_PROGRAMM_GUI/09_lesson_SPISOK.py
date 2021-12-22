# Список

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

# 1. Создание Массива

data = ["Яблоки", "Апельсины", "Лимоны"]

# 2. Создание Списка на форме: шрифт, длина и высота списка, разрешение выбора элементов множественно или SINGLE

list = Listbox(root, font="Tahoma 20", width=20, height=4, selectmode=MULTIPLE)

# 3. Привязка Массива к Списку путем перебора и добавления элементов в конец списка

for d in data:
    list.insert(END, d)

# Указание элементов, которые должны быть выбраны по умолчанию

list.selection_set(1, 2)
print(list.selection_get())

# Создание кортежа из выбранных и их вывод

indexes = list.curselection()
print(indexes)
for index in indexes:
    print(data[index])

# Вывод Списка на форме

list.pack()

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
