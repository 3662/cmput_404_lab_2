"""
I used the "Code for Lab 2" on eclass as reference
"""

import socket

bufsize = 4096

# create a new TCP socket
s = socket.socket() 

# reuse the same bind port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# host: symbolic name meaning all available interfaces
host = ""

# port: arbitrary non-privileged port
port = 8001

# bind socket to address
s.bind((host, port))

# set listening mode 
s.listen(1)

# listen for connections
while True:
    conn, addr = s.accept()

    # received data
    data = conn.recv(bufsize)

    # echo data back 
    conn.sendall(data)
    conn.close()
