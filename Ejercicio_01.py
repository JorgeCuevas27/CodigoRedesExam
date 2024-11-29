#Ejercicio 01: Conexión con el servidor de Google
#Importar librería de sockets

import socket
#Creación del socket llamado "S".
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ("Socket creado exitosamente")

#Obtener la ip de Google.
ip = socket.gethostbyname("www.google.com")
print (ip)

#Indicar que se conectará al puerto 80: 
port = 80

s.connect((ip,port))

print("Conexión OK")
print("Dirección de host: ", ip)
print("Níumero de puerto: ", port)