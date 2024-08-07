# a = 5

# print(a==5)

# print(a > 4)

# print(a >= 5)

# print (a <= 5)

# a=1
# a="Python"
# a=0.5
# print(type(a))



# cevap = input("Bir patern giriniz : ")
# #print(type(cevap))
# print(cevap*5)

# cevap = int(input("Bir tam sayi giriniz : "))
# print(type(cevap))
# bolme = cevap/2
# toplama = cevap + 2
# carpma = cevap * 5

# print(type(bolme), bolme)
# print(type(toplama), toplama)
# print(type(carpma), carpma)


# c1 = input("Deger1 Gir : ")
# c2 = input("Deger2 Gir :")

# print(c1+c2)

# print()


# print("Burayı burdan \ napıcan")
# print("5 \\ 2 = ....")
# print("Deniz bir \"uyuz\"")


# txt = """
# Deniz CANTÜRK
# 45 YAŞINDA
#             MARAŞLI
#     mERİNSDE
#              YAŞIYOR"""

# txt2 = "Deniz CANTURK"+ \
# "45 YAŞIDNA"+ \
# "           MARAŞLI"
# print(txt2)

# a = 25

# if a < 20 and a > 0:
#     print("Sayi aralık içinde")
# else:
#     print("Aralık içinde değil")

# a = int(input("1.Sayi : "))
# b = int(input("2.Sayi : "))

# if a > b :
#     print(a)
# else:
#     print(b)


#---------- SADECE IF

# sayi = int(input("Sayi girinizi : "))

# if sayi == 0:
#     print("Sıfır")
# if sayi > 0:
#     print("buyuk")
# if sayi < 0:
#     print("kucuk")


# if sayi == 0:
#     print("s")
# elif sayi > 0:
#     print("buyuk")
# else :
#     print("kucuk")

# a = 0
# toplam = 0
# while a < 5:
#     a = a+1
#     toplam = toplam + a
    
# print(toplam)

# a = 0
# toplam = 0

# while a < 100:
#     a = a+1
#     if a%2 == 0:
#         toplam = toplam + a
# print(toplam)

# deg0 = "Ogreniorum"
# deg1 = "Python"
# deg2 = 23

# print(deg1 + str(deg2))

# print(deg1, deg2)
# #                                                    0     1
# print("{} ogreniyorum. {} satır kod yazdım".format(deg1, deg2))
# print("{1} ogreniyorum. {0} satır kod yazdım".format(deg1, deg2))

# print(deg1, "ogreniyorum.", deg2, "satir kod yazdım..")

# print(f"{deg1} ogreniorum. {deg2} satir kod yazdım.")
# print(deg1+" "+deg0)

# sonuc = 5 // 2
# print(sonuc)


# deg0 = "Ogreniorum"
# deg1 = "Python"
# deg2 = 23
# deg3 = 1.5

# print(deg0 + str(deg3))
# print(int(deg2+deg3))


# mtn = "python"

# for hrf in mtn :
#     print(hrf)

# i = 1
# while True:
#     print(i)
#     i+=1

#     if i > 100:
#         print("Deniz")
#         break

# print("iŞLEM TAMAMLANDI!")


# shape = "*"
# a = 10
# b=0
# while b <= a :
#     b +=1
#     print(shape*b)

#     *
#    ***
#   *****
#  *******
# *********

# 0 1 1 2 3 5 8 13 21 34 ....(50)

# mtn="python"
# for i in mtn:
#     print(i,end="")

# print("THE END!")

# sayi1 = 0
# sayi2 = 1
# araTop = 0
# for i in range(1):
#     print(sayi1)
#     araTop = sayi1 + sayi2
#     sayi1 =sayi2
#     sayi2 = araTop


# for i in range(5):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(i, 5):
#         print("* ", end="")
#     print()
739

# for i in range(5):
#     for j in range(5, i, -1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("* ", end="")
#     print()


# sampleText = """bu Benim Dünyam"""

# newText = sampleText.capitalize()
# print(newText)

