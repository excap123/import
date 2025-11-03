import socket

clientfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = input("Enter your message: ")
clientfd.sendto(bytes(name, 'utf-8'), ('localhost', 55555))

receivedMsg, server = clientfd.recvfrom(1024)
print("Message Received from Server: ", receivedMsg.decode())
