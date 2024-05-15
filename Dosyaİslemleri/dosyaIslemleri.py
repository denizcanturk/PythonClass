#Absolute Path
dosyaKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/metin.txt"
#Relative Path
relativeDosyaKonumu = "Dosyaİslemleri/metin.txt"

# dosya = open(dosyaKonumu, "w+", encoding="utf-8")

# icerik = dosya.readlines()

# icerik.insert(1,"Benim Adım Batman")

# print(icerik)
# dosya.seek(0)
# dosya.writelines(icerik)


with open(dosyaKonumu,"w+", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)