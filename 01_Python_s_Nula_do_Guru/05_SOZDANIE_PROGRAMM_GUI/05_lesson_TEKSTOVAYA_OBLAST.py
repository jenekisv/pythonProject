# Текстовая область

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

# Создание текстовой области: ширина рамки текстового поля, шрифт, цвет фона, цвет шрифта, размеры текстовой области
# по высоте и длине, а также отступы от краёв по оси Х и У.

text = Text(root, bd=2, font="Tahoma 20", bg="Yellow", fg="Green", width=10, height=4, padx=10, pady=20)

# Предустановка текста в области

text.insert(END, "Hello\nABC")

# Чтение параметров текстового поля на форме. Начинать с 1 строки 0 символа ("1.0") и до конца (END).

print(text.get("1.0", END))

# Вывод элементов текстового объекта на форме

text.pack()

root.mainloop()  # Вывод окна на экран до его закрытия пользователем

# Домашнее задание

print("---------")
