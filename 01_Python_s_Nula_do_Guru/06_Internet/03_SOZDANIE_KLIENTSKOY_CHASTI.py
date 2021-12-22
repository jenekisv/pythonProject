# Создание клиентской части

import socket

SERVER_ADDRESS = ('localhost', 15253)

client = socket.socket()  # Создание сервера
client.connect(SERVER_ADDRESS)  # Привязка к адресу
client.send(bytes("hi Jenek!", encoding="UTF-8"))  # Отправка на сервер
data = client.recv(4096)  # Полученик от сервера
print("Получили от сервера: ", data.decode("UTF-8"))  # Вывод результата
