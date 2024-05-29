# Kullanıcı adı ve şifresi bir text dosyasında tutulur
#
# Kullanıcı adı ve şifresi girilirken tek satırda, 
#        boşluk bırakılmadan ":" karakteri ile ayrılarak girilmelidir
#
# Program, şifre dosyasını görüntüleme, kullanıcı ekleme, 
#        mevcut kullanıcıya ait şifreyi değiştirebilme ve 
#       kullanıcı silme özelliğine sahip olmalıdır
#
# Yeni kullanıcılar yeni bir satır olarak eklenir

import os
from cryptography.fernet import Fernet

class PasswordManager():
    def __init__(self,pwdPath:str,keyPath:str):
        self.pwdFilePath = pwdPath
        self.keyFilePath = keyPath
        self.key = self.anahtarOku()
        self.cryptor = Fernet(self.key)
        self.userName = ""
        self.passWord = ""
        self.PwdManagerMain()

    def __del__(self):
        print("Password Manager bellekten silindi...")

    def anahtarOlustur(self):
        key = Fernet.generate_key()
        with open(self.keyFilePath,"wb") as dosya:
            dosya.write(key)

    def anahtarOku(self):
        if not os.path.exists(self.keyFilePath):
            print("Dosya olusturuldu...")
            self.anahtarOlustur()
        with open(self.keyFilePath, "rb") as file:
            key = file.read()
        return key   
    
    def tumunuGoruntule(self):
        if os.path.exists(self.pwdFilePath):
            with open(self.pwdFilePath, "r") as dosya:
                for line in dosya:
                    kullanici, sifre = line.replace("\n","").split(":")
                    sifre = self.cryptor.decrypt(sifre.encode()).decode()
                    print(f"Kullanıcı Adı: {kullanici}\t Sifre: {sifre}")
        else:
            print("Belirtilen konumda dosya mevcut değil...")

    def kullaniciEkle(self):
        if os.path.exists(self.pwdFilePath):
            yeniKullaniciAdi = input("Kullanıcı Adı Giriniz :")
            yenSifre = input("Sifre Giriniz :")
            yenSifre = self.cryptor.encrypt(yenSifre.encode()).decode()

            with open(self.pwdFilePath, "a") as dosya:
                dosya.write(yeniKullaniciAdi+":"+yenSifre + "\n")
        else:
            print("Dosya mevcut değil...")

    def kullaniciSil(self):
        if os.path.exists(self.pwdFilePath):
            kullaniciAdi = input("Silinecek Kullanıcı Adini Girniz : ")
            with open(self.pwdFilePath, "r") as dosya:
                tumIcerik = dosya.read()
                if kullaniciAdi not in tumIcerik:
                    print("Yok olum böle biri")
                    return 
                
                dosya.seek(0)
                icerik = dosya.readlines()

            for i, satir in enumerate(icerik) :
                if kullaniciAdi in satir:
                    icerik.pop(i)
                
            with open(self.pwdFilePath,"w") as dosya:
                dosya.writelines(icerik)

        else:
            print("Dosya yok...")

    def sifreDegistirme(self):
        if os.path.exists(self.pwdFilePath):
            kullaniciAdi = input("Kullanıcı Adını Giriniz : ")
            with open(self.pwdFilePath, "r") as dosya:
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
                    sifre = self.cryptor.encrypt(sifre.encode()).decode()
                    icerik[idx] = kullaniciAdi + ":" + sifre + "\n"
                    break

            with open(self.pwdFilePath, "w") as dosya:
                dosya.writelines(icerik)

    def PwdManagerMain(self):
        while True:
            print("Seçenekleriniz :\n"
                "1. Kullanıcı ve Şifre Görüntüle\n"
                "2. Kullanıcı Ekle\n"
                "3. Kullanıcı Silme\n"
                "4. şifre Değiştirme\n"
                "5. Çıkış\n")

            cevap = input("Seçiminiz :")

            if cevap==  "1":
                self.tumunuGoruntule()
                #TumunuGoruntule
            elif cevap == "2":
                self.kullaniciEkle()
                #Kullanıcı Ekle
            elif cevap =="3":
                self.kullaniciSil()
                #Kullanıcı Silme
            elif cevap == "4":
                self.sifreDegistirme()
                #Sifre Değistirme
            elif cevap == "5":
                exit()
            else:
                print("Adamın canını sıkma... ")

if __name__ == "__main__":
    print("This file is not intended for direct call!!!")
