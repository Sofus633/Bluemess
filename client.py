import socket
import threading
from bluefunc import *
from multiprocessing import Process 

MAC_ADRESS = "7C:70:DB:59:B6:17"
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
print("socket set looking for host ...")
try :
	client.connect(("7C:70:DB:59:B6:17", 4))
except: #TODO handle errors
	print("connection fail ")
	exit()
print("connected")

"""try:
	while True:
		client.send(input("message to send :").encode('utf-8'))	
		data = client.recv(1024)
		if not data:
			break
		print(data.decode('utf-8'))
except OSError as se:
	pass
"""
"""try:
    t1 = threading.Thread(target=display_newmessage, args=(client,))
    t2 = threading.Thread(target=send_newmessage, args=(client,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
except OSError as se:
    pass²v
"""
try: 
    p = Process(target=send_newmessage, args=(client,))
    display_newmessage(client)
    p.start()
    p.join()
except OSError as se:
    pass


client.close()
server.close()
