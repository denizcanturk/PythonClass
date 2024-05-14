#Absolute Path
dosyaKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/metin.txt"
#Relative Path
relativeDosyaKonumu = "Dosyaİslemleri/metin.txt"

dosya = open(dosyaKonumu, "r+", encoding="utf-8")

icerik = dosya.readlines()

icerik.insert(1,"Benim Adım Batman")

print(icerik)
dosya.writelines()