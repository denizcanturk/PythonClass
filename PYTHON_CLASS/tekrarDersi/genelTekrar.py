#Değişkenlere Değer Atam
input("Devam için enter'a basın...")

x = y = z = "Orange"
print(x)
print(y)
print(z)

input("Devam için enter'a basın...")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

input("Devam için enter'a basın...")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

input("Devam için enter'a basın...")

x = 5
y = 10
print(x + y)

input("Devam için enter'a basın...")


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 

input("Devam için enter'a basın...")

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

input("Devam için enter'a basın...")

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

input("Devam için enter'a basın...")

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

input("Devam için enter'a basın...")

#VERİ TİPLERİ
x = 20.5
print(type(x))
x = "Hello World"
print(type(x))
x = 5
print(type(x))
x = 1j
print(type(x))


x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = {"name" : "John", "age" : 36} 
print(type(x))	
x = range(6)
print(type(x))

input("Devam için enter'a basın...")

#BOOLEAN
print(10 > 9)
print(10 == 9)
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 

#String Veri Tipi
input("Devam için enter'a basın...")

a = "Hello, World!"
print(a[1])

input("Devam için enter'a basın...")

for x in "banana":
  print(x)

input("Devam için enter'a basın...")

a = "Hello, World!"
print(len(a))

input("Devam için enter'a basın...")

txt = "The best things in life are free!"
print("free" in txt)

input("Devam için enter'a basın...")

b = "Hello, World!"
print(b[2:5])

input("Devam için enter'a basın...")

b = "Hello, World!"
print(b[:5])

input("Devam için enter'a basın...")

b = "Hello, World!"
print(b[-5:-2])

input("Devam için enter'a basın...")

a = "Hello, World!"
print(a.upper())

input("Devam için enter'a basın...")

a = "Hello, World!"
print(a.lower())

input("Devam için enter'a basın...")

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

input("Devam için enter'a basın...")

a = "Hello, World!"
print(a.replace("H", "J"))

input("Devam için enter'a basın...")

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

input("Devam için enter'a basın...")

a = "Hello"
b = "World"
c = a + b
print(c)

input("Devam için enter'a basın...")

age = 36
txt = "My name is John, I am " + age
print(txt)

input("Devam için enter'a basın...")

age = 36
txt = f"My name is John, I am {age}"
print(txt)

input("Devam için enter'a basın...")

price = 59
txt = f"The price is {price} dollars"
print(txt)

input("Devam için enter'a basın...")

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

input("Devam için enter'a basın...")

txt = f"The price is {20 * 59} dollars"
print(txt)

input("Devam için enter'a basın...")

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x) 

input("Devam için enter'a basın...")

txt = "Welcome to my world"

x = txt.title()

print(x) 

input("Devam için enter'a basın...")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) 

input("Devam için enter'a basın...")

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36) 

input("Devam için enter'a basın...")

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit()) 

input("Devam için enter'a basın...")

#List Veri Yapısı

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


list1 = ["apple", "banana", "cherry"]
print(type(list1))
list2 = [1, 5, 7, 9, 3]
print(type(list2))
list3 = [True, False, False]
print(type(list3))


input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry", 5, 7, 9]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[2:])

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) 

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

input("Devam için enter'a basın...")

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

input("Devam için enter'a basın...")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

input("Devam için enter'a basın...")

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

input("Devam için enter'a basın...")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

input("Devam için enter'a basın...")

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

input("Devam için enter'a basın...")

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

input("Devam için enter'a basın...")

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 

input("Devam için enter'a basın...")

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

input("Devam için enter'a basın...")

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 
for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 

input("Devam için enter'a basın...")

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

input("Devam için enter'a basın...")

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) 

input("Devam için enter'a basın...")
#Set Veri Yapısı
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
print(type(thisset))



input("Devam için enter'a basın...")

for x in thisset:
  print(x) 

input("Devam için enter'a basın...")

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

input("Devam için enter'a basın...")

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 

input("Devam için enter'a basın...")

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 

input("Devam için enter'a basın...")

#Dict Veri Yapısı
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict)) 


input("Devam için enter'a basın...")

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
x = thisdict.get("model")
print(x)

x = thisdict.keys() 
print(x)

x = thisdict.values() 
print(x)

input("Devam için enter'a basın...")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change 

input("Devam için enter'a basın...")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 

input("Devam için enter'a basın...")

thisdict.update({"year": 2020}) 
print(thisdict)


input("Devam için enter'a basın...")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

input("Devam için enter'a basın...")

for x in thisdict:
  print(x) 

input("Devam için enter'a basın...")

for x in thisdict.keys():
  print(x) 

input("Devam için enter'a basın...")

for x, y in thisdict.items():
  print(x, y) 

input("Devam için enter'a basın...")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

input("Devam için enter'a basın...")

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 
print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


input("Devam için enter'a basın...")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

input("Devam için enter'a basın...")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"Volume": 2500}) 

print("SONA GELDİĞİNİZ İÇİN TEBRİKLER...")