import socket

server = socket.socket(socker.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTRPROTO_RFCOMM)
client.connect((MAC_ADRESS, 4))

try:
	while True:
		client.send(Input("message to send :"))	
		data = client.recv(1024)
		if not date:
			break
		print(data.decode('utf-8'))
except OSRrror as se:
	pass

client.close()
server.close()
