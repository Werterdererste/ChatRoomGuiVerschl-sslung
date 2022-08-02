import socket
from _thread import *


class server():

    def __init__(self):
        self.__ip = "127.0.0.1"
        self.__port = 5000
        self.__clientlist = []

    def thred_client(self, clientSocket):
        while True:
            msg = clientSocket.recv(1024).decode() 
            self.weiterleiten(msg, clientSocket)

    def weiterleiten(self, msg, clientSocket):
        for i in self.__clientlist:
            if i != clientSocket:
                print("send")
                i.send(msg)

    def start(self):
        print("m")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
            serverSocket.bind((self.__ip, self.__port))
            serverSocket.listen(10)
            self.lisenForClients(serverSocket)
            
    def lisenForClients(self, serverSocket):
        while True: 
            clientSocket, addr = serverSocket.accept()
            self.__clientlist.append(clientSocket)
            start_new_thread(self.thred_client, (clientSocket,))

if __name__ == "__main__":
    program1 = server()
    program1.start()
