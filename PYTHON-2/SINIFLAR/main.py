class Arabam():
    """
        Arabamı oluşturacağım Class yapısı
    """
    def __init__(self, renk:str, yil:int, model:str):
        self.renk = renk
        self.yil = yil
        self.model = model
        print("Constructor çalıştı...")
        self.arabamiGoruntule()

    def __del__(self):
        print("Deconstructor çalıştı...")

    def arabamiGoruntule(self):
        print("Rengi : ", self.renk)
        print("Yili  : ", self.yil)
        print("Modeli:", self.model)
# ilkArabam = Arabam("Beyaz", 1960, "Mustang")
# #ilkArabam.arabamiGoruntule()
# ikinciArabam = Arabam("Siyah", 2023,"Dodge")
# del ilkArabam
# print("Bu satırdan sonra ikinci Silinecek...")

class Oyuncu():
    def __init__(self, adi:str, puan:float,hayat:float, gucu : float):
        self.adi = adi
        self.puan = puan
        self.hayat = hayat
        self.gucu = gucu

    def __del__(self):
        print("Oyuncu Öldü...")

    def goruntule(self):
        print(self.adi,self.puan, self.hayat, self.gucu)

    def vuruldu(self):
        self.hayat -=10
    
    def vurdu(self):
        self.puan +=10
        self.gucu +=10

# oyuncuA = Oyuncu("Oyuncu 1", 100, 100, 50)
# oyuncuA.goruntule()
# oyuncuA.vuruldu()
# oyuncuA.goruntule()
# oyuncuA.vurdu()
# oyuncuA.goruntule()

class Ucgen():
    def __init__(self, kenara, kenarb, taban, acia, acib,acic,yukseklik):
        self.kenara = kenara
        self.kenarb = kenarb
        self.taban = taban
        self.acia = acia
        self.acib = acib
        self.acic = acic
        self.yukseklik = yukseklik
        self.alan = self.alanHesapla()
        self.cevre = self.cevreHesapla()

    def alanHesapla(self):
        return (self.taban * self.yukseklik) / 2
    
    def cevreHesapla(self):
        return self.kenara+self.kenarb+self.taban
    
# bermuda = Ucgen(3,4,5,45,45,90,6)
# # bermudaAlani = bermuda.alanHesapla()
# # bermudaCevresi = bermuda.cevreHesapla()
# print("Cwevresi : ", bermuda.cevre, "Alanı : ", bermuda.alan)



class BankaHesabi():
    def __init__(self, adi, IBAN,tc,bakiye):
        self.adi = adi
        self.IBAN = IBAN
        self.tc= tc
        self.bakiye = bakiye

    def MusteriGoruntule(self):
        print(f"""------------------
Müsteri Adı    : {self.adi}
Müsteri IBAN   : {self.IBAN}
Müşteri TC     : {self.tc}
Müşteri Bakiye : {self.bakiye}""")

    def paraYatir(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} başarı ile yatırıldı...")

    def paraCek(self, miktar):
        if miktar > self.bakiye:
            print("Hesabınızda yeterince para yok...")
            return
        else:
            self.bakiye-=miktar
            print(f"{miktar} başarı ile hesabınızdan çekildi...")

# musteriA = BankaHesabi("Deniz", 234, 959, 1000)
# musteriA.MusteriGoruntule()
# musteriA.paraCek(500)
# musteriA.paraYatir(1200)
# musteriA.MusteriGoruntule()


# Kopek Sınıfı oluşturun:
#  Adi,
#  yaşı,
#  Cinsi,
#  Rengi,
#  Kilosu,
#  Enerjisi
# //--------------------------
#  YemekYer():
#     Kilosu artar
#  TuvaleteGider()
#     Kilosu azalır
#  Uyur()
#     Enerjisi artar
#     Kilosu artar
#  Kosar()
#     Enejisi azalır
#     Kilosu azalır
#  Havlar()
#     Enerjisi azalır
    
class Dog():
    dogCount = 0
    def __init__(self, ad, yas, cins, renk, kilo, enerji):
        self.adi = ad
        self.yas = yas
        self.cins = cins
        self.renk = renk
        self.kilo = kilo
        self.enerji = enerji

    def healtcheck(self):
        print(f"""----------------
Adı    : {self.adi}
Yası   : {self.yas}
Cinsi  : {self.cins}
Kilosu : {self.kilo}
Enerji : {self.enerji}""")
        
    def eat(self):
        None

    def shit(self):
        None

    def sleep(self):
        None

    def run(self,deger):
        self.enerji -= deger
        self.kilo -= deger/5

    def makeVoice():
        None
 
barnie = Dog("Barn", 12,"Shephard", "Brown",23.3,100)
barnie.healtcheck()

 