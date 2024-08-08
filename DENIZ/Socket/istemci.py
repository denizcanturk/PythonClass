import socket as sc

def get_local_ip_Win():
    hostname = sc.gethostname()
    ip_addresses = sc.gethostbyname_ex(hostname)[2]
    for ip in ip_addresses:
        if ip.startswith('192'):
            return ip
    return None

def get_local_ip():
    import netifaces
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                ip = addr['addr']
                if ip.startswith('192'):
                    return ip
    return None

# Get the server's IP address
server_ip = input("Enter the server's IP address: ")
# server_ip = get_local_ip_Win()  # Use this if the server is on the same machine (Windows)
# server_ip = get_local_ip()  # Use this if the server is on the same machine (Linux)

server_port = 6127

# Create a socket object
client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

# Connect to the server
client.connect((server_ip, server_port))

print("Connected to the server")

# Send a message to the server
msg = input("Enter a message: ")
client.send(msg.encode("utf-8"))

print("Message sent")

# Close the connection
client.close()