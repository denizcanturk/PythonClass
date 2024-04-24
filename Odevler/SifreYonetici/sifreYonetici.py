# Kullanıcı adı ve şifresi bir text dosyasında tutulur
# Kullanıcı adı ve şifresi girilirken tek satırda, boşlu bırakılmadan "|" karakteri ile ayrılarak girilmelidir
# Program, şifre dosyasını görüntüleme, kullanıcı ekleme, mevcut kullanıcıya ait şifreyi değiştirebilme ve kullanıcı silme özelliğine sahip olmalıdır
# Yeni kullanıcılar yeni bir satır olarak eklenir


def goruntule():
    dosya = open("/home/debinci/Desktop/NOVA_Dersler/Ders-16/sifre.txt","r")
    for line in dosya:
        kullanici, sifre = line.split("|")
        print("Kullanıcı Adı: {}\t Sifre: {}".format(kullanici, sifre.replace("\n","")))

def ekle():
    kullanici = input("Kullanıcı Adi Giriniz: ")
    sifre = input("Sifre Giriniz: ")
    dosya = open("/home/debinci/Desktop/NOVA_Dersler/Ders-16/sifre.txt","a")
    dosya.write(kullanici+"|"+sifre)

def sifreDegistir():
    satirlar = []
    kullaniciMevcutMu=False
    kullanici = input("Hangi kullanici : ")
    yeniSifre = input("Yeni Sifre : ")
    dosya = open("/home/debinci/Desktop/NOVA_Dersler/Ders-16/sifre.txt","r")
    
    for satir in dosya:
        satirlar.append(satir.replace("\n",""))
    dosya.close()

    i = 0
    for satir in satirlar:
        if kullanici in satir:
            satirlar[i]= kullanici+"|"+yeniSifre+"\n"
            kullaniciMevcutMu = True
            break
        i+=1
    # if kullaniciMevcutMu is False:
    #     print("{} kullanıcı adı dosyada bulunamadı".format(kullanici))
    #     return
    
    dosya = open("/home/debinci/Desktop/NOVA_Dersler/Ders-16/sifre.txt","w")
    for satir in satirlar:
        dosya.write(satir)
        dosya.write("\n")

def kullaniciSil():
    satirlar=[]
    kullaniciMevcutMu=False

    kullanici = input("Kullanici Adı Giriniz : ")
    dosya = open("/home/debinci/Desktop/NOVA_Dersler/Ders-16/sifre.txt","r")
    for satir in dosya:
        satirlar.append(satir.replace("\n",""))
    dosya.close()

    i = 0
    for satir in satirlar:
        if kullanici in satir:
            satirlar.pop(i)
            kullaniciMevcutMu = True
            break
        i+=1

    # if kullaniciMevcutMu is False:
    #     print("{} kullanıcı adı dosyada bulunamadı".format(kullanici))
    #     return

    dosya = open("/home/debinci/Desktop/NOVA_Dersler/Ders-16/sifre.txt","w")
    for satir in satirlar:
        dosya.write(satir)
        dosya.write("\n")

def main():
    secim = input("Yapmak istediğiniz işlemi seçiniz : \n" + \
                  "1. Kullanıcı ve Şifre Görüntüleme \n" + \
                  "2. Kullanıcı Ekleme\n" + \
                  "3. Kullanıcı Silme\n" + \
                  "4. Şifre Değiştirme\n"+ \
                  "5. Çıkış\n" + \
                  "Seçiminiz : ")
    
main()

