import socket

##!!press 1 to exit dialogue with server!!
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = input("Enter Server Ip : ")
PORT = int(input("Enter Server Port : "))
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

msg = input("Enter message : ")
while msg != '1':
    send(msg)
    msg = input("Enter message : ")
send(DISCONNECT_MESSAGE)
