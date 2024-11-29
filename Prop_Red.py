import ipaddress

net_IN = input("Ingrese la subred/mascara = ")

net = ipaddress.IPv4Network(net_IN,strict=False)

print("Direccion de red =",net.network_address)

print("Direccion de red =",net.broadcast_address)

print("Mascara de red =",net.netmask)

print("Red y mascara de host =",net.with_hostmask)

print("Longitud de Mascara de Red =",net.prefixlen)

print("Numero de hosts =",net.num_addresses-2)


