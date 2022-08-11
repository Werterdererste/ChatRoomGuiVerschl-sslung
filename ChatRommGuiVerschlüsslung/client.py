import socket
from threading import Thread
import tkinter as tk


class client:
    def __init__(self, root, listbar):
        self.__ip = "127.0.0.1"
        self.__port = 5000
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__listbar = listbar

    def conect_to_server(self):
        self.__s.connect((self.__ip, self.__port))
        Thread(target=self.emfangeNachrichten).start()

    def send_nachricht(self, nachricht):
        self.__s.send(nachricht.encode())

    def emfangeNachrichten(self):
        while True:
            print("emfange")
            msg = self.__s.recv(1024).decode()
            self.nachrichtAnzeigen(msg)

    def nachrichtAnzeigen(self, msg):
        tk.Label(self.__listbar, text=msg, bg="#f2f2f2").pack(
            anchor="w", side="top", padx=5, pady=5, ipadx=5, ipady=5
        )
