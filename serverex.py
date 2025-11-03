import socket 
sockfd=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print('Socket Created') 
sockfd.bind(('localhost',55555)) 
sockfd.listen(3) 
print('Waiting for connections') 
while True: 
    clientfd,addr=sockfd.accept() 
    receivedMsg=clientfd.recv(1024).decode() 
    print("Connected with ",addr) 
    print("Message Received from Client: ",receivedMsg) 
    clientfd.send(bytes(receivedMsg,'utf-8')) 
    print("Message reply sent to Client!") 
    print("Do you want to continue(type y or n):") 
    choice=input() 
    if choice=='n': 
        break 
