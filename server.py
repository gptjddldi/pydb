import threading
import socket


def handle(conn, addr):
    while True:
        data = str(conn.recv(1024), 'ascii')
        print(data)
        cur_thread = threading.current_thread()
        response = bytes("pong", 'ascii')
        conn.sendall(response)
        if data == 'bye':
            conn.close()
            break

if __name__ == "__main__":
    HOST, PORT = "localhost", 10002
    server  = socket.socket()
    server.bind((HOST, PORT))
    
    while True:
        server.listen(3)
        conn, addr = server.accept()
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=handle, args=(conn, addr))
        # Exit the server thread when the main thread terminates
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)


