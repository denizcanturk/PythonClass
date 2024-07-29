import os
path = "/home/debinci/Desktop/proje/PYTHON-2/SifreYonetici/sifre.txt"
menu="""İslem Seciniz:
        1. Kullanıcı ve Sifre Goruntule
        2. Kullanıcı Ekle
        3. Kullanıcı Sil
        4. Sifre Değiştir
        5. Çıkış
        >:"""


def sifreDegistir():
    if not os.path.exists(path):
        print("aradığınız dosya bulunamadı")
        return
    else:
        dosya=open(path, encoding="utf-8")
        icerik=dosya.readlines()
        dosya.close()

        kullaniciAdi=input("kullanıcı adınızı girin")
        for idx,i in enumerate(icerik):
            if kullaniciAdi in i:
                yeniSifre=input("yeni şifrenizi girin")
                yeniSatir=kullaniciAdi+"|"+yeniSifre+"\n"
                icerik[idx]=yeniSatir

        dosya=open(path, "w", encoding="utf-8")
        dosya.writelines(icerik)
        dosya.close()
sifreDegistir()

def kullaniciVeSifreGoruntule(path):
    if not os.path.exists(path):
        print("Aradığınız dosyaya şu an ulaşılamıyor...")
        return
    else:
        dosya = open(path)
        icerik = dosya.read()
        print(icerik)


secim = input(menu)
if secim == "1":
    kullaniciVeSifreGoruntule(path)

elif secim == "2":
    None #Kullanıcı Ekleme Fonksiyonu

elif secim=="3":
    None #Kullanıcı Silme

elif secim == "4":
    None #Sifre Değiştir

elif secim == "5":
    None #
    exit()

else:
    print("Elinin örekesi, bak bakıyım listede var mı?")
