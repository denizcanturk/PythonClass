# Kullanıcı adı ve şifresi bir text dosyasında tutulur
#
# Kullanıcı adı ve şifresi girilirken tek satırda, 
#        boşluk bırakılmadan ":" karakteri ile ayrılarak girilmelidir
#
# Program, şifre dosyasını görüntüleme, kullanıcı ekleme, 
#        mevcut kullanıcıya ait şifreyi değiştirebilme ve 
#       kullanıcı silme özelliğine sahip olmalıdır
#
# Yeni kullanıcılar yeni bir satır olarak eklenir

# from pwdLibs import main
from CPwdManager import PasswordManager
#import CPwdManager as c

dosyaKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/PwdManager/sifre.txt"
anahtarKonumu = "/home/debinci/Desktop/proje/Dosyaİslemleri/PwdManager/key.data"

if __name__ == "__main__":
    pwdMng = PasswordManager(dosyaKonumu, anahtarKonumu)
