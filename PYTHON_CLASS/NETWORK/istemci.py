import socket as sc

serverIP = "192.168.1.81"
port = 3254

client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
try:
    client.connect((serverIP, port))
    print(f"Sunucuya {port} üzerinden bağlandık...")

    msg = input("Mesajınız : ")
    client.send(msg.encode("utf-8"))
    client.close()
except Exception as e:
    print("Hata Oluştu")