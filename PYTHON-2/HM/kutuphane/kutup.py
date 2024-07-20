menu = """
    1. Toplama
    2. Çıkarma
    3. Çarpma
    4. Bölme
    --------
    q. Çıkış
    >:"""
secenekler = ["1","2","3","4","q"]

# Fonksiyon tanımları
def toplama(*num):
    sonuc = 0
    for i in num:
        sonuc +=float(i)
    return sonuc

def cikarma(*num):
    if len(num) > 2:
        a,b,_ = num
    else:
        a,b = num
    return float(a)-float(b)

def carpma(*num):
    sonuc = 1
    for i in num:
        sonuc *= float(i)
    return sonuc

def bolme(*num):
    if len(num) > 2:
        a,b,_ = num
    else:
        a,b = num
    return float(a)/float(b)

def main():
    while True:
        secim = input(menu)
        
        if secim not in secenekler:
            print("Gardaş görmüyon mu listeyi... ")
            continue

        if secim.lower() == "q":
            break
        
        girdi = input("İşlem yapmak istediğin Sayıları gir :").split()

        if secim == "1":
            sonuc = toplama(*girdi)

        if secim == "2":
            sonuc = cikarma(*girdi)

        if secim == "3":
            sonuc = carpma(*girdi)

        if secim == "4":
            sonuc = bolme(*girdi)

        print("Islem Sonucu : ", sonuc)


if __name__ == "__main__":
    print("Kardeş bu dosya direk çalıştırmak için değil")