import os
from datetime import datetime
class FileManager():
    """
        Dosya yönetici sınıfların taslağı
    """

    def __init__(self):
        print("Abstract Sınıf Constructor ı")

    def readEntireFile(self, path:str)->str:
        """
            Okunacak olan dosyanın içeriğini döndüren fonksiyon
        """
        raise Exception ("Dosya okuma fonksiyonu implement edilmedi")
    

    def writeToFile(self, path:str,data:any):
        """
            Dosyaya bilgi yazdıracak olan fonksiyon
        """
        raise Exception ("Dosya yazma fonksiyonu implement edilmedi")
    
    def deleteFile(self, path:str):
        """
            Dosyayı sistemden silecek olan fonksiyon
        """
        if os.path.exists(path):
            os.remove(path)
        else:
            print("Dosya bulunamadı...")
    
    def getFileSize(self, path:str)->int:
        """
            Dosya boyutunu alacak olan fonksiyon
        """
        if os.path.exists(path):
            return os.path.getsize(path)
        else:
            print("Dosya bulunamadı")
            return None
        
    def getFileCreationTime(self, path:str) -> datetime:
        """
            Dosyanın yaratılma zamanını verecek olan fonksiyon
        """

        if os.path.exists(path):
            return datetime.fromtimestamp(os.path.getctime(path))
        else:
            print("Dosya Bulunamadı")
            return None
        
    def getFileModificationTime(self, path:str) -> datetime:
        """
            Dosyanın değiştirilme zamanını verecek olan foksiyon
        """

        if os.path.exists(path):
            return datetime.fromtimestamp(os.path.getmtime(path))
        else:
            print("Dosya bulunamadı")
            return None