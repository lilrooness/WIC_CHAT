#!/usr/bin/env python

import socket, threading, sys, json

def to_json_string(diction):
	return json.dumps(diction)
	
def from_json_string(string):
	return json.loads(string)

def send_users(messege):
	for client in clients:
		client.socket.send(messege)

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
		
		try:
			self.user_data = from_json_string(self.socket.recv(1024))
			print self.user_data['username']
			prompt = "SERVER_MESSEGE> "+self.user_data['username']+" is online\n"
		except ValueError:
			print "Failed to recieve details from", self.address
			lock.acquire()
			clients.remove(self)
			lock.release()
			return 0
			
		send_users(prompt)
		
		while True:
			messege = self.socket.recv(1024)
			print messege.strip()
			if not messege:
				break
			send_users(messege)
		
		self.socket.close()
		print "Dissconnected from", self.address
		lock.acquire()
		clients.remove(self)
		lock.release()	
	


if __name__ == "__main__":
	host = ""
	port = 1234
	clients = []
	usernames = []
	lock = threading.Lock()
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host, port))
	sock.listen(5)
	
	while True:
		Server(sock.accept()).start()
