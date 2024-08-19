arabam = {
    "Marka" : "Mercedes",
    "Model" : "E200",
    "yılı" : 2023,
    "Yakiti" : "LPG",
    "Rengi" : "Siyah"
}

arabam2 = dict(marka="Doğan", model="slx", yili=1993, yakiti="LPG", rengi="Gri")

# print(arabam)
# print()
# print(len(arabam))

# print(arabam2["marka"])
# benimMarkam = arabam.get("Marka")
# print(benimMarkam)

# print(type(arabam.keys()))
# print(type(arabam.values()))

# arabam["yılı"] = 2024
# print(arabam)

# items = arabam.items()
# print(items)

# if "Mercedes" in arabam:
#     print("Buldum")
# else : 
#     print("Yogh gardaş... ")

# arabam.update({"Jant":25})
# print(arabam)

# arabam.popitem()
# print(arabam)

# del arabam["Rengi"]
# print(arabam)

# arabam.clear()
# print(arabam)

# for i in arabam:
#      print(i)

# for i in arabam:
#      print(arabam[i])

# for anahtar, deger in arabam.items():
#     print(anahtar + " : " + str(deger))

# seninAraban = arabam.copy()
# seninAraban["Marka"] = "Skoda"
# seninAraban["Model"] = "Fabia"
# seninAraban["yılı"] = 2012

# print(arabam)
# print(seninAraban)

# ailem = {
#     "Anne" : {"Adı": "Rahime", "Yasi": 28},
#     "Baba" : {
#         "Adı" : "Cabbar", 
#         "Yasi":35
#         },
#     "Kardes" : {
#         "Adi" : "Aydan", 
#         "Yasi" : 28
#         }
# }

# for anahtar, degerler in ailem.items():
#     print(anahtar)

#     for deger in degerler:
#         print(deger + " : " , degerler[deger])



listem = [[1 ,5 ,7 ],
          [10,15,18],
          [30,37,39]
         ]

for i in listem:
    for j in i : 
        print(j, end=" ")
    print()
