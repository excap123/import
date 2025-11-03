
import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('UDP Socket Created')

sockfd.bind(('localhost', 55555))
print('Waiting for client messages')

while True:
    receivedMsg, addr = sockfd.recvfrom(1024)
    receivedMsg = receivedMsg.decode()
    print("Connected with ", addr)
    print("Message Received from Client: ", receivedMsg)
    sockfd.sendto(bytes(receivedMsg, 'utf-8'), addr)
    print("Message reply sent to Client!")
    print("Do you want to continue(type y or n):")
    choice = input()
    if choice == 'n':
        break


