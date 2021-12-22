print('\n Задача БЛОК 1, Задачи 3.3.')

print('----------')


# Длина окружности и площадь круга

def circle_length(radius):
    p = 3.14159
    return radius * p * 2


def circle_area(radius):
    p = 3.14159
    return p * radius ** 2


def main():
    r = float(input())
    p = 3.14159
    print(r * p * 2, p * r ** 2)


print(circle_length(5))
print()
print(circle_area(10))

print('----------')


# Длина окружности и площадь круга

def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def larger_root(p, q):
    d = discriminant(1, p, q)
    if d >= 0:
        return (-p + d ** 0.5) / 2


def smaller_root(p, q):
    d = discriminant(1, p, q)
    if d >= 0:
        return (-p - d ** 0.5) / 2


print(discriminant(1, 2, 1))
print(smaller_root(2, 1))
print(larger_root(2, 1))

print('----------')

# Длинный чек

count: int = 1
items: [(str, int)] = []


def add_item(name: str, cost: int):
    items.append((name, cost))


def print_receipt():
    global count
    if not items:
        return
    total: int = 0
    print(f"Чек {count}. Всего предметов: {len(items)}")
    for name, cost in items:
        total += cost
        print(f"{name} - {cost}")
    print(f"Итого: {total}\n-----")
    count += 1
    items.clear()


add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
# (Отменить чек) - этот чек не печатаем

print('----------')

# НРЗБРЧВ

translatedText = ''


def translate(text):
    global translatedText
    redLetter = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
                 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                 '.', ',', '-']
    for i in range(len(text) - 1):
        if redLetter.count(text[i]) == 0:
            translatedText = translatedText + text[i]
    translatedText = ' '.join(translatedText.split())
    return translatedText


print(translate('Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно \
 небольшой тренировки - и вы сможете это делать.'))

print('----------')


# Айболит

def hello(name):
    print('Здравствуйте, {}! Вашу карту ищут...'.format(name))


def search_card(name):
    global base
    for i, val in enumerate(base):
        if val == name:
            print('Ваша карта с номером {} найдена'.format(i + 1))
            return
    print('Ваша карта не найдена')


base = ["Иван", "Юлия Иванова"]

hello("Иван")
search_card("Иван")
hello("Юлия Иванова")
search_card("Юлия Иванова")

print('----------')


# Делайте ваши ставки

def do_bet(horse, bet):
    if bet == 0 or horse in horses or horse > 10 or horse <= 0:
        print('Что-то пошло не так, попробуйте еще раз')
        return
    else:
        print('Ваша ставка в размере', bet, 'на лошадь', horse, 'принята')
        horses.append(horse)
        return


horses = []

do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)

print('----------')

# Бюрократия

Name = ''
Vac = ''


def setup_profile(name, vac):
    global Name, Vac
    Name = name
    Vac = vac
    return None


def print_application_for_leave():
    global Name, Vac
    print('Заявление на отпуск в период ', Vac, '. ', Name, sep='')
    return None


def print_holiday_money_claim(amo):
    global Name
    print('Прошу выплатить ', amo, ' отпускных денег. ', Name, sep='')
    return None


def print_attorney_letter(to):
    global Name, Vac
    print('На время отпуска в период ', Vac, sep='', end='')
    print(' моим заместителем назначается ', to, '. ', Name, sep='')


setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысячпиастров")
print_attorney_letter("ВасилийВасильев")
