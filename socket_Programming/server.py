import socket
s = socket.socket()         # by de fault it is IP4 and tcp
print('Socket Created')

s.bind(('localhost',9999))        # port number range 0  to 65535

s.listen(3)
print('Waiting for  connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Connected with ', addr, name)

    c.send(bytes('wellcome to Ritam Pharmacy','utf-8'))  # for coverting string as byte format,utf-8 is byte format
    c.close()