# caseFolded = sampleText.casefold()
# print(caseFolded)
# print(sampleText)

# sampleText.count()
metin = """Avrupa Parlamentosu, dünyada yapay zeka kullanımına ilişkin kurallar getiren ilk yasal düzenleme olan, Avrupa Yapay Zeka Yasasını onayladı. Yeni yasa ile yüz tanıma amaçlı veri tabanı oluşturan sistemler de dahil olmak üzere insan haklarını tehdit eden yapay zeka uygulamaları yasaklanıyor. Avrupa Birliği (AB) Komisyonu, Avrupa Parlamentosu ve üye ülkelerin daha önce üzerinde uzlaşmaya vardığı düzenleme, Çarşamba günü parlamento genel kurulunda ele alındı. Avrupa Yapay Zeka Yasası, 46’ya karşı 523 üyenin oyuyla kabul edildi. Yeni yasa ile yüz tanıma amaçlı veri tabanı oluşturan sistemler de dahil olmak üzere insan haklarını tehdit eden yapay zeka uygulamaları yasaklanıyor. Avrupa Birliği (AB) Komisyonu, Avrupa Parlamentosu ve üye ülkelerin daha önce üzerinde uzlaşmaya vardığı düzenleme, Çarşamba günü parlamento genel kurulunda ele alındı. Avrupa Yapay Zeka Yasası, 46’ya karşı 523 üyenin oyuyla kabul edildi. Dünyada genel amaçlı yapay zeka kullanımına ilişkin önlemler içeren ilk düzenleme olan yasa, özellikle güvenlik güçleri tarafından biyometrik tanımlama sistemlerinin kullanımı konusunda sınırlamalar getiriyor. Düzenleme, hassas özelliklere dayalı biyometrik sınıflandırma sistemleri ve yüz tanıma veritabanları oluşturmak için internetten veya güvenlik kamerası görüntülerinin saklanması da dahil olmak üzere, vatandaşların haklarını tehdit eden belirli yapay zeka uygulamalarını yasaklıyor. Yasa ile iş yeri, okullar ve diğer toplumsal alanlarda kullanıcının güvenlik açıklarını manipüle etmek veya istismar etmek için kullanılan sosyal puanlama ve yapay zeka uygulamaları da yasaklanıyor. Biyometrik tanımlama sistemlerinin güvenlik güçleri tarafından kullanılması, ancak terör saldırısı veya kayıp gibi olağan dışı durumlarda ve adli makamların izniyle mümkün olacak. Yeni yasa, su, enerji, yargı, güvenlik, sağlık ve biyometri gibi yaşamsal öneme sahip alanları yönetmek için kullanılan yapay zeka sistemleri için de düzenlemeler içeriyor. Sağlık, güvenlik, temel haklar, çevre, demokrasi ve hukukun üstünlüğüne yönelik önemli potansiyel zararların önüne geçilmesi için bu alanlarda kullanılacak yapay zeka uygulamalarına ayrıntılı belgeler, net kullanıcı bilgileri, insan gözetimi gibi katı koşullar getiriliyor. Yasa kapsamında, "deepfake" adı verilen, yapay veya değiştirilmiş görsellerin, ses veya video içeriklerinin açıkça belirtilmesi de zorunlu olacak. Avrupa Yapay Zeka Yasası, AB vatandaşlarının, yapay zeka sistemleri hakkında şikayette bulunma ve haklarını etkileyen yüksek riskli yapay zeka sistemlerine dayalı kararlar hakkında bilgi edinmelerine de olanak sağlayacak.  Avrupa Parlamentosu İç Pazar Komitesi eş raportörü Brando Benifei, riskleri azaltmak, fırsatlar yaratmak, ayrımcılıkla mücadele etmek ve şeffaflık getirmek için yapay zeka konusunda dünyanın ilk bağlayıcı yasasının hayata geçirildiğini söyledi. İtalyan parlamenter, yasa sayesinde kabul edilemez yapay zeka uygulamalarının Avrupa'da yasaklanacağını ve vatandaşların haklarının korunacağını vurguladı.Parlamento Sivil Özgürlükler Komitesi eş raportörü Dragos Tudorache de, "AB amacına ulaştı. Yapay zeka kavramını toplumlarımızın temelini oluşturan temel değerlere bağladık" dedi. Avrupa Yapay Zeka Yasası, AB Komisyonu’nun onayının ardından resmi gazetede yayımlanacak. Yasa, Mayıs ayından itibaren, 2 yıl içinde aşamalı olarak bütün birlik genelinde yürürlüğe girecek. Kabul edilemez yapay zeka sistemlerine yönelik yasaklar 6 ay sonra, ChatGPT ve Midjourney gibi üretken yapay zeka sistemlerine ilişkin kurallar da önümüzdeki yıl uygulamaya konacak. Yasaya ilişkin nihai kurallar da, yapay zeka uygulamalarının ön yargılı ya da ayrımcı olup olmadığı konusundaki insan hakları testlerinin ardından Mayıs 2026'da yürürlüğe girmiş olacak. Yasada belirtilen kuralları ihlal eden şirketler, toplam cirolarının yüzde 7'si oranında para cezasına çarptırılabilecek."""

