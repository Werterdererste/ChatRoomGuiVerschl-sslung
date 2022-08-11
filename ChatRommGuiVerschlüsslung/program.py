from guiClient import guiClient
from server import server
from threading import Thread


class program:
    def ServerStart(self):
        server1 = server()
        server1.start()

    def ClientStart(self):
        guiClient1 = guiClient()
        guiClient1.start()

    def main(self):
        Thread(target=self.ServerStart).start()

        Thread(target=self.ClientStart).start()
        Thread(target=self.ClientStart).start()
        # Thread(target=self.ClientStart).start()

if __name__ == "__main__":
    program1 = program()
    program1.main()