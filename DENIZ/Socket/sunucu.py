import socket as sc
import netifaces

myIP = sc.gethostbyname(sc.gethostname())
myPort = 6127
print(myIP)

#Windows
def get_local_ip_Win():
    hostname = sc.gethostname()
    print(sc.gethostbyname_ex(hostname))
    ip_addresses = sc.gethostbyname_ex(hostname)[2]
    for ip in ip_addresses:
        print(ip)
        if ip.startswith('192'):
            return ip
    return None
#Linux
def get_local_ip():
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                ip = addr['addr']
                if ip.startswith('192'):
                    return ip
    return None

#This only for accepting comms
server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.bind((myIP, myPort))

server.listen(5)

while True:
    # comm_sock is for communication with the client... 
    comm_sock, clientAddr =server.accept()
    print(f"Connected to :  {clientAddr}")
    msg = comm_sock.recv(1024).decode("utf-8")
    print(f"Rec Mdg : {msg}")
