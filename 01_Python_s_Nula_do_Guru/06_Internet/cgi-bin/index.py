# Создание Web-страниц 2
# Обработка форм

import cgi, html  # Вывод модулей обработки

r = cgi.FieldStorage()  # Переменная хранения полей ввода

a = html.escape(r.getvalue("a", ""))  # Вывод  поля ввода а, если значений ещё нет, то вывод пустой строки - это ""
b = html.escape(r.getvalue("b", ""))  # Вывод  поля ввода b, если значений ещё нет, то вывод пустой строки - это ""

# html.escape - это экранирование всех спец символов, защита от изменений исходника

message = ""  # Вывод переменной, изначально с пустой строкой
display = ""  # Вывод переменной, изначально с пустой строкой

# Рассчёт и обработка ошибок при рассчёте

try:
    display = float(a) + float(b)  # Сложение переменных a и b
    display = "<p>Сумма чисел равна: " + str(display) + "</p>"  # Вывод если не было вызвано исключение
except ValueError:
    message = "<p style='color: red;'>Вы ввели не числа!</p>"  # Вывод если было вызвано исключение

print("Content-type: text/html; charset=utf-8")  # Создание страницы с определёнными параметрами
print()
print("<html><head><title>Заголовок</title></head><body style='text-align: center;'>")  # Открытие и описание страницы
print("<h1>Первая Web-страница!</h1>")  # Заголовок
print("<p>Какой-нибудь текст...</p>")  # Текст

# Создание формы, метки 1, поле ввода a, метки 2, поле ввода b, кнопки посчитать
# Вывод переменной message (об ошибки), display (результат), a и b (подстановка в форму последних введённых данных a, b)

print('''
<form name="form" style="margin: 0 auto;" action="/cgi-bin/index.py" method="post">
    <h2>Сложение чисел</h2>
    ''' + message +
      '''
      <label>Число 1:</label>
      <input type="text" name="a" value="''' + a + '''" />
    <br />
    <br />
    <label>Число 2:</label>
    <input type="text" name="b" value="''' + b + '''" />
    <br />
    <br />
    <input type="submit" value="Посчитать" />
    ''' + display +
      '''</form>''')
print("</body></html>")  # Закрытие страничного кода
