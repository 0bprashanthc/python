import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',1234))

while True:
    d,ad = s.recvfrom(1024)
    print(d,ad)
