
ModuleNotFoundError

import gmap
print("Bakalım burası çalışacak mı?")

# ------------------------------------------
try :
    import gmap
except Exception as e:
    pass




try :
    import gmap
except Exception as e:
    print(str(e))
except ModuleNotFoundError as e:
    print("Module Bulunamadı :", str(e))
except Exception as e:
   print("Error: ", str(e))
   raise IndexError
else:
    print("Herhangi bir sorun yaşamazsam çalışırım...")
finally:
    print("Her şartta çalışırım ben... ")


# ------------------------------------------
IndexError

mList = [10,20,30]
print(mList[3])


try:
    print(mList[3])
    print(f)
except Exception as e:
    print(str(e))
except IndexError as e:
    print("Hata : ", str(e))
except NameError as e:
    print("Bu Sefer da : ", str(e))
else:
    print("Liste elemanını bulduk...")
finally:
    print("Burda işimiz bitti...")

# ------------------------------------------
ZeroDivisionError

a = 25
b = 0
print(a/b)



try:
    print(a/b)
except Exception as e:
    print(str(e))
except ZeroDivisionError as e:
    print("Sıfıra bölmek de neyin nesi gardaş :", str(e))

# ------------------------------------------
TypeError

x = "abc"
y = 2

print(x+y)



try:
    print(x+y)
except Exception as e:
    print(str(e))
except TypeError as e:
    print("Tip uyumsuzluğu :", str(e))
else:
    print("Çok başarılı bir toplama işlemi... ")    
finally:
    print("Burda işimiz bitti...")

# ------------------------------------------
ValueError

import math
z = -10
print(math.sqrt(z))


try:
    print(math.sqrt(z))
except Exception as e:
    print(str(e))
except ValueError as e:
    print("Değer Uyuşmazlığı :", str(e))
else:
    print("Çok başarılı bir Kök alma işlemi... ")    
finally:
    print("Burda işimiz bitti...")
# ------------------------------------------


##########################################
#                 ORNEK
##########################################

while True:
    secim = input("Bir tam sayı giriniz : ")
    if secim.isdigit():
        sonuc = int(secim)**2
        print("İslem Sonucu : ", sonuc)
        break
    print("Paşam girdiğin değer olmadı, tekrar dene...")

while True:
    try:
        secim = int(input("Bir sayı giriniz : "))
    except Exception as e:
        print(str(e))
    except ValueError as e:
        print("Hata : Bir sayı girmediğiniz için patladım...", str(e))
    else:
        print("Sayının karesi :", secim**2)
        break


##########################################
#                 ORNEK
##########################################

dosyaAdi = "dosyam.txt"
try:
    file = open(dosyaAdi, 'r')
    print(file.read())
    print("Dosya " + dosyaAdi + " Başarılı şekilde okundu...")
except IOError:
    print("Hata : hele bi bak bakam, var mı :  " + dosyaAdi)


##########################################
#                 ORNEK
##########################################

sayi = 6
if sayi > 5:
    raise Exception(f"Sayi 5 den büyük olamaz. ({sayi=})")
print(sayi)
