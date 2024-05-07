

dosya = open("/home/debinci/Desktop/proje/Dosyaİslemleri/metin.txt","r")

icerik = dosya.readlines()
for satir in icerik:
    print(satir)