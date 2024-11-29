# -*- coding: utf-8 -*-
"""
Redes de Computadoras 2024-2
Actividad 5 - Programación de sockets
Envío de archivos - Lado Cliente
"""

import socket                   # Importa el módulo Socket
s = socket.socket()             # Crea el objeto socket
host = socket.gethostname()     # Obtiene el nombre de la PC local
port = 60000                    # Reserva un PUERTO para el servicio

s.connect((host, port))
s.send(b"Hola Servidor!")

with open('archivo_recibido.txt', 'wb') as f:
    print('Archivo abierto')
    while True:
        print('Recibiendo datos...')
        data = s.recv(1024)
        print('datos = %s', (data))
        if not data:
            break
        # Escribe los datops en un archivo
        f.write(data)

f.close()
print('Archivo recibido exitosamente')
s.close()
print('Conexión cerrada')
