# class SinifAdi:
#     "Sınıfın tanımlama dokümantasyon metni"
#     #Sinifin elemanlar ve fonksiyonlar..

# """
# __doc__
# __name__
# __module__
# __bases__
# """

# print("Doc : ", SinifAdi.__doc__)
# print("Name : ", SinifAdi.__name__)
# print("Mod : ", SinifAdi.__module__)
# print("Base : ", SinifAdi.__bases__)

class Calisan:
    "Fabrikamizda çalışan personel bilgileri için sınıf"
    calisanSayisi = 0

    def __init__(self, adi, soyadi , yasi):
        self.adi = adi
        self.soyadi = soyadi
        self.yasi = yasi
        Calisan.calisanSayisi+=1
        print("Nesne Oluşturuldu...")

    def __del__(self):
        print("Yıkıcı çalıştı...")

    def bilgileriDok(self):
        print(self.adi)
        print(self.soyadi)
        print(self.yasi)
        print("calisan Sayisi : ", Calisan.calisanSayisi)


isci=Calisan("Deniz","CANTURK", 45)
isci2 = Calisan("İnci", "Boncuk", 15)

isci.bilgileriDok()
isci2.bilgileriDok()

