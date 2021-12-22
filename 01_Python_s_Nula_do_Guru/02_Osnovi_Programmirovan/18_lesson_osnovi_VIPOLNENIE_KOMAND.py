# Выполнение команд
# P.S. Узнать команды ОС можно по команде "help" в терминале

import subprocess  # Процесс который занимается выполнением команд
import io  # Модуль который читает и выводит процесс

# Оптимальная (лучшая) конструкция выполнения команд

sp = subprocess.Popen(['date'], stdout=subprocess.PIPE, shell=True)  # Запуск процесса "ДАТА"
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding="cp866")  # Чтение процесса "ДАТА" и вывод в нужной кодировке
s = ' ';
while s:
    s = out.readline()  # Вывод процесса "ДАТА" построчно
    print(s)
    break

# Домашнее задание

print('----------')

sp = subprocess.Popen(['dir'], stdout=subprocess.PIPE, shell=True)
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding="cp866")
s = ' ';
while s:
    s = out.readline()
    print(s)
