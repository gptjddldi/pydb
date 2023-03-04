import threading
import socket

class ThreadedServer(object):
    def __init__(self, host="localhost", port=10002):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.store = dict()
        self.sock.bind((self.host, self.port))
        
    def listen(self):
        self.sock.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target=self.handle_client, args=(client, address)).start()
            
    def handle_client(self, client, address):
        print(f"Client {address[0]}:{address[1]} connected.")

        while True:
            try:
                data = client.recv(1024).decode()
                if data:
                    client.send(self.parse_data(data).encode())
                else:
                    raise socket.error("Client disconnected")
            except:
                print(f"Client {address[0]}:{address[1]} disconnected.")
                client.close()
                return

    def parse_data(self, data):
        if (data.split(" ")[0] == "set"):
            k, v = data.split(" ")[1:]
            self.store[k] = v
            return "set"

        elif (data.split(" ")[0] == "get"):
            k = data.split(" ")[1]
            return self.store.get(k, "None")
        return "pong"


if __name__ == "__main__":
    server = ThreadedServer()
    server.listen()
