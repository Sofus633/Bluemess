import socket

server = socket.socket(socker.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTRPROTO_RFCOMM)
server.bind((MAC_ADRESS, 4))

client, addr = server.accept()

try:
	while True:
		data = client.recv(1024)
		if not date:
			break
		print(data.decode('utf-8'))
		client.send(Input("message to send :"))
except OSRrror as se:
	pass

client.close()
server.close()
