file = open("input2.txt")
sorok = file.readlines()
file.close()
print(sorok)

szamok = []
for i in range(len(sorok)):
    szam_str = sorok[i].strip()
    #print(szam_str)
    szam = int(szam_str)
    #print(szam)
    szamok.append(szam)
print(szamok)

osszeg = 0
for i in range(len(szamok)):
    osszeg += i
print(osszeg)

print("-----------------------------------")

file = open("input2.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szam = int(sorok[i].strip())
    szamok.append(szam)
print(szamok)

print("-----------------------------------")

file = open("input2.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)