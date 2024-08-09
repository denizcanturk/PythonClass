from filemanager import FileManager

class TxtManager(FileManager):
    """
        FileManager sınıfının Text Dosyaları için özelliştirilmiş implementasyonu
    """

    def readEntireFile(self, path:str)->str:
        with open(path) as file:
            return file.read()
        
    def readLineFromFile(self, path:str)->str:
        with open(path) as file:
            return file.readline()
        
    def readLinesFromFile(self, path:str)->list:
        with open(path) as file:
            return file.readlines()
        
    def writeToFile(self, path: str, data: any):
        with open(path,"w") as file:
            file.write(data+"\n")

    def appendTofile(self, path, data):
        with open(path, "a") as file:
            file.write(data+"\n")

    def deleteFile(self, path):
        super().deleteFile(path)

    def getFileSize(self, path: str) -> int:
        return super().getFileSize(path)
        
    def getFileCreationTime(self, path: str) -> datetime:
        return super().getFileCreationTime(path)
    
    def getFileModificationTime(self, path: str) -> datetime:
        return super().getFileModificationTime(path)

    def findTextInFile(self, path:str, textToFind:str):
        None

    def replaceTextInFile(self, path:str, targetText, newtext):
        None

if __name__ == "__main__":
    path = "/home/debinci/Desktop/proje/PYTHON-2/filemanagers/metin.txt"
    txtmng = TxtManager()
    #txtmng.writeToFile(path,"Bu benim klassdan gelme metnim")
    
