# Создание окна

from tkinter import *

# Функция настройки окна и местоположения окна на экране

root = Tk()
root.title("Окно программы")
root.resizable(False, False)  # Разрешение на изменение размера окна

w = 800  # Размер окна по ширине
h = 600  # Размер окна по высоте

# Узнаём разрешение экрана у пользователя
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

# Вывод окна по центру
x = int(ws / 2 - w / 2)
y = int(wh / 2 - h / 2)

# root.geometry("800x600+700+400")

root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))  # Указание местоположения окна

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
