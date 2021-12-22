# Чтение данных с сайта

# requests - библиотека запросов к страницам
# bs4 - библиотека парсинга (изъятия) информации со страниц

import requests, bs4

url = "https://market.yandex.ru/catalog--mobilnye-telefony/54726/list?hid=91491&onstock=1&local-offers-first=0"
r = requests.get(url)  # Передача URL в переменную посредством get
r.encoding = 'UTF8'  # Установка кодировки страницы к которой обращаемся

b = bs4.BeautifulSoup(r.text, "html.parser")  # Создать переменную с html.parser

atitles = b.select("div.n-snippet-cell2__title a")  # Вытащить все элементы "а" из div.n-snippet-cell2__title

titles = []  # Создать пустой массив

# Перебор массива и добавление текста в массив
for a in atitles:
    titles.append(a.getText())

print(titles)
