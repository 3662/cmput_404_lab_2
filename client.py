"""
I used the "Code for Lab 2" on eclass as reference
"""

import socket

bufsize = 4096

# create a new TCP socket
s = socket.socket() 

# host: hostname in internet domain notation or IPv4 address
host = socket.gethostbyname("www.google.com")

# port: usually 80
port = 80

# connect to www.google.com
# address (host, port) used for the AF_INET family
s.connect((host, port))

# send GET request
s.sendall(f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'.encode())

# received data from the socket
data = b""

while True:
    temp = s.recv(bufsize)

    if not temp:
        break

    data += temp

print(data)

s.close()

