#!/usr/bin/env python

import socket, threading, sys, json

class Server(threading.Thread):
	def __init__ (self, (socket, address)):
		threading.Thread.__init__(self)
		self.socket = socket
		self.address = address
	
	
	def run(self):
		lock.acquire()
		clients.append(self)
		lock.release()
		print "Connected to", self.address
		
		while True:
			message = self.socket.recv(1024)
			print message.strip()
			if not message or message == "END".strip():
				break
			for client in clients:
				client.socket.send(message)
		
		self.socket.close()
		print "Dissconnected from", self.address
		lock.acquire()
		clients.remove(self)
		lock.release()
	
	
	def to_json_string(diction):
		return json.dumps(diction)
	
	def from_json_string(string):
		return json.loads(string)
	


if __name__ == "__main__":
	host = ""
	port = 1234
	clients = []
	lock = threading.Lock()
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host, port))
	sock.listen(5)
	
	while True:
		Server(sock.accept()).start()
	
	