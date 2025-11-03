import xmlrpc.client 
proxy=xmlrpc.client.ServerProxy("http://localhost:8000/") 
for i in range(5): 
    a=int(input("Enter a number:")) 
    b=int(input("Enter b number:")) 
    print("addition of given number is %d "%((proxy.add(a,b)))) 
    print("sub of given number is %d "%((proxy.sub(a,b)))) 
    print("multiplication of given number is %d "%((proxy.mul(a,b)))) 
    print("division of given number is %d "%((proxy.div(a,b)))) 
    print("mod of given number is %d "%((proxy.mod(a,b)))) 
