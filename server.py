import socket

s= socket.socket()

print("Socket Created!!")
s.bind(('localhost',9998))
s.listen(3)
print("Waiting for connection")

while True:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print(name)
    print("Connected with ",addr)
    s.send(bytes("Welcome to my server",'utf-8'))
    c.close()