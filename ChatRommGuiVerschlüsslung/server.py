import socket
from _thread import *

class server:
    def __init__(self):
        self.__ip = "127.0.0.1"
        self.__port = 5000
        self.__clientlist = []

    def thred_client(self, clientSocket):
        while True:
            try:
                msg = clientSocket.recv(1024)
                self.weiterleiten(msg, clientSocket)
            except:
                print("client disconect")
                for i  in self.__clientlist:
                    if i == clientSocket:
                        self.__clientlist.remove(i)
                clientSocket.close()
                exit()      

    def weiterleiten(self, msg, clientSocket):
        for i in self.__clientlist:
            if i != clientSocket:
                i.send(msg)

    def start(self):
        print("server start")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
            serverSocket.bind((self.__ip, self.__port))
            self.lisenForClients(serverSocket)

    def lisenForClients(self, serverSocket):                   
        serverSocket.listen(1)
        while True:
            clientSocket, addr = serverSocket.accept()
            name = clientSocket.recv(1024)
            print("Client Conect:"+ name.decode())
            self.__clientlist.append(clientSocket)
            start_new_thread(self.thred_client, (clientSocket, ))

if __name__ == "__main__":
    program1 = server()
    program1.start()