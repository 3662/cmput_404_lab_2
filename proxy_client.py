import socket 

BUFSIZE = 4096

HOST_CLIENT = ""
PORT_CLIENT = 8001

def main():
    s = socket.socket() 
    s.connect((HOST_CLIENT, PORT_CLIENT))

    s.sendall(f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'.encode())

    data = b""

    while True:
        temp = s.recv(BUFSIZE)

        if not temp:
            break

        data += temp

    print(data)

    s.close()

main()
