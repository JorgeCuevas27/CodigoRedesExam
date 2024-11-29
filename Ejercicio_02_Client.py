import socket
S =socket.socket()

port = 12345

S.connect (('127.0.0.1', port))

print (S.recv(1024))

S.close