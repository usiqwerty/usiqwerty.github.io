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


def getfile(fn, ip):
	print(f"Getting {fn} from {ip}")
	s = socket.socket()
	f = open(fn,'wb')
	s.connect((ip,1212))
	if s:
		print("TCP connection started")
		size=0
		l = '1'
		while l:
			l = s.recv(1024)
			size+=len(l)
			f.write(l)
			print ( str(size/1024) + " kbytes received")

		f.close()
		s.close()
		print("TCP connection closed")
	else:
		print("Connection refused")
def sendfile(fn):
	print(f"Sending {fn}...")
	s = socket.socket()         # Create a socket object
	s.bind(('', 1212))        # Bind to the port
	s.settimeout(10)
	f = open(fn,'rb')
	s.listen(5)
	c, addr = s.accept()     # Establish connection with client.
	print(f"{addr} accepted TCP connection")

	l = f.read(1024)
	size=len(l)
	while l:
		c.send(l)
		print (str(size/1024) + " kbytes sent")
		l = f.read(1024)
		size+=len(l)
	c.shutdown(2)
	f.close()
	s.close()
	print("TCP connection closed")
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
			elif "FILE_ALERT" in message:
				fn=message.split(':')[1]
				r=True if input("Save file y/n? ") == "y" else False
				if r:
					getfile(fn, ip)
					print(f"\n{prompt} ", end='')


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
		t.join()
		server.close()
		break
	elif msg==b"sendfile":
		fn=input("Filename: ")
		server.sendto(b"FILE_ALERT:"+bytes(fn, 'utf-8'), ('<broadcast>', 1234))
		sendfile(fn)

	elif msg:
		server.sendto(msg, ('<broadcast>', 1234))
	elif not msg:
		print(prompt,end='')
