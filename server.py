import socket
import threading
#import bluetooth
import time
import bluefunc

RUNNING = True
CANAL = 4
#ppls = []

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("50:84:92:E6:14:B8", CANAL))
server.listen(1)
client, addr = server.accept()

print("connected")


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
"""
macth = "7C:70:DB:5A:79:6C"
maccla = "50:84:92:E6:14:B8"
client = try_connect()"""
print("server accepted")




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
