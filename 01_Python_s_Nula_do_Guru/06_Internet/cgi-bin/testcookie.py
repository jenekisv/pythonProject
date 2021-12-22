# Работа с cookie

import cgi, http.cookies, os  # Вывод модулей обработки

dict = {'red': 'Красный', 'green': 'Зелёный', 'orange': 'Оранжевый'}  # Создание библиотеки

r = cgi.FieldStorage()  # Создание объекта для получение параметра выбранного цвета из cgi
color = r.getvalue('color', 'white')  # Получение параметра выбранного цвета, по умолчанию white из объекта r

bg = 'background-color: {0};'  # Переменная цвета фона, с подстановкой

# Если значение есть в словаре, то тогда... (защита от всякой мути написанной пользователем)

if dict.get(color):
    bg = bg.format(color)
    print("Set-cookie: color=" + color)  # Сохранение (запись) параметра, выбранного цвета, в cookie
else:
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))  # Получение в объекта cookie из сохранёных
    color = cookie.get('color').value  # Получение цвета из объекта cookie
    if dict.get(color):
        bg = bg.format(color)  # Если есть сохранённый цвет в объекте cookie, то использовать его

print("Content-type: text/html; charset=utf-8")
print()
print("<html><head><title>Заголовок</title></head><body style='text-align: center;" + bg + "'>")  # Подстановка фона bg
print("<h1>Test Cookie!</h1>")
for key in dict:
    print("<h2><a href='?color=" + key + "'>" + dict[key] + "</a></h2>")  # Перебор библиотеки и вывод значения
print("</body></html>")  # Закрытие страничного кода
