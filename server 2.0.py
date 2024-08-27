import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('192.168.56.1', 8888))
print('192.168.56.1', ':', 8888)
print("сервер запущен")


class ClientTread(threading.Tread):

    def __init__(threading, Thread):
        threading, Thread.__init__(self)
        self.csocket = clientsocket
        print("Новое подключение: ", clientAddress)
        
    def run(self):
        message = ''
        while True:
            data = self.csocket.recv(4096)
            message = data.decode('utf-8')
            print(message)

while True:
    server listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    nwethread.start()
