set0 = {"Begonya", "Sümbül"}
set1 = {"Begonya","Kardelen","Lavanta","Sümbül","Begonya","Kardelen","Lavanta", "Sümbül",1,4}
set2 = {1,4,7,6,3,4,3,2,1,3,4,"Lavanta", False, "Adıyaman","Üzüm"}
set3 = {True,False,True, False,False}
list1 = ["Elma","Armut", "Üzüm",4,122,"g",1,4,2,6,"Üzüm","Armut"]
tuple1 = ("İzmit", "Mersin","Adıyaman","Diyarbakır")

# print("Set0 :", set0)
# print("Set1 : ", set1)

# for i in set1:
#     print(i)

# if "Lavanta" in set2:
#     print("Evet buldum..")
# else:
#     print("Yogh")

# set0.add(True)
# print(set0)
# set0.add(True)
# print(set0)


#Birleşim kümesi
# set2.update(set1)

# print(set1)
# print(set2)

# yeniSet = set1 | set2
# print(yeniSet)

# set0.update(list1)
# print(set0)

# set1.discard("Begonya")
# set1.remove("Begonya")
# set1.clear()

# del set1

# print(set1)


#İki Kümenin kesişimi

#yeniSet = set0.intersection(set1)
# yeniSet = set0 & set1

# print(yeniSet)


# farkSeti = set1.difference(set2)
# farkSet2 = set1 - set2
# print(farkSeti)


# simetrikFark = set1.symmetric_difference(set2)
# simetrikFark2 =  set1 ^ set2


# print(simetrikFark)
# print(simetrikFark2)


print(set0.issubset(set1)) #-> True ya da False

print(set1.issuperset(set0)) #-> True ya da False