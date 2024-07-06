ascii_letters = 'abccdefgghiijklmnooprsstuuvyz'
turkish_letters = 'abcçdefgğhıijklmnoöprsştuüvyz'

#Böylece translate ve maketrans fonksiyonlarını da anlamış oluyoruz :)

#Hangi harfin neye çevrilmesi gerektiği ile ilgili ascii stringden bir maske oluşturuluyor 
#ascii listesinde, TÜRKÇE KARAKTERLERE KARŞILIK GELEN YERLERE KOYULAN ILAVE KARAKTERLERE
#lütfen dikkat edin!!! 

#Daha sonra bir dönüşüm tablosu oluşturuluyor.Bu dönüşüm tablosu, gerçek karakterlerin
#sıralanması sırasında bir maske olarak kullanılıp, sıralamanın ASCII imiş gibi yapılmasını
#sağlıyor.

turkishTable = str.maketrans(turkish_letters, ascii_letters)

s = 'Çınar'

s.lower().translate(turkishTable)
#'cinar'
player_list = ['Zeynep','Ahmet', 'Çınar', 'Oğuz']
mliet = [1,2,3,4]

sorted(player_list, key=lambda s: s.lower().translate(turkishTable))
#['Ahmet', 'Çınar', 'Oğuz', 'Zeynep']
print(player_list + mliet)