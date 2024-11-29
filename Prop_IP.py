import ipaddress

ip_IN = input("Ingrese la IP_HOST = ")
print("\n")
ip = ipaddress.ip_network(ip_IN, strict=False)

print("Bits en la IP =",ip.max_prefixlen)

print("Multicast =",ip.is_multicast)

print("Privada =",ip.is_private)

print("Publica",ip.is_global)

print("Reservada",ip.is_reserved)

print("Loopback =",ip.is_loopback)

ip1 = ip + 1
print("Proxima direccion IP :",ip1)
ip2 = ip-1
print("Ip Anterior:",ip2)


