#ComputeIt
class Hayvan():
    def __init__(self, adi, yas):
        self.adi = adi
        self.yas = yas
        print("Hayvan Constructor")

    def hareketEder(self):
        raise NotImplementedError("Hayırdır sen bildar' Bu fonksiyon implement edilmeli")

    def sesCikarır(self):
        raise NotImplementedError("Ses cikarmayacaz mı?")
    
    def kakaYap(self):
        print("Uff cok kotu koktu...")
    
class Kedi(Hayvan):
    def __init__(self,adi, yas, cinsi):
        super().__init__(adi, yas)
        self.cinsi = cinsi
        print("Kedi Constructor")

    def hareketEder(self):
        print("Sürtünüyorum...")

    def sesCikarır(self):
        print("Miyawwwww")

    def showYap(self):
        print(f"""----------------
Benim Adım    : {self.adi}
Yasım         : {self.yas}
Cinsim        : {self.cinsi}""")
        self.hareketEder()
        self.sesCikarır()

    def kakaYap(self):
        super().kakaYap()
        print("Bahceye yaptı...")

#class Kopek():

boncuk = Kedi("Boncuk", 2, "Tekir")
# boncuk.showYap()
# boncuk.kakaYap()

print(isinstance(boncuk, Hayvan))

a = "Python"

if isinstance(a, str):
    print("Evet string... ")
else:
    print("Hayıırrrr.")