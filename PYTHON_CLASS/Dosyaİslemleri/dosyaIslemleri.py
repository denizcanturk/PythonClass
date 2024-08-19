#Absolute Path
dosyaKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/metin.txt"
#Relative Path
relativeDosyaKonumu = "Dosyaİslemleri/metin.txt"


import os

if os.path.exists(dosyaKonumu):
    print("Doyayı buldum, işlem yapıyorum... ")
    with open(dosyaKonumu, "r+") as dosya:
        icerik = dosya.read()
        print(icerik)
else:
    print("Dosya yok gözün kör olmasın... ")

