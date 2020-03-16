import socket

s= socket.socket()

print("Socket Created!!")

# After creating socket 3 steps.(Bind, listen and accept)
#1. Bind
s.bind(('localhost',9998))
#2. listen
s.listen(3)
print("Waiting for connection")

while True:
    #3. accept
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print(name)
    print("Connected with ",addr)
    s.send(bytes("Welcome to my server",'utf-8'))
    c.close()