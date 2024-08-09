from datetime import datetime
from filemanager import FileManager
import csv

class CSVManager(FileManager):
    """
        CSV Dosyaları için sınıf implementasyonu
    """

    def readEntireFile(self, path: str) -> list:
        data = []
        with open(path,newline="") as file:
            content = csv.reader(file)

            for row in content:
                data.append(row)
        return data
    
    def getHeaders(self, path)-> list:
        with open(path,newline="") as file:
            content = csv.reader(file)
            return next(content)
        
    def writeToFile(self, path: str, data: list):
        with open(path,"w",newline="") as file:
            content = csv.writer(file)
            content.writerows(data)

    def appendToFile(self, path, data:list):
        with open(path, "a", newline="") as file:
            content = csv.writer(file)
            content.writerow(data)

    def csvToJson(self, csvPath, jsonPath):
        None

    def updateCellvalue(self, path, refVal, NewValue):
        None

    def deleteFile(self, path: str):
        return super().deleteFile(path)
    
    def getFileSize(self, path: str) -> int:
        return super().getFileSize(path)
    
    def getFileCreationTime(self, path: str) -> datetime:
        return super().getFileCreationTime(path)
    
    def getFileModificationTime(self, path: str) -> datetime:
        return super().getFileModificationTime(path)
    
if __name__ == "__main__":
    csvMng = CSVManager()
    path = "/home/debinci/Desktop/proje/PYTHON-2/filemanagers/isimler.csv"

    textList = [["Adi","Soyadı"],
                ["Deniz","CANTURK"]]
    
    added = ["Aydan", "Geçer"]

    #csvMng.writeToFile(path,textList)
    #csvMng.appendToFile(path, added)
    #print(csvMng.getFileCreationTime(path))

    print(csvMng.readEntireFile(path))