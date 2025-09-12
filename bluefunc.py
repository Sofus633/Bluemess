RUNNING = True

def send_message(message, client):
    client.send(message.encode('utf-8'))


def erase_line():
    print("\033[F\033[2K", end="")


def wait_for_response(client, time):
    act = time.time() + time
    while (time.time() < act):
        data = client.recv(1024)
        if not data:
            break
        return data.decode('utf-8')


def display_newmessage(client):
    global RUNNING
    while (RUNNING):
        data = client.recv(1024)
        if not data:
            break
        erase_line()
        print(data.decode('utf-8'))
        #print("enter ur message :", flush=True, end="")


def try_connect(adress):
    global CANAL
    global server
    #try:
    server.bind((adress, CANAL))
    server.listen(1)
    client, addrr = server.accept()
    #if identificate(client):
    #    return client
    return client
    #except:
    #    CANAL -= 1
    #    return 0


"""def scan_bluetooth():
    devices_found = []
    new_devices = bluetooth.discover_devices(
        duration=8, lookup_names=True, lookup_class=True)
    for addr, name, device_class in device:
        tmp = try_connect(addr)
        if tmp:
            devices_found.append(tmp[0])
    return devices_found
"""

def identificate(client):
    send_message("AUTH", client)
    if wait_for_response(client, 10):
        return 1
    return 0


def send_newmessage(client):
    global RUNNING
    while (RUNNING):
	#print("\033
        message = input("Enter Your Message :")
        if message == "/stop":
            RUNNING = False
            break
        send_message(message, client)
        erase_line()
        print(message)
        #print("enter ur message :", flush=True, end="")


