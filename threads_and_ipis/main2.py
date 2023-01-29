import ipaddress

ip = "192.168.0.1"

# showing as IP
address_ip = ipaddress.ip_address(ip)
print(address_ip)

# calculation with IP
print(address_ip + 257)

ip_network = "192.168.0.0/24"
network = ipaddress.ip_network(ip_network, strict=False)
print(network)
