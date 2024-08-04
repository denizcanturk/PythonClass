import csv

path = "/home/debinci/Desktop/proje/PYTHON-2/CSV/name.csv"
path1 = "/home/debinci/Desktop/proje/PYTHON-2/CSV/name2.csv"

# with open(path, encoding="utf-8") as file:
#     icerik = csv.reader(file, delimiter=";")

#     for satir in icerik:
#         print(satir)

# data = []

# with open(path, encoding="utf-8") as file:
#     icerik = csv.reader(file, delimiter=";")

#     basliklar = next(icerik)

#     for satir in icerik:
#         data.append(satir)
# print(f"{basliklar = }")
# print(data)
# print(icerik.line_num)

# print(len(data[0]))

baliklar = ["Adi","Soyadi","DT"]

bilgiler = [["Erkan", "ALTINTAŞ", 1978],
            ["Rahşan", "ERDOĞAN", 1990]
]

with open(path1, "w", encoding="utf-8") as file:
    yazdir = csv.writer(file,delimiter="-")
    yazdir.writerow(baliklar)
    yazdir.writerows(bilgiler)