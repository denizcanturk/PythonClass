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
myIP = "127.0.0.1" #get_local_ip()  # You can also use `''` to bind to all interfaces

# Create and configure the server socket
server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.bind(('', myPort))  # Bind to all network interfaces
server.listen(5)

print(f"Server listening on port {myPort}...")

while True:
    comm_sock, clientAddr = server.accept()
    print(f"Connected to : {clientAddr}")
    msg = comm_sock.recv(1024).decode("utf-8")
    print(f"Received message: {msg}")
    comm_sock.close()
