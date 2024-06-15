import csv

path = "/home/debinci/Desktop/proje/PYTHON-1/Dosyaİslemleri/JSON/sinif.csv"

# with open(path, encoding="utf-8") as file:
#     metin = csv.reader(file, delimiter=",")
#     #print(metin)

#     for line in metin:
#         print(line)

# lines = []
# with open(path, encoding="utf-8") as file:
#     for line in file:
#         lines.append(line.strip().split(","))

# for i in lines:
#     print(i)

path2 = "/home/debinci/Desktop/proje/PYTHON-1/Dosyaİslemleri/JSON/sinif2.csv"
lines=[]
with open(path, encoding="utf-8") as file:
    metin = csv.reader(file)
    with open(path2,"w") as file2:
        toWrite = csv.writer(file2)

        for line in metin:
            lines.append(line)
            #toWrite.writerow(line)

#print(lines)

for i in range(len(lines)):
    for j in range(len(lines[0])):
        print(lines[i][j], end="\t")
    print()

