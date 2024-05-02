# Bu dersin konusu Hata Yakalama...

# Bizim programcı olarak yakalayamadığımız hataları, 
# programın yakalaması için vaziyet alma...
dosyaAdi = "metin.txt"
try:
    dosya = open(dosyaAdi,"r")
    print(dosya.read())
except IOError as i:
    print("Dosya yok kardeşim")
except NameError as r:
    print("Degisken Tanımlanmadı...")
except Exception as e:
    print(str(e))
else:
     dosya.close()
finally: 
   print("Happened...")
