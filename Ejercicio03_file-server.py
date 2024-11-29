# -*- coding: utf-8 -*-
"""
Redes de Computadoras
Actividad 5 - Programación de sockets
Envío de archivos - Lado Servidor
"""

import socket                   # Importa el módulo Socket
port = 60000                    # Reserva un PUERTO para el servicio
s = socket.socket()             # Crea un objeto socket
s.bind(('', port))            # Lo enlaza al puerto
s.listen(5)                     # Espera por la conexión de un Cliente

print ('Servidor escuchando ...')

while True:
    conn, addr = s.accept()     # Establece conexión con el Cliente
    print ('Conexión recibida de ', addr)
    data = conn.recv(1024)
    print ('Servidor recibido ', repr(data))

    filename='mi_texto2.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print ('Enviado ',repr(l))
       l = f.read(1024)
    f.close()

    print ('Terminó de enviar')
    conn.send(b'Gracias por conectarse')
    conn.close()