import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(("localhost", 1234))
mySocket.listen(1)
while True:
    channel, details = mySocket.accept();
    print "We have opened a connection with", details
    print channel.recv (100)
    channel.send("Winter is Comming")
    channel.close()
