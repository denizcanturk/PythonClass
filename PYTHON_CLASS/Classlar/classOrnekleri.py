class Ucgen:
    """Bu bir usgen sekil sınıf taslagı
    """

    def __init__(self,taban,kenar2,kenar3,yukseklik):
        print("Contructor calıstı...")
        self.kenar2 = kenar2
        self.kenar3 = kenar3
        self.taban = taban
        self.yukseklik = yukseklik

    def alani(self):
        return (self.taban * self.yukseklik)/2

    def cevre(self):
        return self.taban + self.kenar2 + self.kenar3
    
    def __del__(self):
        print("Nesne hafizadan silindi...")

#----------------------------------------

class Daire():
    """ Daire sınıfının nesne taslagi"""

    def __init__(self,yariCap):
        self.yariCap = yariCap

    def alani(self):
        return 3*(self.yariCap**2)
    
    def cevre(self):
        return 2*3*self.yariCap

#----------------------------------------

class Dortgen:
    def __init__(self, uzun_kenar, kisa_kenar):
        self.uzun_kenar = uzun_kenar
        self.kisa_kenar = kisa_kenar

    def alan_hesapla(self):
        return self.uzun_kenar * self.kisa_kenar

    def cevre_hesapla(self):
        return 2 * (self.uzun_kenar + self.kisa_kenar)

    def bilgileriYazdir(self):
        return (
            f"Dörtgen Bilgileri:\n"
            f"Uzun Kenar: {self.uzun_kenar}\n"
            f"Kısa Kenar: {self.kisa_kenar}\n"
            f"Alan: {self.alan_hesapla()}\n"
            f"Çevre: {self.cevre_hesapla()}\n"
        )

# Örnek kullanım:
dortgen1 = Dortgen(10, 5)
print(dortgen1.bilgileriYazdir())

# Alan ve çevre hesaplamaları:
print(f"Alan: {dortgen1.alan_hesapla()}")
print(f"Çevre: {dortgen1.cevre_hesapla()}")

#----------------------------------------
class Kitap:
    def __init__(self, baslik, yazar, yayinevi, yil, sayfa_sayisi):
        self.baslik = baslik
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.yil = yil
        self.sayfa_sayisi = sayfa_sayisi

    def __str__(self):
        return f"'{self.baslik}' yazarı {self.yazar}, {self.yayinevi} tarafından {self.yil} yılında yayımlandı, {self.sayfa_sayisi} sayfa."

    def yas_hesapla(self, mevcut_yil):
        return mevcut_yil - self.yil

    def ozet(self):
        return (
            f"Kitap Bilgileri:\n"
            f"Başlık: {self.baslik}\n"
            f"Yazar: {self.yazar}\n"
            f"Yayınevi: {self.yayinevi}\n"
            f"Yıl: {self.yil}\n"
            f"Sayfa Sayısı: {self.sayfa_sayisi}\n"
            f"Yaş: {self.yas_hesapla(2024)} yıl\n"  # 2024 yılı sabit olarak kullanılmıştır, istenirse mevcut yıl dinamik olarak da alınabilir.
        )

# Örnek kullanım:
kitap1 = Kitap("1984", "George Orwell", "Secker & Warburg", 1949, 328)
print(kitap1)

# Kitap özetini yazdırmak için:
print(kitap1.ozet())
