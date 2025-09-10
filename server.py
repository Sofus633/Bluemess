import socket
import threading


RUNNING = True

server = socket.socket(socket.AF_BLUETOOTH,
socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("50:84:92:E6:14:B8", 4))
server.listen(1)
client, addr = server.accept()
print("server accepted")


def send_message(message, client):
    client.send(message.encode('utf-8'))


def erase_line():
    print("\033[F\033[2K", end="")


def display_newmessage(client):
    global RUNNING
    while (RUNNING):
        data = client.recv(1024)
        if not data:
            break
        erase_line()
        print(data.decode('utf-8'))
        print("enter ur message :", flush=True, end="")


def send_newmessage(client):
    global RUNNING
    while (RUNNING):
        message = input("")
        if message == "/stop":
            RUNNING = False
            break
        send_message(message, client)
        erase_line()
        print(message)
        print("enter ur message :", flush=True, end="")


"""try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
        send_message(input("message to send :"), client)
except OSError as se:
    pass
"""
try:
    t1 = threading.Thread(target=display_newmessage, args=(client,))
    t2 = threading.Thread(target=send_newmessage, args=(client,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
except OSError as se:
    pass

client.close()
server.close()
