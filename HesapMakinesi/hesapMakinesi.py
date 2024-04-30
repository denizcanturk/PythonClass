# + Toplama
# + Çıkarma
# + Çarpma
# + Bölme
# + Kök Alma
# + Kuvvetini alma
# + Bölümden kalanı bulma

# işlemlerini yerine getirecek bir hesap makinesi 
from math import pow
sonuc = 0
def toplama(num1:int, num2:int)->int:
    return num1+num2

def kokalma(num1:int, num2:int)->int:
    return pow(num1, 1/num2)

def kuvvetiniAlma(num1,num2):
    return pow(num1,num2)
    #return num1**1/num2

secim = input("1. Toplama\n" \
              "2. Çıkarma\n" \
              "3. Çarpma\n" \
              "4. Bölme\n" \
              "5. Kok Alma\n" \
              "6. Kuvvetini Alma\n" \
              "7. Bölümden Kalanı Bulma\n" \
              "8. Çıkış\n" \
              "Seçiminiz > " )

if secim == "8":
    exit()

if not secim.isdigit():
    print("Lütfen 1-8 arası sayı giriniz.")
elif int(secim) not in range(1,9):
    print("Aralık dışı sayı girdiniz!!!")


a = int(input("1.Sayıyı Giriniz : "))
b = int(input("2.Sayıyı Giriniz : "))
sonuc = 0
if secim == "1":
   sonuc = toplama(a,b)
elif secim == "2":
    None
elif secim == "3":
    None
elif secim == "4":
    None
elif secim == "5":
    None
elif secim == "6":
    None
elif secim == "7":
    None

print("İşleminizin sonucu : ".format(sonuc))