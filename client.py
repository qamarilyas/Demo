import socket

c= socket.socket()
#On client side after socket created, connect and send/receive
c.connect(('localhost',9998))

print(c.recv(1024).decode())
c.send(bytes("I am conncted",'utf-8'))