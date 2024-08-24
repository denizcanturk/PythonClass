import socket as sc

ip = "192.168.1.81"
port = 3254

server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.bind((ip, port))

server.listen(10)
print("Gelen bağlantı bekleniyor...")
commSock, clientAddr = server.accept()
print(f"{clientAddr} : size bağlandı...")

msg = commSock.recv(1024).decode("utf-8")
print(f"{clientAddr} : {msg}")

commSock.close()

