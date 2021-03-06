#!/usr/bin/env python

import socket, threading, sys, json

def get_users():
	return_val = ""
	for client in clients:
		return_val = return_val + client.user_data['username']+"\n"
	return return_val

def read_info(filename):
	try:
		info = open(filename)
	except IOError:
		print "could not find client.info file"
		sys.exit()
	
	string = ""
	for line in info:
		string = string + line
	info.close()
	return string

def to_json_string(diction):
	return json.dumps(diction)
	
def from_json_string(string):
	return json.loads(string)

def send_users(messege):
	for client in clients:
		client.socket.send(messege)

#checks if username is already in use, True/False
def user_exists(username):
	for client in clients:
		if(client.user_data['username'] == username or client.user_data['username'] == "SERVER"):
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
	client.socket.send(to_json_string(j)+"\n")

def mass_server_messege(message):
	j = {"message":message, "username":"SERVER"}
	for client in clients:
		client.socket.send(to_json_string(j)+"\n")

def disconnect(client, send_messege):
	lock.acquire()
	clients.remove(client)
	lock.release()
	if send_messege:
		mass_server_messege(client.user_data['username']+" has disconnected"+"\n")

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
			mass_server_messege(self.user_data['username']+" is online")
		except ValueError:
			print "Failed to recieve details from", self.address
			disconnect(self, True)
			return 0
		
		while True:
			try:
				messege = self.socket.recv(1024)
				message_info = from_json_string(messege)
				if message_info['message'] == "/users":
					server_messege(self, get_users())
				print messege
				if not messege:
					print "disconnecting"
					break
				send_users(messege+"\n")
			except Exception, e:
				print str(e)
				break
		self.socket.close()
		print "Dissconnected from", self.address
		disconnect(self, True)
	


if __name__ == "__main__":
	variables_string = read_info("server.info")
	variables = from_json_string(variables_string)
	host = ""
	port = variables['port']
	print port
	clients = []
	usernames = []
	lock = threading.Lock()
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host, port))
	sock.listen(5)
	
	while True:
		Server(sock.accept()).start()
