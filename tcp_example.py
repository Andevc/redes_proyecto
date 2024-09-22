# Server TCP

import socket

HOST="127.0.0.1"  # interfaz standar de retorno (localhost)
PORT=56789  # puerto de escucha (sin-privilegio son > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr=s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data=conn.recv(1024)
            if not data:
                break
            conn.sendall(data.lower())


# Client TCP
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 56789  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Recivido {data}")