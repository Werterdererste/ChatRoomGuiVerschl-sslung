import tkinter as tk
from turtle import width
from client import client
from threading import Thread


class guiClient:
    def __init__(self):
        self.__root = tk.Tk()

        self.__entry = tk.Entry(self.__root)
        self.__listbox = tk.Listbox(self.__root)
        self.__scrollbar = tk.Scrollbar(self.__root)
        self.__sendbutton = tk.Button(self.__root, text="--->", command=self.senden)

        self.__name = "xx"
        self.__client = client(self.__listbox)

    def senden(self):
        if self.__entry.get():
            self.__listbox.insert("end", "You: " + self.__entry.get())
            self.__client.send_nachricht(self.__entry.get())
            self.__entry.delete(0, "end")

    def Chat(self):

        list = self.__root.grid_slaves()
        for l in list:
            l.destroy()
        self.__client.conect_to_server(self.__name)

        self.__root.title("chat")
        self.__root.geometry("400x600")
        self.__root.resizable(width=False, height=False)
        self.__root.configure(bg="#ffffff")

        self.__listbox.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="nsew",
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
        )
        self.__scrollbar.grid(
            row=0,
            column=2,
            sticky="nse",
            padx=5,
            pady=5,
        )
        self.__entry.grid(
            row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5, ipadx=5, ipady=5
        )
        self.__sendbutton.grid(
            row=3, column=2, sticky="se", padx=5, pady=5, ipadx=5, ipady=5
        )

        self.__listbox.configure(yscrollcommand=self.__scrollbar.set)
        self.__scrollbar.configure(command=self.__listbox.yview)

        self.__root.mainloop()
        self.__client.disconect_to_server()

    def Anmelden(self, username):
        if username.get():
            self.__name = username.get()
            self.Chat()

    def Login(self):

        self.__root.title("login")
        self.__root.geometry("300x200")
        self.__root.resizable(width=False, height=False)

        self.__root.grid_rowconfigure(0, weight=2)
        self.__root.grid_columnconfigure(1, weight=2)

        tk.Label(self.__root, text="Username").grid(row=0, column=1, padx=15, pady=20)

        username = tk.Entry(self.__root)
        username.grid(row=1, column=1, padx=5, pady=20)
        tk.Button(
            self.__root, text="Anmelden", command=lambda: self.Anmelden(username)
        ).grid(row=2, column=1, padx=15, pady=20, ipadx=5, ipady=5)

        self.__root.mainloop()

if __name__ == "__main__":
    program1 = guiClient()
    program1.Login()