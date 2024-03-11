"""
1. Fájl átnevezése: osztály_név.py

Feladatok:
1. A beolvas fv-ben valósítsd meg, hogy a paraméterben megadott fájlt beolvassa, és térjen vissza a szám listával az átalakítások után
2. A feladat1,2 stb fv-ben valósítsd meg a kért eljárásokat! A fájl beolvasásához használd a beolvas() függvényedet!
3. feladat1(): számold ki a fájlban található számok összegét a tanult prog tétel segítségével!
4. feladat2(): számold ki a fájlban található számok átlagát a tanult prog tétel segítségével!
5. feladat3(): számold ki a fájlban található számok minimumát a tanult prog tétel segítségével!
6. feladat4(): számold ki a fájlban található számok maximumát a tanult prog tétel segítségével!

Kiírások:
feladat1: [eredmény]
feladat2: [eredmény]
feladat3: [eredmény]
feladat4: [eredmény]
A ": " után csak az eremény szerepeljen

A dolgozat python fájlját küldd el a andrasi.norbert@puskas.hu-ra az alábbi tárggyal:
[osztály][filebeolvasas2] név 
"""



def beolvas(fajlnev):
    fajl = open(fajlnev, encoding="utf-8")
    sorok = fajl.readlines()
    fajl.close()
    return sorok



def feladat1(elso, utolso):
    sorok = beolvas("input")
    szamok=[]
    for i in range(len(sorok)):
        szamok.append(sorok[i].split(","))
    osszeg = 0
    for i in range(elso, len(szamok[0])-utolso):
        osszeg += int(szamok[0][i])
    return osszeg



def feladat2(elso, utolso):
    sorok = beolvas("input")
    szamok=[]
    for i in range(len(sorok)):
        szamok.append(sorok[i].split(","))
    osszeg = 0
    for i in range(elso, len(szamok[0])-utolso):
        osszeg += int(szamok[0][i])
    return osszeg // len(szamok[0])



def feladat3(elso, utolso):
    sorok = beolvas("input")
    szamok=[]
    for i in range(len(sorok)):
        szamok.append(sorok[i].split(","))
    minx = int(szamok[0][1])
    for i in range(elso, len(szamok[0])-utolso):
        if minx > int(szamok[0][i]):
            minx = int(szamok[0][i])
    return minx



def feladat4(elso, utolso):
    sorok = beolvas("input")
    szamok=[]
    for i in range(len(sorok)):
        szamok.append(sorok[i].split(","))
    maxx = int(szamok[0][1])
    maxi = 0
    for i in range(elso, len(szamok[0])-utolso):
        if maxx < int(szamok[0][i]):
            maxx = int(szamok[0][i])
            maxi = i
    return maxx



print(f"feladat1: {feladat1(1, 1)}")
print(f"feladat2: {feladat2(1, 1)}")
print(f"feladat3: {feladat3(1, 1)}")
print(f"feladat4: {feladat4(1, 1)}")