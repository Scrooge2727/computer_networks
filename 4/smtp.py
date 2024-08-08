import socket

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ('mail.cs.petrsu.ru', 25)

Socket.connect(host)

recv = Socket.recv(1024)
recv = recv.decode()
print(recv)

data = b""

Socket.send(b'EHLO Dan\n')#.encode("utf-8"))
recv = Socket.recv(1024)
print(recv.decode("utf-8"))

me = 'MAIL FROM: ' + input("Input your e-mail: ") + '\n'
Socket.send(me.encode())

recv = Socket.recv(1024)
recv = recv.decode("utf-8")
print(recv)

toUser = 'RCPT TO: ' + input("Input e-mail ur friend: ") + '\n'
Socket.send(toUser.encode())

recv = Socket.recv(1024)
recv = recv.decode("utf-8")
print(recv)

Socket.send('DATA\n'.encode())
recv = Socket.recv(1024)
recv = recv.decode("utf-8")
print(recv)

subject = 'Subject: ' + input("Subject: ") + '\n'
fr = 'FROM: ' + input("Sender name: ") + '\n'
to = 'TO: ' + input("Recipient name: ") + '\n'
comm = 'COMMENTS: ' + input("Comments: ") + '\n'
message = input("Main message: ") + '\n.\n'
lets_go = subject + fr + to + comm + message
Socket.send(lets_go.encode())
recv = Socket.recv(1024)
recv = recv.decode("utf-8")
print(recv)

Socket.send('QUIT\n'.encode())
recv = Socket.recv(1024)
recv = recv.decode("utf-8")
print(recv)

Socket.close()