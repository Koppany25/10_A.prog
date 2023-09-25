nemjo = True
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

'''def szamok_beker():
    els = int(input("elso szam: "))
    mas = int(input("masodik szam: "))
    return(els,mas)

msz = int(input("Menü számod: "))
if msz == 1:
    els,mas = szamok_beker()
    print(add(els,mas))'''

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