"""1) Metin içinde “yapay” ifadesinin kaç defa geçtiğini bulan programı yazınız.
	Ornek Çıktı : “Metin içerisinde ‘yapay’ kelimesi 25 defa kullanılmıştır.”"""

#Soru -1 
# count = metin.count("yapay")
# print(count)

#Soru - 2
"""2) Metin içinde “zeka”  ifadesinin geçtiği 
konumları (başlangıc ve bitiş konumları ) ekrana yazdıran programı yazınız."""

# aranacakKelime = "zeka"
# konum = -1
# sayac = 0
# kucukMetin = metin.lower()
# while True: 
#     konum = kucukMetin.find(aranacakKelime, konum+1)
#     if konum > -1:
#         print("Kelime Başlangıcı :", konum," - ",konum+len(aranacakKelime))
#         sayac +=1
#     else:
#         print("Metin Sonuna ulaşıldı.")
#         break
        
# print(sayac)

#Soru - 3
"""3) Metin içinde geçen küçük harf ve büyük harfleri yazdıran programı yazınız.
	Örn.Çıktı : “Metin içinde …. adet küçük, …. adet büyük harf tespit edilmiştir.”"""
# kucuk = 0
# buyuk = 0
# for hrf in metin:
#     if hrf.islower():
#         kucuk+=1
#     if hrf.isupper():
#         buyuk+=1

# print("Metin içinde ", kucuk, "Adet kucuk harf ve ", buyuk, "adet buyuk harf var")

#Soru-4
"""4)  Metin içinde bulunan non-alphanumeric karakterlerin sayısını bulan programı yazınız."""
# sayac = 0
# for hrf in metin:
#     if hrf.isalnum():
#         sayac +=1

# print(sayac)

#Soru - 5
"""5) Metin içinde ascii karakter tablosunda bulunmayan harf sayısını bulan programı yazınız."""

# sayac = 0
# for hrf in metin:
#     if not hrf.isascii():
#         sayac+=1
# print(sayac)

#Soru -6 
"""6) Metin içinde geçen “yasa” ifadesini, “Kanun” ifadesi ile değiştiren 
ve kaç adet değişiklik yapıldığını belirten programı yazınız."""

# yeniMetin = metin.replace("yasa","Kanun")

# print(yeniMetin)

# gunler = ["pazar", "p.tesi","salı"]
# renkler = ["mor", "mavi", "yeşil",1,2]
# gunler.extend(renkler)
# gunler.extend("mor")
# print(gunler)
# print(renkler.sort())

# metin = "Python;2;sinifi;ortalığı;yıkıp;geçiyor"
# mtnL = metin.split(";")
# print(mtnL)
# mtnL.reverse()
# gunler = ["pazar", "p.tesi","salı"]

# print(gunler.count("pazar"))
