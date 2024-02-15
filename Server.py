import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5000
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("Connection closed".encode(FORMAT))
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1} ")

print("[STARTING] server is starting ..")
start()