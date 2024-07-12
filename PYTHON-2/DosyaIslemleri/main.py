import os

apath = "/home/debinci/Desktop/proje/PYTHON-2/DosyaIslemleri/Dosyalar/yeni.txt"
rpath = "PYTHON-2/DosyaIslemleri/Dosyalar/yeni.txt"

# if os.path.exists(apath):
#     print("Evet dosya mevcut")
# else:
#     print("Dosya mevcut deeel")

# dosya = open(apath,"r", encoding="utf-8")
# icerik = dosya.read()
# print(icerik)
# print(dosya.tell())

# dosya = open(apath, "r", encoding="utf-8")
# icerik = dosya.read(5)
# print(icerik)
# print(dosya.tell())

# dosya = open(apath, encoding="utf-8")

# icerik = dosya.readlines()
# #print(icerik)
# dosya.close()
# for i in icerik:
#     print(i,end="")

# dosya = open(apath, "r+", encoding="utf-8")
# dosya.write("bunu da r+ la yazdım"+"\n")
# print("Seeker Konumu : ", dosya.tell())
# dosya.seek()
# icerik = dosya.read()
# print(icerik)

# dosya.close()

# data = ["Birinci Satır\n", "İkinci Satır\n", "Ücüncü Satir\n"]

# dosya = open(apath,"a+", encoding="utf-8")
# dosya.seek(2,0)
# dosya.writelines(data)

dosya = open(apath, "w", encoding="utf-8")
print(dosya.tell())
dosya.flush()

