# Компановщик pack

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

# Вывод меток на форме компановшиком pack с параметрами размещения от краёв по центру (местами размещения меток)

# side - от какого края размещать (верх, низ, право, лево)
# fill - растянуть данный объект по оси Х или У заняв все оставшееся место
# expand - размещение строго по центру от оставшегося места
# anchor - выравнивание по краю (углу), запад, восток, север, юг (w, e, n, s)

label1.pack(side='left', fill=X, expand=True, anchor="n")
label2.pack(side='top')
label3.pack(side='top')
label4.pack(side='bottom')
label5.pack(side='bottom', expand=True)

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
