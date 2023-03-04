import socket

class Client:
    def __init__(self, host="localhost", port=10002):
      self.host = host
      self.port = port

      self.socket = socket.socket()
      self.connect()

    def connect(self):
        self.socket.connect((self.host, self.port))

    def ping(self):
        self.send_recv("ping")
      
    def close(self):
       self.socket.close()

    def set(self, key, value):
      self.send_recv(f"set {key} {value}")
      
    def get(self, key):
      self.send_recv(f"get {key}")    
    
    def send_recv(self, cmd):
      self.socket.sendall(cmd.encode())
      recv = self.socket.recv(1024)
      print(recv.decode())
    
    
if __name__ == '__main__':
  c = Client()
  c.ping()
  c.set("hihi", "22")
  c.get("hihi")
  c.get("hi")
  c.close()
  print(123)