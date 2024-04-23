
#ALISTIRMA - 1
#Kullanıcı tarafından bir metin/kelime girilir. Girilen ifade ekrana tersten yazdırılır.
#------------------------------------------------

metin = input("Bir metin giriniz : ")

tersMetin = metin[::-1]

print(metin[::-1])
print(tersMetin)

#ALISTIRMA - 2
#Kullanıcı tarafından metin ve sayılardan olusan bir ifade girilir. Girilen ifade içinde karakterlerin ve sayıların adetleri ekrana yazdırılır.
#------------------------------------------------

text = input("Rastgele bir metin giriniz : ")
digitNum = 0
letterNum = 0

for harf in text:
    if harf.isdigit():
        digitNum+=1
    if harf.isalpha():
        letterNum+=1

print("Metin içerisinde {} adet harf ve {} adet sayı bulunmaktadır".format(letterNum, digitNum))

#ALISTIRMA - 3
#Kullanıcı bir metin/kelime ve bu metin/kelime içinde aranacak bir harf girer. Aranan harfin metin içinde kaç defa geçtigi ekrana yazdırılır.
#------------------------------------------------

mainText = input("Bir uzun metin girin : ").lower()
aranacakHarf = input("Aranacak Harfi girin :").lower()
print("{} harfi, metin içinde {} defa geçmektedir".format(aranacakHarf, mainText.count(aranacakHarf)))

#ALISTIRMA - 4
#Kullanıcı tarafından girilecek olan bir kelimenin “palindrom” olup olmadıgını kontrol edip sonucu ekrana yazdırın.
#------------------------------------------------
word = input("Bir kelime giriniz")

if word == word[::-1]:
    print("Kelimeniz bir palidromdur")
else:
    print("Sadece bir kelime işte...")    

#ALISTIRMA - 5
#Kullanıcı tarafından girilen bir metinin kaç kelimeden olustugunu bulup, ekrana yazdırınız.
#------------------------------------------------

mainText = input("en az 10 kelimelik bir metin girin : ")
wordList = mainText.split(" ")

print("Metniniz {} kelimeden oluşmaktadır.".format(len(wordList)))

#ALISTIRMA - 6
#Kullanıcının girdigi matematiksel ifadeye göre islemi yapıp ekrana yazdırınız.
# NOT : Bir matematiksel islem sadece <sayı><islem><sayi> seklinde olabilir. Orn: 15+14 gibi.

operatorler = ["+","-","*","/"]

islem = input("Matematiksel bir islem girin (Örn:10*12): ")

for n in islem:
  if n in operatorler:
    parcalar= islem.split(n)
    if n == "+":
      sonuc = int(parcalar[0]) + int(parcalar[1])
    if n == "-":
      sonuc = int(parcalar[0]) - int(parcalar[1])
    if n == "*":
      sonuc = int(parcalar[0]) * int(parcalar[1])
    if n == "/":
      sonuc = int(parcalar[0]) / int(parcalar[1])

print("{} = {}".format(islem, sonuc))


#ALISTIRMA - 7
#Rastgele sayılar ile doldurulmus bir tam sayı listesinin, en küçük ve en büyük elemalarını,
# negatif sayıların ve pozitif sayıların adedini ekrana yazdırınız.
#------------------------------------------------

tamSayiList = [12,25,15,36,22,54,69,85,665,-51,-8,-6,54,-53]
sifirdanKucuk = 0

enBuyuk = max(tamSayiList)
enKucuk = min(tamSayiList)

for n in tamSayiList:
  if n < 0:
    sifirdanKucuk +=1
    
print("Elinizdeki listenin en küçük değeri {}, \
en büyük değeri ise {} dir. \
Sayi listenizde toplam {} adet negatif sayı bulunmaktadır.".format(enKucuk, enBuyuk, sifirdanKucuk))

#ALISTIRMA - 8
#Rastgele tam sayılardan olusan iki liste nin elemanları ile ilgili olarak :
#- Her iki listenin elemanlarını içeren üçüncü bir liste olusturun
#- Her iki listenin elemanlarını içeren ancak aynı degerlerin tekrar etmedigi bir liste olusturun
#- Her iki listenin sadece benzersiz (digerinde bulunmayan) degerlerinin bulundugu bir liste olusturun
#- Her iki listenin en büyük ve en küçük degerlerini iceren bir liste olusturun.
#------------------------------------------------

liste1 = [1,5,2,6,9]
liste2 = [8,4,7,2,6]

liste3 = liste1.copy()
liste3.extend(liste2)
print(liste3)

#2
essizListe = liste1.copy()

for eleman in liste2:
    if eleman not in essizListe:
        essizListe.append(eleman)

print(essizListe)
#3
benzersizListe = []

for item in liste1:
    if item not in liste2:
        benzersizListe.append(item)

for item in liste2:
    if item not in liste1:
        benzersizListe.append(item)

print(benzersizListe)
#4
print(max(liste1))
print(min(liste1))

#ALISTIRMA - 9
#Klavyeden “Tamam” girilinceye kadar girilecek olan tam sayıların toplamlarını ve aritmetik ortalamalarını ekrana yazdırınız.
toplam = 0
sayac = 0
ort = 0
while True:
    cevap = input("Giriş yapınız")

    if cevap.isdigit():
        toplam += int(cevap)
        sayac +=1
    elif cevap.lower()=="tamam":
        ort = toplam / sayac
        print("Girilen {} adet sayaının toplamı {}, ortalaması {}".format(sayac,toplam,ort))
        break

