import tkinter as tk
from client import client

class guiClient():

    def __init__(self):
        self.__root = tk.Tk()        
        self.__eingabefeldWert = tk.StringVar()
        self.__client = client()


    def senden(self):
        tk.Label(self.__root, text=self.__eingabefeldWert.get()).pack(anchor="e" ,side="top")
        self.__client.send_nachricht(self.__eingabefeldWert.get())
        self.__eingabefeldWert.set("")

    def start(self):
        self.__client.conect_to_server()

        self.__root.title("chat")
        self.__root.geometry("400x600")
        self.__root.resizable(width=False, height=False)

        tk.Entry(self.__root, textvariable = self.__eingabefeldWert).pack(anchor="s", side="left", expand=True, fill="x", padx=10, pady = 10, ipady = 5)
        tk.Button(self.__root, text ="--->", command = self.senden).pack(anchor="s", side="left" , padx=10, pady = 10, ipady = 5)

        self.__root.mainloop()







if __name__ == "__main__":
    program1 = guiClient()
    program1.start()