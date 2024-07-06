#ModuleNotfoundError

# import gmap
# print("Bakalım bu satır çalışacak mı?")

# try:
#     import gmap
# except Exception as e :
#     print(e)

# print("Bakalım bu satır çalışacak mı?")

# try:
#     import gmap
# except ModuleNotFoundError as e:
#     print("Gmap kütüphanesi yüklenmeli")
# else:
#     print("Kütüphance zaten yüklü")
# finally:
#     print("Yukarıdakiler beni ilgilendirmez, her türlü çalıştım...")

#IndexError

# a = [1,3,5,7]
# # print(a[6])

# try:
#     print(a[6])
# except TypeError as e:
#     print(e)
# except IndexError as e:
#     print("Bakalım çalışacak mı")
# except ZeroDivisionError as e:
#     print("sdlfjksdfk")


# a = 20
# b = 0
# try:
#     c = a / b
# except ZeroDivisionError as e:
#     print("Bölen 0 olamaz!")

# try:
#     print(c)
# except NameError as e:
#     print("Bölme işlemi gerçekleşmedi")

#Type Error

# a = "Python"
# b = 5.1
# try:
#     print(a*b)
# except Exception as e:
#     print(e)

sayi = 5

if sayi < 6:
    raise Exception("Bu değer tanımle limitin altında olamaz")

print("Bakalım bu çalışacak mı?")
