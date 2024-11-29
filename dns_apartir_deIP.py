import socket
ip_TN = input("Ingresar IP =")

try:
    dominio = socket.gethostbyaddr(ip_TN)[0]
    print("La IP %s tiene una entra DNS: %s"%(ip_TN,dominio))

except socket.error as msg:
    print("%s:%s"%(ip_TN,msg))
    
