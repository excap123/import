from xmlrpc.server import SimpleXMLRPCServer 
def add(a,b): 
    return a+b 
def sub(a,b): 
    return a-b 
def mul(a,b): 
    return a*b 
def div(a,b): 
    return a/b 
def mod(a,b): 
    return a%b 
server=SimpleXMLRPCServer(("localhost",8000)) 
print("Listening on port 8000...") 
server.register_function(add,"add") 
server.register_function(sub,"sub") 
server.register_function(mul,"mul") 
server.register_function(div,"div") 
server.register_function(mod,"mod") 
server.serve_forever() 
