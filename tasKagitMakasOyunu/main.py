
from random import randint
import kutuphane.kutuphane1 as k


while True:
    oyuncu = input("""Seçiminiz
    1. Taş
    2. Kağıt
    3. Makas
    --------
    q. Çıkış\n>: """)
    
    if oyuncu not in k.girilebilirDegerler:
        print("Lütfen belirtilen değerlerden birini seçiniz")
        continue

    if oyuncu == "q":
        print("Bizimle oynadığınız için teşekkür ederiz")
        k.puanYazdir()
        break


    rastgeleSayi = randint(0,2)
    oyuncuSecenek = k.secenekler[int(oyuncu)-1]
    bilgisayarSecenek = k.secenekler[rastgeleSayi]

    k.hesapla(oyuncuSecenek, bilgisayarSecenek)

#--------------------------------------------
