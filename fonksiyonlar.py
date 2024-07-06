#Parametre almayan fonksiyon
# def merhabaDe():
#     print("Merhaba, hoşgeldiniz!")

# #Cağrılması
# for i in range(5):
# merhabaDe()

# def deliceKarsila():
#     for i in range(10):
#         print("Çok ama çok hoşgeldin")

# deliceKarsila()


# def beniYazdir(isim):
#     print(f"{isim} ifadesinde", len(isim) , "adet harf bulunmaktadır.")

# beniYazdir("Deniz")

# def tanimla(isim, soyisim):
#     if isim == "Cabbar" and soyisim == "Abdul":
#         print("Giris Dogrulandı")
#     else:
#         print("Cek arabanı...")

# a,b  = input("Adini Soyadini Gir : ").split(" ")
# print(a,b)

# tanimla(a,b)

# def topla(a,b):
#     c = a+b
#     return c

# x = 5
# y = 45

# # v = topla(x,y)
# print(topla())
# # print(v)

# def carp(a, b = 5):
#     c = a*b
#     print(c)

# carp(6)


# def carp(a,b):
#     return a*b

# def carpim(*a):
#     sonuc =1 
#     for i in a:
#         sonuc *=i
#     return sonuc

# print("5:", carpim(5))
# print("5,8,9, 1.2:", carpim(5,8,9))
# print("2,5,9,56,5,80,7.3: ", carpim(2,5,9,56,5,80,7.3))

# a = carpim(1,5,6,9,8,2,1,5)







# Kullanıcının adini parametre olarak alan ve 
# "Merhaba <Kullanıcı Adi >" şeklinde mesajı ekrana yazdıran
# fonksiyonu yazınız. 

# def kullanici(a):
#     print(f"Merhaba {a}")
#     print("Merhaba", a)

# adim = "Deniz"
# kullanici(adim)

# kullanici("Rahşan")
# isim = "Emrecan"
# def karsila():
    
#     print("Merhaba", isim)

# karsila()
# print(isim)


# Kullanıcıdan alınacak olan belirsiz sayıdaki isim listesini
# Ekrana yazdıran ve kişi sayısını döndüren fonk. yazınız. 

# def listele(*a):
#     for i in a:
#         print(i)
#     return len(a)


# sayi = listele("Mazlum", "Ogun", "Bugün", "Rahşan", "Erkan", "Gökay", "Emrecan")
# print(f"Listede {sayi} adet kişi mevcut!")


# Parametre olarak string değerin 

# def kullanici(*sonuc):
#     for i in sonuc:
#         print(i)
#     return len(sonuc)

# sayi = kullanici("Mazlum", "Ogun", "Bugün", "Rahşan")
# print(f"Listede {sayi} adet kişi vardır.")

x = 5

def yazdir():
    global x
    x = 10
    print(x)


yazdir()
print(x)