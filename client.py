import socket

MAC_ADRESS = "7C:70:DB:59:B6:17"
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("7C:70:DB:59:B6:17", 4))
print("connected")
try:
	while True:
		client.send(input("message to send :").encode('utf-8'))	
		data = client.recv(1024)
		if not data:
			break
		print(data.decode('utf-8'))
except OSError as se:
	pass

client.close()
server.close()
