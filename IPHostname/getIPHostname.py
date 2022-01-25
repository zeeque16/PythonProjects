import socket
print("IP address is: " + socket.gethostbyname('google.com'))

ipaddress = socket.gethostbyname('google.com')

print("hostname: " + socket.gethostbyaddr(ipaddress)[0])

# print("hostname: " + socket.gethostname())