import socket
from multiprocessing import Process

BUFSIZE = 1024

HOST_CLIENT = socket.gethostbyname("www.google.com")
PORT_CLIENT = 80

HOST_SERVER = ""
PORT_SERVER = 8001

def handle_connection(conn, addr):
    print("Connection:", addr)

    data = conn.recv(BUFSIZE)
    print("Received request {} from {}".format(data, addr))

    # create a client socket to redirect data to HOST_CLIENT
    client_socket = socket.socket()
    client_socket.connect((HOST_CLIENT, PORT_CLIENT))

    print("Redirecting request from {} to {}".format(addr, HOST_CLIENT))
    client_socket.sendall(data)
    client_socket.shutdown(socket.SHUT_WR)

    response = b""

    while True:
        temp = client_socket.recv(BUFSIZE)

        if not temp:
            break

        response += temp

    client_socket.close()

    print("Redirecting response from {} to {}".format(HOST_CLIENT, addr))
    conn.sendall(response)
    conn.shutdown(socket.SHUT_WR)
    conn.close()

def main():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST_SERVER, PORT_SERVER))

    server_socket.listen()

    while True:
        conn, addr = server_socket.accept()

        # create an independent process to handle each connection
        p = Process(target=handle_connection, args=(conn, addr))
        
        p.daemon
        p.start()
        

main()