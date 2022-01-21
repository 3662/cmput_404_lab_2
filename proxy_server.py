import socket

BUFSIZE = 4096

HOST_CLIENT = socket.gethostbyname("www.google.com")
PORT_CLIENT = 80

HOST_SERVER = ""
PORT_SERVER = 8001

def main():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST_SERVER, PORT_SERVER))

    server_socket.listen(1)

    while True:
        conn, addr = server_socket.accept()
        print("Connection:", addr)

        data = conn.recv(BUFSIZE)
        print("Received request {} from {}".format(data, addr))

        # create a client socket to redirect data to HOST_CLIENT
        client_socket = socket.socket()
        client_socket.connect((HOST_CLIENT, PORT_CLIENT))

        print("Redirecting request from {} to {}".format(addr, HOST_CLIENT))
        client_socket.sendall(data)

        response = b""

        while True:
            temp = client_socket.recv(BUFSIZE)

            if not temp:
                break

            response += temp

        print("Redirecting response from {} to {}".format(HOST_CLIENT, addr))
        conn.sendall(response)

        conn.close()

main()