import socket
from _thread import *

class client():
    
    def __init__(self):
        self.__ip = "127.0.0.1"
        self.__port = 5000
        print("I")
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conect_to_server(self):
        print("g")
        self.__s.connect((self.__ip, self.__port))
        #start_new_thread(self.emfangeNachrichten())

    def send_nachricht(self ,nachricht):       
            self.__s.send(nachricht.encode())

    def emfangeNachrichten(self):
        print(self.__s.recv(1024).decode()) 