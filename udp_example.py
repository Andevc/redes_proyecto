# Server UDP
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server=socket.gethostbyname(socket.gethostname())
print(f'Servidor comenzo en {server}')
print('Socket creado con exito')
port=56789
s.bind((server, port))
print(f'socket esperando en el puerto {port} y el servidor {server}')
print('ecuchando')
while True:
    mensaje, direccion=s.recvfrom(1024)
    print('Se coneccto', direccion)
    print(f'mensaje recivido: {mensaje}')
    mensaje=mensaje.upper()
    s.sendto(mensaje, direccion)
    if str(mensaje).__contains__('EXIT'):
        break
print('fin de conexcion')
s.close()



# Client UDP
import socket

clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message=b'test'
port=56789
addr=("127.0.1.1", port)
clientSocket.sendto(message, addr)
data, server=clientSocket.recvfrom(1024)
print(data)
clientSocket.close()