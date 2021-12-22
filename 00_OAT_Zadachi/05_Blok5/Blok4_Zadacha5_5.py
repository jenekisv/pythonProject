print('\n Задача БЛОК 5, Задачи 5.5.')

print('----------')

# Сайт поиска вакансий

class Profile:
    def __init__(self, proffesion):
        self.proffesion = proffesion

    def info(self):
        return ''

    def describe(self):
        print(self.proffesion, self.info())


class Vacancy(Profile):
    def __init__(self, profile, a):
        super().__init__(profile)
        self.a = a

    def info(self):
        return f'Предлагаемая зарплата: {self.a}'


class Resume(Profile):
    def __init__(self, profile, a):
        super().__init__(profile)
        self.a = a

    def info(self):
        return f'Стаж работы: {self.a}'

print('----------')

# Сумматоры – 2

class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        s = 0
        for i in range(1, N + 1):
            s += self.transform(i)
        return s


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)