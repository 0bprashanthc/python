import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(sys.argv[1],('127.0.0.1',1234))
