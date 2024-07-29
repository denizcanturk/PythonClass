from random import *  # noqa: F403
from getpass import getpass

targetPasswd = getpass("Sifrenizi Giriniz : ")

charSource = "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGHIİJKLMNOÖPQRSŞTUÜVWXYZ01234567890!'^+%&/()=?_-*$#{[]}`|~"

producedPasswd = ""
pwds = set()
pBar = "\\|/-"
counter = 0
while producedPasswd!=targetPasswd: 
    producedPasswd=""
    for i in range(len(targetPasswd)):  #Not to cross the lines and to save some time...
        guessedPasswd = charSource[randint(0, len(charSource)-1)]  # noqa: F405
        producedPasswd += guessedPasswd
        pwds.add(producedPasswd)
        print(pBar[counter], end="\r")
        counter+=1
        if counter ==4:
            counter = 0

print("Passwd : ", pwds)
print("Passwd : ", producedPasswd)

# for i in range(len(charSource)):
#     for j in range(3):