import random

szaz = []
diak = int(input("diákok száma: "))

for i in range(diak):
    a = random.randint(0, 100)
    szaz.append(a)
print(szaz)

maxx = szaz[0]
for i in range(len(szaz)):
    if maxx < szaz[i]:
        maxx = szaz[i]

minn = szaz[0]
for i in range(len(szaz)):
    if minn > szaz[i]:
        minn = szaz[i]

print(maxx, minn)

print("-----------------------------------------------")#2


xdb = 0
for i in range(len(szaz)):
    if maxx == szaz[i]:
        xdb += 1

mdb = 0
for i in range(len(szaz)):
    if minn == szaz[i]:
        mdb += 1

print(xdb, mdb)

print("-----------------------------------------------")#3

summ = 0
for i in range(len(szaz)):
    summ += szaz[i]

atlag = summ/diak
print(atlag)

print("-----------------------------------------------")#4

szaz2 = []

for i in range(diak):
    a = random.randint(0, 100)
    szaz2.append(a)
print(szaz2)

summ2 = 0
for i in range(len(szaz2)):
    summ2 += szaz2[i]

atlag2 = summ2/diak
print(atlag2)

if atlag > atlag2:
    print(f"{atlag} nagyobb mint {atlag2}")
elif atlag < atlag2:
    print(f"{atlag} nagyobb mint {atlag2}")
else:
    print("egyenlőek")



















