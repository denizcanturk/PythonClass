from filemanager import FileManager
import json
from datetime import datetime

class JSONManager(FileManager):
    """
        JSON Dosyaları yönetici sınıf implementasyonu
    """

    def readEntireFile(self, path: str) -> dict:
        with open(path) as file:
            return json.load(file)
        
    def writeToFile(self, path: str, data: any):
        None

    def jsonToCSV(self, jsonPath, csvPath):
        None

    def appendToJSON(self, path, data):
        None

    def replaceValue(self, path, targetKey, value):
        None

    def removeKey(self, path, keyToremove):
        None

    def deleteFile(self, path: str):
        super().deleteFile(path)
    
    def getFileSize(self, path: str) -> int:
        return super().getFileSize(path)
    
    def getFileCreationTime(self, path: str) -> datetime:
        return super().getFileCreationTime(path)
    
    def getFileModificationTime(self, path: str) -> datetime:
        return super().getFileModificationTime(path)


if __name__ == "__main__":
    jsonMng = JSONManager()
    path = "/home/debinci/Desktop/proje/PYTHON-2/filemanagers/arabam.json"
    jsonData = {"Marka" : "BMW",
                "Model" : "X5",
                "Hacim" : 2500,
                "Yıl" : 2020,
                "Renk" : "Gri"
    }

    jsonMng.writeToFile(path, jsonData)

