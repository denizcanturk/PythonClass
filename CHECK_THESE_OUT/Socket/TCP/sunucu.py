import socket as sc

myPort = 61127

# Function to get local IP address
# def get_local_ip():
#     import netifaces
#     interfaces = netifaces.interfaces()
#     for iface in interfaces:
#         addrs = netifaces.ifaddresses(iface)
#         if netifaces.AF_INET in addrs:
#             for addr in addrs[netifaces.AF_INET]:
#                 ip = addr['addr']
#                 if ip.startswith('192'):
#                     return ip
#     return None

# Get the IP address
myIP = "192.168.1.26" #get_local_ip()  # You can also use `''` to bind to all interfaces

# Create and configure the server socket
server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.bind(('0.0.0.0', myPort))  # Bind to all network interfaces
server.listen(5)

print(f"Server listening on port {myPort}...")


comm_sock, clientAddr = server.accept()
print(f"Connected to : {clientAddr}")
while True:
    msg = comm_sock.recv(1024).decode("utf-8")
    print(f"Received message: {msg}")
    if msg == "exit":
        break
    
comm_sock.close()
