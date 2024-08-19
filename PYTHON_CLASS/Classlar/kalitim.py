#from abc import ABC, abstractmethod







class Sekiller():
    def __init__(self):
        pass

    def alan(self):
        raise NotImplementedError("Bu fonksiyon yazılmalı... ")
    
    def cevresi(self):
        raise NotImplementedError("Bu fonksiyon yazılmalı... ")

class Daire(Sekiller):
    def __init__(self, yariCap):
        self.yariCap = yariCap

    def alan(self):
        alan = 3*(self.yariCap**2)
        return alan

daire1 = Daire(5)
print(daire1.alan())
print(daire1.cevresi())



# class Hayvan():
#     def __init__(self, adi, yasi, rengi,cinsi):
#         self.adi = adi
#         self.yasi = yasi
#         self.rengi = rengi
#         self.cinsi = cinsi

#     def sesCikart(self):
#         raise NotImplementedError("Failed")
    
#     def yemekYer(self):
#         raise NotImplementedError("Failed")
    
#     def ozellikleriniYazdir(self):
#         return (f"Adi : {self.adi}, yasi : {self.yasi}, rengi : {self.rengi}, cinsi : {self.cinsi}")
    
# class Kopek(Hayvan):
#     def __init__(self, adi, yasi, rengi, cinsi):
#         super().__init__(adi, yasi, rengi,cinsi)

#     def sesCikart(self):
#         print("havliyorum")

#     def yemekYer(self):
#         print("Kopek maması yerim")

#     def ozellikleriniYazdir(self):
#         return super().ozellikleriniYazdir()
    
# kopek1 = Kopek("Deniz", 2,"Terier","Bi şey")
# print(kopek1.ozellikleriniYazdir())