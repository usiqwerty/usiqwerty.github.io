# Thanks to @stevenreddie
import socket, time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(('',12345))
client.sendto(b"I have joined the chat!", ('<broadcast>', 12345))
client.recvfrom(1024)
client.sendto(bytes(input("You: "),'utf-8'), ('<broadcast>', 12345))
a=0
while True:
	if a!=1:
		client.settimeout(0.1)
		try:
			data, addr = client.recvfrom(1024)
			print (addr[0], ": ", data.decode('utf-8'))
		except socket.timeout:
			client.settimeout(None)
	a=0
	msg=input("You: ")
	if msg=="/exit":
		break
	if msg!="":
		client.sendto(bytes(msg,'utf-8'), ('<broadcast>', 12345))
	else:
		client.settimeout(0.1)
		try:
			data, addr = client.recvfrom(1024)
			print (addr[0], ": ", data.decode('utf-8'))
		except socket.timeout:
			client.settimeout(None)
			a=1
			continue
client.close()
