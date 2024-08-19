import socket as sc

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

# Get the server's IP address
server_ip = "127.0.0.1" #get_local_ip()  # Change this to the server's IP address if different
print(server_ip)
print(type(server_ip))
server_port = 61127

# Create a socket object
client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

try:
    # Connect to the server
    client.connect((server_ip, server_port))
    print("Connected to the server")

    # Send a message to the server
    msg = input("Enter a message: ")
    client.send(msg.encode("utf-8"))

    print("Message sent")

except Exception as e:
    print("Houston we have a problem!")
finally:
    # Close the connection
    client.close()
