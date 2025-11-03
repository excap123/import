import socket 
clientfd=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
clientfd.connect(('localhost',55555)) 
name=input("Enter your message:") 
clientfd.send(bytes(name,'utf-8')) 
print("Message Received from Server: ",clientfd.recv(1024).decode()) 
