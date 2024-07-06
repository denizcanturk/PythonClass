# a listesini içinde ki elemanlarden a harfi 
# içerenlerden oluşan bir b listesi oluşturunuz

a = ["elma","muz","çilek","kiwi", "armut"]

b = []

b = [meyve for meyve in a if "a" in meyve]
print(b)


# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] == "a":
#             b.append(a[i])

# print(b)

# for i in a :
#     if "a" in i:
#         b.append(i)