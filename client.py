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
	HOST = 'localhost'
	PORT = 1234
	BUFSIZE = 1024
	ADDR = (HOST, PORT)

	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	Thread(target=recv).start()
	#tcpCliSock.send("{'username':'joe'}\n")
	while True:
		data = raw_input('>')
		print data
		tcpCliSock.send(data)
	