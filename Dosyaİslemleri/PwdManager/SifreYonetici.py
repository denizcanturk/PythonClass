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

dosyaKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/PwdManager/sifre.txt"



def tumunuGoruntule(dosyaYolu):
    if os.path.exists(dosyaYolu):

        with open(dosyaYolu, "r") as dosya:
            icerik = dosya.readlines()
        
            for satir in icerik:
                kullaniciAdi, sifre = satir.split(":")
                print("Kullanıcı Adi : {}, Sifre : {}".format(kullaniciAdi, sifre.replace("\n","")))
    else:
        print("Dosya mevcut değil...")
        
def kullaniciEkle(dosyaYolu):
    if os.path.exists(dosyaYolu):
        yeniKullaniciAdi = input("Kullanıcı Adı Giriniz :")
        yenSifre = input("Sifre Giriniz :")

        with open(dosyaYolu, "a") as dosya:
            dosya.write(yeniKullaniciAdi+":"+yenSifre)
    else:
        print("Dosya mevcut değil...")
        exit()

def kullaniciSil(dosyaYolu):
    if os.path.exists(dosyaYolu):
        kullaniciAdi = input("Silinecek Kullanıcı Adini Girniz : ")
        with open(dosyaYolu, "r") as dosya:
            icerik = dosya.readlines()
        
        for i, satir in enumerate(icerik) :
            if kullaniciAdi in satir:
                icerik.pop(i)
            else:
                print("Bulamadım...")
            


        with open(dosyaYolu,"w") as dosya:
            dosya.writelines(icerik)

    else:
        print("Dosya yok...")



print("Seçenekleriniz :\n"
      "1. Kullanıcı ve Şifre Görüntüle\n"
      "2. Kullanıcı Ekle\n"
      "3. Kullanıcı Silme\n"
      "4. şifre Değiştirme\n"
      "5.Çıkış\n")

cevap = input("Bir seçenek seçiniz :")

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
    None
    #Sifre Değistirme
elif cevap == "5":
    exit()
else:
    print("Adamın canını sıkma... ")