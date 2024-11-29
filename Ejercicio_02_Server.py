#importar la librer√≠a socket
import socket

#crear el socket
s=socket.socket()
print ("socket creado exitosamente")
port = 12345

s.bind(('',port))

print("El socket esta enlazado a: ", port)

s.listen(5)

print ("El socket est· en modo escucha")

while True:
    con, addr = s.accept()
    print("conexion recibida de: ", addr)
    con.send(b'Gracias por conectarse')
    con.close()