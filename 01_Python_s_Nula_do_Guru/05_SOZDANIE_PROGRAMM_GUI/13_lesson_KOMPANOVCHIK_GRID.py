# Компановщик grid

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

# Создание меток: цвет, шрифт, цвет бордюра

label1 = Label(root, text="Метка 1", font="Tahoma 20", bg="red")
label2 = Label(root, text="Метка 2", font="Tahoma 20", bg="green")
label3 = Label(root, text="Метка 3", font="Tahoma 20", bg="blue")
label4 = Label(root, text="Метка 4", font="Tahoma 20", bg="#9a3")
label5 = Label(root, text="Метка 5", font="Tahoma 20", bg="#777")

# Вывод меток на форме компановшиком grid с параметрами размещения в табличном виде

# row - какая строка
# column - какой столбец
# padx, pady - отступы от края по оси х и у
# ipadx, ipady - растянуть объект, от центра объекта по оси х (вправо и влево) и у (вверх и вниз)
# columnspan - разрешить объекту занять два столбца
# rowspan - разрешить объекту занять две строки
# sticky - выравнивание внутри определенной клетки (контейнера) таблицы, запад, восток, север, юг (w, e, n, s) и т.д.

label1.grid(row=0, column=0, padx=10, pady=20)
label2.grid(row=0, column=1, ipadx=10, ipady=20)
label3.grid(row=1, column=0, columnspan=2, pady=20, ipadx=40)
label4.grid(row=2, column=0, rowspan=2, sticky="w")
label5.grid(row=2, column=1, sticky="nw")

# Саздание и Вывод объекта на экран

Label(root, text="Метка 6", font="Tahoma 20", bg="#abf").grid(row=3, column=1, sticky="se")

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
