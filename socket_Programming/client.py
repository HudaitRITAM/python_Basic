import socket
c = socket.socket()         # by de fault it is IP4 and tcp

c.connect(('localhost',9999))   # ip address and port number of server

name= input("write your name ::")
c.send(bytes(name,'utf-8'))          # send client name to the server

print(c.recv(1024).decode())          # receive server massege