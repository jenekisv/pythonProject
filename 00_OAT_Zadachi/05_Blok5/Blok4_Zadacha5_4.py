print('\n Задача БЛОК 5, Задачи 5.4.')

print('----------')

# Классификация животных

class Animal():
    def breathe(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass
print('----------')

# Социальная сеть

class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print(self.name)
        print(self.info)


class Person(User):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def info(self):
        return f'Дата рождения: {self.date}'

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, about):
        self.name = name
        self.about = about

    def info(self):
        return f'Описание: {self.about}'
