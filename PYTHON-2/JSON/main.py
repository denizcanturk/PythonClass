# import json
# path = "/home/debinci/Desktop/proje/PYTHON-2/JSON/myJson.json"

# myDict = {
#     "Marka" : "Hyundai",
#     "Model" : 2024,
#     "Kasa"  : "HatchBack",
#     "Motor" : "Elektrikli",
#     "Rengi" : "Gri",
#     "Çekici" : None,
#     "Çelik Jant" : False,
#     "Filmli Cam" : True
# }

# # jString = json.dumps(myDict)
# # print(jString)

# # a = '{"Marka": "Hyundai", "Model": 2024, "Kasa": "HatchBack", "Motor": "Elektrikli", "Rengi": "Gri", "\u00c7ekici": null, "\u00c7elik Jant": false, "Filmli Cam": true}'

# # newDict = json.loads(a)
# # print(newDict)

# # jString = json.dumps(myDict, indent=4, sort_keys=True) #Human Readable
# # print(jString)

# a = '{"Marka": "Hyundai", "Model": 2024, "Kasa": "HatchBack", "Motor": "Elektrikli", "Rengi": "Gri", "\u00c7ekici": null, "\u00c7elik Jant": false, "Filmli Cam": true}'

# with open(path,"w") as file:
#     json.dump(a,file)

# # with open(path) as file:
# #     data = json.load(file)

# # print(data)

import requests
import json
url = "https://api.jsonbin.io/v3/qs/66ad224ee41b4d34e41ac7bf"

response = requests.get(url)

data = json.dumps(response.json(),indent=4)
print(type(data))
print(data)