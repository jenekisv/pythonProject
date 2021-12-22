# Компановщик place

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

# Вывод меток на форме компановшиком place с параметрами размещен. по координатам х и у от общего места (не оставшегося)

# relx, rely - относительные координаты, относительно какого - либо места
# anchor - выравнивание объекта строго по центру запад, восток, север, центр и т.д. (w, e, n, s, ne, nw, se, sw, center)

label1.place(x=10, y=0)  # Координаты левого верхнего угла объекта

# Координаты относительно центра левого верхнего угла объекта, добавление anchor - строго по центру объекта
label2.place(relx=0.5, rely=0.5, anchor="center")
label3.place(relx=0.5, y=0, anchor="n")  # Совмещение абсолютных и относительных координат, смещение на север (по верху)
label4.place(relx=0.5, rely=0.7, width=70, height=100, anchor="center")  # Указание длины и ширины объекта
label5.place(relx=1, y=0, anchor="ne")  # Смещение объекта на северо - восток (правый верхний угол объекта)

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
