<<<<<<< HEAD
#!/usr/bin/env python

from socket import *
from threading import Thread
import sys

def read_info(filename):
	try:
		info = open(filename)
	except IOError:
		print "could not find client.info file"
		sys.exit()
	
	string = ""
	for line in info:
		string = string + line.strip()
	info.close()
	return string

def recv():
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data: sys.exit(0)
        print data


if __name__ == "__main__":
	HOST = '192.168.1.5'
	PORT = 1234
	BUFSIZE = 1024
	ADDR = (HOST, PORT)

	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	Thread(target=recv).start()
	tcpCliSock.send('{"username":"dan"}\n')
	while True:
		data = raw_input('>')
		tcpCliSock.send(data)
	
=======
#!/usr/bin/env python

from socket import *
from threading import Thread
import sys, json

def to_json_string(diction):
	return json.dumps(diction)
	
def from_json_string(string):
	return json.loads(string)
	
def construct_message(msg):
	return '{"username":"'+info['username']+'", "message":"'+msg+'"}'

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

def recv():
	while True:
		data = tcpCliSock.recv(BUFSIZE)
		if not data:
			sys.exit(0)
		try:
			det = from_json_string(data)
			if not (det['username'] == info['username']): 
				print det['username'],">", det['message']
		except ValueError:
			pass

if __name__ == "__main__":
	json_string = read_info("client.info")
	print json_string
	info = from_json_string(json_string)
	HOST = info['host']
	PORT = int(info['port'])
	BUFSIZE = 1024
	ADDR = (HOST, PORT)
	
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	Thread(target=recv).start()
	tcpCliSock.send('{"username":"'+info['username']+'"}\n')
	while True:
		data = raw_input('>')
		tcpCliSock.send(construct_message(data))
	
>>>>>>> Fixed Bugs
