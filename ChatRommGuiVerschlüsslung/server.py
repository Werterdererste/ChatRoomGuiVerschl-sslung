import socket


class server():

    def __init__(self):
        self.__ip = "127.0.0.1"
        self.__port = 5000

    def start(self):
        print("m")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__ip, self.__port))
            s.listen()
            print ("socket is listening")           

            while True:
 
                c, addr = s.accept()    
 
                c.send('Thank you for connecting'.encode())
 
   
  

