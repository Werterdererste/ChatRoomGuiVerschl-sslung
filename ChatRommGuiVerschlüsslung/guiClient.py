import tkinter as tk
from client import client
from threading import Thread


class guiClient:
    def __init__(self):
        self.__root = tk.Tk()

        self.__eingabe = tk.Entry(self.__root)
        self.__listbar = tk.Listbox(self.__root)
        self.__button = tk.Button(self.__root, text="--->", command=self.senden)

        self.__client = client(self.__root, self.__listbar)

    def senden(self):
        tk.Label(self.__listbar, text=self.__eingabe.get(), bg="#80ff80").pack(
            anchor="e", side="top", padx=5, pady=5, ipadx=5, ipady=5
        )
        self.__client.send_nachricht(self.__eingabe.get())
        self.__eingabe.delete(0, "end")

    def start(self):
        self.__client.conect_to_server()

        self.__root.title("chat")
        self.__root.geometry("400x600")
        self.__root.resizable(width=False, height=False)
        self.__root.configure(bg="#ffffff")

        self.__root.grid_rowconfigure(0, weight=2)
        self.__root.grid_columnconfigure(1, weight=2)

        self.__listbar.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="nsew",
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
        )
        self.__eingabe.grid(
            row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5, ipadx=5, ipady=5
        )
        self.__button.grid(
            row=1, column=2, sticky="se", padx=5, pady=5, ipadx=5, ipady=5
        )

        self.__root.mainloop()
        self.__client.disconect_to_server()