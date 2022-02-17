#!/usr/bin/env python3
import socket, time, threading

run=True
prompt="msg: "

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.5)
server.bind(('', 1234))

fulladdr=socket.getaddrinfo('localhost', 1234)
you=socket.getaddrinfo('localhost', 1234) [len(fulladdr)-1][len(fulladdr[0])-1][0]



def rec():
	while run:
		time.sleep(0.5)
		try:
			data, addr = server.recvfrom(1024)
			ip=addr[0]
			message=data.decode("utf-8")
			if message=="LOGIN_MSG":
				print(f"\n *** {ip} has joined the chat\n{prompt} ", end='')
				continue
			elif message=="LOGOUT_MSG":
				print(f"\n *** {ip} has left the chat\n{prompt} ", end='')
				continue


			print(f"\n{ip}: {message}\n{prompt} ", end='')
		except:
			continue

t=threading.Thread(target=rec)
t.start()
print("megchat v1.0")
print(f"You're {you}")

server.sendto(b"LOGIN_MSG", ('<broadcast>', 1234))
print("msg: ",end='')
while run:
	msg=bytes(input(), "utf-8")
	if msg==b"q":
		print("Exiting")
		run=False
		server.sendto(b"LOGOUT_MSG", ('<broadcast>', 1234))
		server.close()
		t.join()
		break
	elif msg:
		server.sendto(msg, ('<broadcast>', 1234))
	elif not msg:
		print(prompt,end='')
