import socket
from threading import Thread
import tkinter as tk


class client:
    def __init__(self, root, listbar):
        self.__ip = "127.0.0.1"
        self.__port = 5000
        self.__serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__listbox = listbar

    def conect_to_server(self):
        try:
            self.__serversocket.connect((self.__ip, self.__port))
            Thread(target=self.emfangeNachrichten).start()
        except:
            print("keine verbindung zum server moeglich")
            self.__serversocket.close()
        
    def disconect_to_server(self):
        self.__serversocket.close()

    def send_nachricht(self, nachricht):
        try:
            self.__serversocket.send(nachricht.encode())
        except:
                print("conection lose")

    def emfangeNachrichten(self):
        while True:
            try:
                msg = self.__serversocket.recv(1024).decode()
                self.nachrichtAnzeigen(msg)
            except:
                exit()

    def nachrichtAnzeigen(self, msg):
        self.__listbox.insert("end", msg)
