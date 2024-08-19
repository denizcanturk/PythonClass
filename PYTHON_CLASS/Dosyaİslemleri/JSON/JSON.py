import json

myDict = {"Adi":"Python", "yasi":45, "renkliMi" : False, "hayattaMi" : True, "sevdiğiMeyve":None}

# print(myDict["hayattaMi"])

# for key, val in myDict.items():
#     print(key, val)

# print(myDict)
# print(type(myDict))
# jsonStr = json.dumps(myDict, indent=4,sort_keys=True)
# print(jsonStr)
# print(type(jsonStr))

# try:
#     myJsonStr = '{"Adi": "Python", "yasi": 45, "renkliMi": False, "hayattaMi": true, "sevdi\u011fiMeyve": null}'
#     newDict = json.loads(myJsonStr)
# except Exception as e:
#     print(str(e))
#     print("JSON String Donusum Hatası")
# else:
#     print(type(newDict))
#     print(newDict)

#---------------------------------------------

path = "/home/debinci/Desktop/proje/PYTHON-1/Dosyaİslemleri/JSON/some.json"

with open(path) as jFile:
    data = json.load(jFile)
    print(type(data))
    print(data)

jString = json.dumps(data,indent=4)
#print(jString)

#print(data["cars"][1]["hacim"])

for keys, vals in data["cars"][1].items():
    print(keys,vals)