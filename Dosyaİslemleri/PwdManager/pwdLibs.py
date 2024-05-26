import os
from cryptography.fernet import Fernet

dosyaKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/PwdManager/sifre.txt"
anahtarKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/PwdManager/key.data"

#Sadece Bir kere 
def anahtarOlustur():
    key = Fernet.generate_key()
    with open(anahtarKonumu,"wb") as dosya:
        dosya.write(key)

def anahtarOku():
    if not os.path.exists(anahtarKonumu):
        print("Dosya olusturuldu...")
        anahtarOlustur()
    with open(anahtarKonumu, "rb") as file:
        key = file.read()
        return key

key = anahtarOku()
anahtar = Fernet(key)

def tumunuGoruntule(filePath):
    if os.path.exists(filePath):
        with open(filePath, "r") as dosya:
            for line in dosya:
                kullanici, sifre = line.replace("\n","").split(":")
                sifre = anahtar.decrypt(sifre.encode()).decode()
                print(f"Kullanıcı Adı: {kullanici}\t Sifre: {sifre}")
    else:
        print("Belirtilen konumda dosya mevcut değil...")
        
def kullaniciEkle(dosyaYolu):
    if os.path.exists(dosyaYolu):
        yeniKullaniciAdi = input("Kullanıcı Adı Giriniz :")
        yenSifre = input("Sifre Giriniz :")
        yenSifre = anahtar.encrypt(yenSifre.encode()).decode()

        with open(dosyaYolu, "a") as dosya:
            dosya.write(yeniKullaniciAdi+":"+yenSifre + "\n")
    else:
        print("Dosya mevcut değil...")
        exit()

def kullaniciSil(dosyaYolu):
    if os.path.exists(dosyaYolu):
        kullaniciAdi = input("Silinecek Kullanıcı Adini Girniz : ")
        with open(dosyaYolu, "r") as dosya:
            tumIcerik = dosya.read()
            if kullaniciAdi not in tumIcerik:
                print("Yok olum böle biri")
                return 
            
            dosya.seek(0)
            icerik = dosya.readlines()

        for i, satir in enumerate(icerik) :
            if kullaniciAdi in satir:
                icerik.pop(i)
            
        with open(dosyaYolu,"w") as dosya:
            dosya.writelines(icerik)

    else:
        print("Dosya yok...")

def sifreDegistirme(dosyaYolu):
    if os.path.exists(dosyaYolu):
        kullaniciAdi = input("Kullanıcı Adını Giriniz : ")
        with open(dosyaYolu, "r") as dosya:
            tumIcerik = dosya.read()
            if kullaniciAdi not in tumIcerik:
                print("Yok olum böle biri")
                return 

            dosya.seek(0)
            icerik = dosya.readlines() 
        
        for idx, satir in enumerate(icerik):
            if kullaniciAdi in satir:
                kullaniciAdi, sifre = satir.replace("\n","").split(":")
                sifre = input("Sifre Giriniz : ")
                sifre = anahtar.encrypt(sifre.encode()).decode()
                icerik[idx] = kullaniciAdi + ":" + sifre + "\n"
                break

        with open(dosyaYolu, "w") as dosya:
            dosya.writelines(icerik)


def main():
    print("Seçenekleriniz :\n"
        "1. Kullanıcı ve Şifre Görüntüle\n"
        "2. Kullanıcı Ekle\n"
        "3. Kullanıcı Silme\n"
        "4. şifre Değiştirme\n"
        "5. Anahtar Olustur\n"
        "6.Çıkış\n")

    cevap = input("Seçiminiz :")

    if cevap==  "1":
        tumunuGoruntule(dosyaKonumu)
        #TumunuGoruntule
    elif cevap == "2":
        kullaniciEkle(dosyaKonumu)
        #Kullanıcı Ekle
    elif cevap =="3":
        kullaniciSil(dosyaKonumu)
        #Kullanıcı Silme
    elif cevap == "4":
        sifreDegistirme(dosyaKonumu)
        #Sifre Değistirme

    elif cevap == "5":
        anahtarOlustur()

    elif cevap == "6":
        exit()
    else:
        print("Adamın canını sıkma... ")



if __name__ == "__main__":
    print("Bu aslında kütüphane dosyası...")
    tumunuGoruntule(dosyaKonumu)