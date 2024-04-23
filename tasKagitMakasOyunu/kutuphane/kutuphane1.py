oyuncuPuan = 0
bilgisayarPuan = 0
berabere = 0
secenekler = ["taş", "kağıt", "makas"]
girilebilirDegerler = ["1","2","3","q"]

def hesapla(oyuncu, bilgisayar):
    global oyuncuPuan
    global bilgisayarPuan
    global berabere
    
    if oyuncu == bilgisayar:
        print("Berabere...")
        berabere +=1

    elif oyuncu == "taş":

        if bilgisayar == "makas":
            print("Oyuncu kazandı...")
            oyuncuPuan+=1

        elif bilgisayar == "kağıt":
            print("Bilgisayar Kazandı...")
            bilgisayarPuan+=1
        
    elif oyuncu == "makas":

        if bilgisayar == "taş":
            print("Bilgisayar kazandı...")
            bilgisayarPuan +=1
        else:
            print("Oyuncu kazandı...")
            oyuncuPuan +=1

    elif oyuncu == "kağıt":
        if bilgisayar == "makas":
            print("Bilgisayar kazandı")
            bilgisayarPuan +=1
        else:
            print("Oyuncu Kazandı...")
            oyuncuPuan+=1


def puanYazdir():
    print("Oyuncu : {}, Bilgisayar : {}, Berabere : {}".format(oyuncuPuan, bilgisayarPuan, berabere))
    if oyuncuPuan == bilgisayarPuan : 
        print("Sonuç : Berabere")
    elif oyuncuPuan > bilgisayarPuan:
        print("Kazanan : Oyuncu")
    else:
        print("Kazanan : Bilgisayar")
