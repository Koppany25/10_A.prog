'''nemjo = True
while nemjo:
    szam_str = input("adj meg egy számot: ")
    if szam_str.isdecimal():
        nemjo = False
        szam = int(szam_str)

if szam < 3:
    print("x kissebb mint 3")
elif szam > 3:
    print("x nagyobb mint 3")
else:
    print("x egynelő 3")

print("---------------------------------")

def kiir(str):
    print(str)
kiir(5)

print("---------------------------------")

def g_fv(x,y,z):
    return x*x+y+z/2

x=g_fv(5,3,4)
kiir(x)

print("---------------------------------")

def lista_osszeg(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    return sum

l1 = [1,3,5,7]
l2 = [7,2,9]
l3 = [6,3,0,4]
print(lista_osszeg(l1))
print(lista_osszeg(l2))
print(lista_osszeg(l3))

print("---------------------------------")

def lista_atlag(lista):
    sum = lista_osszeg(lista)
    return sum/len(lista)

print(lista_atlag(l1))
print(lista_atlag(l2))
print(lista_atlag(l3))

print("---------------------------------")

def szamok_beker():
    els = int(input("elso szam: "))
    mas = int(input("masodik szam: "))
    return(els,mas)

msz = int(input("Menü számod: "))
if msz == 1:
    els,mas = szamok_beker()
    print(add(els,mas))

print("---------------------------------")

l1 = []
l2 = list()
l3 = [1,3,7,"szia"]
gy = ["alma","citrom","barack","pomelo"]
print(gy[0])
print(gy[-1])
print(gy[1:3])
print(gy[2:])
print(gy[:])
print(gy[::2])

print("---------------------------------")

def nagy_betu(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].upper()
    return lista

print(gy)
print(nagy_betu(gy[:]))
print(gy)

print("---------------------------------")

d1 = {}
d2 = dict()
d3 = {"nev": "dobostorta",
      "szeletek": 12,
      "elfogyott": "false"}
print(d3["szeletek"])

print("---------------------------------")

t1 = ()
t2 = ("banan", "barack")

print("---------------------------------")

s1 = {}
s = {"hetfo", "kedd"}

print("---------------------------------")

import random

m = 4
n = 7
het = [[0]*n for j in range(m)]

for i in range(m):
    for j in range(n):
        het[i][j] = random.randint(0, 9)
        
for x in het:
    for y in x:
        print(y, end = " ")
    print("\n")

print("---------------------------------")
#összen mennyi eladás

x = 0
for i in range(m):
    for j in range(n):
        x = het[i][j] + x
print(x)

print("---------------------------------")
#hetente mennyi eladás

x = 0
for j in range(n):
        x = het[0][j] + x
print(f"elso het ={x}")

x = 0
for j in range(n):
        x = het[1][j] + x
print(f"masodik het ={x}")

x = 0
for j in range(n):
        x = het[2][j] + x
print(f"harmadik het ={x}")

x = 0
for j in range(n):
        x = het[3][j] + x
print(f"utso het ={x}")

print("---------------------------------")
#legnagyobb eladással rendelkező hét

print("maximális összegü hét:")
maxx = 0
max_sor = []

for x in het:
    summ = sum(x)
    if summ > maxx:
        maxx = summ
        max_sor = x

print(maxx)
print(max_sor)

print("---------------------------------")
#eladás mentes napok száma

db = 0
for i in range(m):
    for j in range(n):
        if het[i][j] ==0:
            db += 1
print(db)

print("---------------------------------")
#legkissebb páratlan eladással rendelkező nap

x = 0
np = 0
a = 40
while np != 7:
    for i in range(m):
        x = het[i][np] + x
        if x % 2 != 0:
             if x > a:
                a = x
    np += 1
print(a)

print("---------------------------------")

maxx = 0
ind = 0
l = [23, 123, 7]
for i in range(len(l)):
    if l[i] > maxx:
        maxx == l[i]
        ind == i
print(maxx)
print(ind)

print("---------------------------------")'''
