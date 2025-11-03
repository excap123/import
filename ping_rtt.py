import socket, time 
host = "google.com" 
port = 80 
count = 4 
times = [] 
 
for i in range(count): 
    try: 
        s = socket.socket() 
        start = time.time() 
        s.connect((host, port)) 
        end = time.time() 
        s.close() 
        rtt = (end - start) * 1000 
        times.append(rtt) 
        print(f"Reply from {host}: time={rtt:.2f} ms") 
    except: 
        print("Request timed out") 
if times: 
    print("\nMin RTT =", min(times), "ms") 
    print("Max RTT =", max(times), "ms") 
    print("Avg RTT =", sum(times)/len(times), "ms") 
