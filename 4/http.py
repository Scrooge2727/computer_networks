#!/bin/python3
import socket, time
print("Введите адрес")
host = input()
#host = 'www.google.com'
print("Введите порт")
port = input()
#port = 80
http = 'HTTP/1.1'

m = 'GET / '+ http +'\r\nHost: '
n = '\r\nConnection: close\r\n\r\n'
request = m + host + n

print('Наш запрос:\n\n' + request)
time.sleep(2)

#получаем кортеж; отправляем все данные; отключаемся, запрещая отправку
sock = socket.socket()
#подключаемся к удалённому сокету;
target = socket.getaddrinfo(host, port)
sock.connect(target[0][4])
sock.sendall(bytes(request, 'utf-8'))
sock.shutdown(socket.SHUT_WR)

data = ' '
response = ''

while data:
    #Получаем данные из сокета и записываем их
    data = sock.recv(1024)
    response = response + data.decode()

print('Ответ сервера:\n\n')
time.sleep(1)
print(response)
