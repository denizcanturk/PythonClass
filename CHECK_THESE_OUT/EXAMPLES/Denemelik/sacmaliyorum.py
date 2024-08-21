# a = [[1,2,3],[3,4,5],[4,5,6]]


# def func(a):
#     for i in a:
#         print(i)
#         func(i)

# func(a)


# 5!

# Permutasyon : 5! / k!(5-k)!

# def fact(n):
#     if n == 0 or n==1 :
#         return 1
#     return n * fact(n-1)

# print(fact(5))

# import tkinter as tk

# def draw_line(canvas):
#     canvas.create_line(50, 50, 150, 50, fill="red")  # Horizontal line
#     canvas.create_line(50, 50, 50, 150, fill="blue")  # Vertical line

# root = tk.Tk()
# canvas = tk.Canvas(root, width=200, height=200)
# canvas.pack()

# draw_line(canvas)

# root.mainloop()

# import random
# kullaniciPuan=0
# compPuan=0
# secenekler=["Taş", "Makas", "Kağıt"]

# while True:
#     #input dan alınan değerin veri tipini hatırlıyor musunuz?
#     kullanici=input("taş için 1, kağıt için 2, makas için 3 giriniz:")
    
#     comp=random.randint(1,3)
#     print("siz:", kullanici, "bilgisayar:", comp)
#     scoreBoard=(kullaniciPuan, compPuan) #Bunu neden böyle kullandınız?
    
#     if kullanici==1 and comp==2:
#         #Burda kullanıcı ya da bilgisyarın puanının katlanarak gitmesini istediğinize emin misiniz?
#         compPuan+=compPuan
#         print(scoreBoard)
#     elif kullanici==1 and comp==3:
#         kullaniciPuan+=kullaniciPuan
#         print(scoreBoard)
#     elif kullanici==2 and comp==3:
#         compPuan+=compPuan
#         print(scoreBoard)
#     elif kullanici==2 and comp==1:
#         kullaniciPuan+=kullaniciPuan
#         print(scoreBoard)
#     elif kullanici==3 and comp==1:
#         compPuan+=compPuan
#         print(scoreBoard)
#     elif kullanici==3 and comp==2:
#         kullaniciPuan+=kullaniciPuan
#         print(scoreBoard)

#     else:
#         #Print score boardu gerçekten her if else if statementinin altına koymak zorunda mısınız?
#         print(scoreBoard)

#     #VE SON OLARAK : Gerçekten bu kadar çok if else if e ihtiyacınız var mı? Tek if-else ile 
#     # çözebilir(mi)siniz :))

try:
    with open("/home/debinci/Desktop/Project1/csvv.csv", "+a") as file:
        file.seek(0)
        icerik = file.read()
        print(icerik)
except:
    print("sıçtık...")