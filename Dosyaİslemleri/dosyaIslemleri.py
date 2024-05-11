#Absolute Path
dosyaKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/metin.txt"
#Relative Path
relativeDosyaKonumu = "Dosyaİslemleri/metin.txt"

dosya = open(dosyaKonumu, "r")

satirlar = dosya.readlines()

print(satirlar)

for satir in satirlar:
    print(satir)