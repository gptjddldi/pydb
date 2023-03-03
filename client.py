
import socket

class Client:
    def __init__(self):
      self.port = 10002
      self.host = "localhost"

      self.socket = socket.socket()
      self.connect()

    def connect(self):
        self.socket.connect((self.host, self.port))
        
    def ping(self):
        self.socket.sendall("ping".encode())
        recv = self.socket.recv(1024)
        print(recv.decode())
    
if __name__ == '__main__':
  c = Client()
  c.ping()