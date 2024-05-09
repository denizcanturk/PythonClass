#Absolute Path
dosyaKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/metin.txt"
#Relative Path
dk = "Dosyaİslemleri/metin.txt"
dosya = open(dosyaKonumu, "r", encoding="utf-8")

# print(dosya.tell())
# icerik = dosya.read(10)

# print(dosya.tell())
# icerik2=dosya.read(3)

# print(dosya.tell())
# print(icerik)
# print(icerik2)


# satir1 = dosya.readline().replace("\n", "")
# print(dosya.tell())
# satir2 = dosya.readline()
# print(dosya.tell())

# print(satir1)
# print(satir2, end="")

satirlar = dosya.readlines()

print(len(satirlar))

# for satir in satirlar:
#     print(satirlar)