##############    İkinci  Yöntem     ##############

liste = []
toplam = 0
sayac = 0
harf = "Tamam"
while True:
    sayı = input("{} inci sayıyı giriniz :".format(sayac+1))

    #if sayı not in liste:
    if sayı.isdigit():
        liste += [int(sayı)]
        sayac += 1
        print(liste)
    elif sayı.lower() == harf.lower():
        for i in liste:
            toplam += i
        print(f"Listenin içindeki sayıların toplamı : {toplam} ")
        print("Liste içindeki sayıların ortalaması ",toplam/sayac)
        break

#ALISTIRMA - 10
#Kullanıcı tarafından girilecek metre cinsinde degerin :
#- mil,
#- inç,
#- yard
#- feet birimlerinden olan miktarlarını ekrana yazdırır.

sayi = int(input("Lütfen bir sayı giriniz :"))
mil = sayi / 1609,344
inc = sayi * 0.0254
yard = sayi * 1.0936133
feet = sayi * 3.28

print("Bir Metre :",mil," mil eder")
print("Bir Metre :",inc," inc eder")
print("Bir Metre :",yard," yard eder")
print("Bir Metre :",feet," feet eder")

#ALISTIRMA - 11
#Klavyeden girilen tam sayının haftanın hangi gününe denk geldigini ekrana yazdırın. Orn.: Gırıs : 2, Cıkıs : Salı gibi
#------------------------------------------------
while True:

    sayi = int(input("Lütfen Bir Sayı Giriniz :"))
    if sayi not in range(1,8):
        print("Haftada kaç gün var?")
        break
    
    if sayi == 1:
        print("Pazartesi")
    elif sayi == 2:
        print("Salı")
    elif sayi == 3:
        print("Çarşamba")
    elif sayi == 4:
        print("Perşembe")
    elif sayi == 5:
        print("Cuma")
    elif sayi == 6:
        print("Cumartesi")
    elif sayi == 7:
        print("Pazar")
    else:
        print("Hafta günlerine eş gelen bir sayı girmediniz")
        break

#ALISTIRMA – 12
#Kullanıcı tarafından girilen ay numarasının hangi aya karsılık geldigini ekrana yazdırın.
#------------------------------------------------
aylar =["OCAK","ŞUBAT","MART", "NİSAN","MAYIS", "HAZİRAN","TEMMUZ","AGUSTOS","EYLÜL","EKİM","KASIM","ARALIK"]
while True:
    sayi = int(input("Lütfen Bir Sayı Giriniz :"))
    if sayi not in range(1,13):
        print("Bizim toplam 12 ayımız var... Bu nerden çıktı")
        break

    if sayi == 1:
        print("Ocak")
    elif sayi == 2:
        print("Şubat")
    elif sayi == 3:
        print("Mart")
    elif sayi == 4:
        print("Nisan")
    elif sayi == 5:
        print("Mayıs")
    elif sayi == 6:
        print("Haziran")
    elif sayi == 7:
        print("Temmuz")
    elif sayi == 8:
        print("Agustos")
    elif sayi == 9:
        print("Eylül")
    elif sayi == 10:
        print("Ekim")
    elif sayi == 11:
        print("Kasım")
    elif sayi == 12:
        print("Aralık")
    else:
        print("Ay günlerine eş gelen bir sayı girmediniz")
        break

    #İKİNCİ ÇÖZÜM ÖNERİSİ
    print(aylar[sayi-1])

#ALISTIRMA - 13
#Kullanıcı 1-100 arasında bir sayı girisi yapar.
#- Eger sayi 3’ün katıysa ekrana : Fizz
#- Eger sayi 5’in katıysa ekrana : Buzz
#- Eger sayi hem 3 ün hem de 5 in katıysa : Fizz Buzz
#- Eger girilen sayi istenen aralik disinda ise hata mesajı ekrana yazdırılmalıdır.
#------------------------------------------------
while True:
    sayi = int(input("Bir ile yüz arasında bir sayı giriniz :"))
    if sayi < 1 and sayi >100:
        print("Girilen sayı 1 ile 100 sayı aralığının dışındadır")
        break
    elif sayi % 3 and sayi % 5 == 0:
        print("Fizz Buzz")
    elif sayi % 5 == 0:
        print("Buzz")
    elif sayi % 3 == 0:
        print("Fizz")


#ALISTIRMA - 14
#Kullanıcı bir ifadenin kaç kere yazdırılacagını ve ifadeyi arada bosluk bırakmadan gırıs yapar.
# Programcının görevi, sayıdan farklı olarak girilen ifadeyi baslangıcta belirtildigi kadar ekrana yazdırır.
#Orn : 7x
#Cıktı :
#x
#x
#x
#x
#x
#x
#x

txtToPrint = input("Girbakalım bişeyler : ")
letterStartIndex = 0
for i in txtToPrint:
    if not i.isdigit():
        letterStartIndex = txtToPrint.index(i)
        if (letterStartIndex == 0):
            print("Hoppala paşam, malkara keşan")
            print("İfaden sayı ile başlamıyor senin.. Hayırdır...")
        break

numberPart = txtToPrint[:letterStartIndex:]
txtPart = txtToPrint[letterStartIndex::]

for i in range(int(numberPart)):
    print(txtPart, ":) İyi bayramlar")

