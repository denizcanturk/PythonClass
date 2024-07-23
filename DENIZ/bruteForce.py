# from random import *
# from getpass import getpass
# import os

# targetPasswd = getpass("Sifrenizi Giriniz : ")

# charSource = "abcçdefghıijklmnoöprsştuüvxyzqw1234567890!'^+%&/()=?_-*$#{[]}`|~"

# producedPasswd = ""

# while producedPasswd!=targetPasswd: 
#     producedPasswd=""
#     for i in range(6):  #Not to cross the lines and to save some time...
#         guessedPasswd = charSource[randint(0, len(charSource)-1)]
#         producedPasswd = str(guessedPasswd)+str(producedPasswd)
#         print(producedPasswd)

# print("Passwd : ", producedPasswd)

giris=input("matematik işlemini giriniz (örn: 15+23):")

for i, islem in enumerate(giris,1):
    if islem=="+" or islem=="-" or islem=="*" or islem=="/":
        ilkSayi=float(giris[0:i-1])
        ikinciSayi=float(giris[i:len(giris)+1])
        if islem=="+":
            print(ilkSayi+ikinciSayi)
        elif islem=="-":
            print(ilkSayi-ikinciSayi)
        elif islem=="/":
            print(ilkSayi/ikinciSayi)
        elif islem=="*":
            print(ilkSayi*ikinciSayi)