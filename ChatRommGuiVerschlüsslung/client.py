import socket

class client():
    
    def __init__(self):
        self.__ip = "127.0.0.1"
        self.__port = 5000

    def conect_to_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.__ip, self.__port))

            print (s.recv(1024).decode())
    