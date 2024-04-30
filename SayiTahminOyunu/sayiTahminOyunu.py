"""# Bilgisayar 1-100 arasında bir sayı üretir
# Kullanıcıya giriş yapması gereken aralık belirtilir
# Kullanıcı sayıyı buluncaya kadar yönlendirilir
# - Örn.: Kullanıcı ilk iki tahmininde 15 ve 85 girdi ise:
# - Sayı girmesi gereken aralık "15-85 arasında bir sayı giriniz:" şeklinde olmalıdır
# Kullanıcının yaptığı tahminler bir listede tutulur
# Kullanıcının yaptığı tahmin sayısı ve yaptığı tahminler
# oyun sonunda ekrana yazdırılır
# Oyuncu oyundan çıkmak için q harfi ile giriş yapmalıdır"""

from random import randint

bilgisayarSecimi = randint(1,100)
MIN = 1
MAX = 100
tahminListesi = []
while True:
    kullaniciSecimi = input("{}-{} arasında Sayi arassında giriniz : ".format(MIN,MAX))
    
    if kullaniciSecimi == "q":
        break
    elif not kullaniciSecimi.isdigit():
        print("Paşam sana zahmet bir sayı giriver...")
        continue

    kullaniciSecimi = int(kullaniciSecimi)

    tahminListesi.append(kullaniciSecimi)
    
    if kullaniciSecimi > bilgisayarSecimi:
        print("Daha küçük olmalı")
        MAX = kullaniciSecimi

    elif bilgisayarSecimi > kullaniciSecimi:
        print("Daha büyük olmalı")
        MIN = kullaniciSecimi

    elif bilgisayarSecimi == kullaniciSecimi:
        print("Kutlaaarrııııızzzz....")
        break

for idx,i in enumerate(tahminListesi):
    print(idx+1 ,". Tahmin : ", i)

print("Tahmin Sayısı : {}".format(len(tahminListesi)))
