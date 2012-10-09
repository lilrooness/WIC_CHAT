#!/usr/bin/env python

import socket, threading, sys, json

def to_json_string(diction):
	return json.dumps(diction)
	
def from_json_string(string):
	return json.loads(string)

def send_users(messege):
	for client in clients:
		client.socket.send(messege)

def user_exists(username):
	for client in clients:
		if(client.user_data['username'] == username):
			return True
	return False

def messege_prot(messege):
	data = from_json_string(messege)
	return data['protocol']	

def messege_username(messege):
	data = from_json_string(messege)
	return data['username']
	
def server_messege(client, message):
	j = {"message":message, "username":"SERVER"}
	client.socket.send(to_json_string(j))

def mass_server_messege(message):
	j = {"message":message, "username":"SERVER"}
	for client in clients:
		client.socket.send(to_json_string(j))

def disconnect(client, send_messege):
	lock.acquire()
	clients.remove(client)
	lock.release()
	if send_messege:
		mass_server_messege(client.user_data['username']+" has disconnected")

class Server(threading.Thread):
	def __init__ (self, (socket, address)):
		threading.Thread.__init__(self)
		self.socket = socket
		self.address = address
		self.user_data = {"username":"Server"}

	def run(self):
		lock.acquire()
		clients.append(self)
		lock.release()
		print "Connected to", self.address
		
		try:
			temp = from_json_string(self.socket.recv(1024).strip())
			
			#if useraname exists send error messege and break connection
			if user_exists(temp['username']):
				server_messege(self, "username already in use")
				disconnect(self, False)
				return 0
			self.user_data.clear()
			self.user_data = temp
			print self.user_data['username']
			mass_server_messege(self.user_data['username']+" is online\n")
		except ValueError:
			print "Failed to recieve details from", self.address
			disconnect(self, True)
			return 0
		
		while True:
			try:
				messege = self.socket.recv(1024)
				print messege
				if not messege:
					break
				send_users(messege)
			except Exception:
				break
		self.socket.close()
		print "Dissconnected from", self.address
		disconnect(self, True)
	


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
