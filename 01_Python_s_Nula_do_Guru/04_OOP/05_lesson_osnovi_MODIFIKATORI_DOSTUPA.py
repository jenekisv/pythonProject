# Модификаторы доступа.

class Point:
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __test(self):  # private
        print("Private метод")

    def runPrivate(self):  # public
        self.__test()


p = Point(10, 15)
# print(p.__x)  # Ошибка
print(p.getX())
print(p.getY())
p.setX(20)
p.setY(8)
print(p.getX())
print(p.getY())

# p.__test()  # Ошибка

p.runPrivate()

# Домашнее задание

print('----------')
