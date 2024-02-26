file = open("Feladat file/file1.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
atlag = szum/len(szamok)
print(atlag)

print("-------------------------------------------------------------------")

file = open("Feladat file/file2.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(2, len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
atlag = szum/len(szamok)
print(atlag)

print("-------------------------------------------------------------------")

file = open("Feladat file/file3.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(2, len(sorok)-1):
    szamok.append(int(sorok[i].strip()))
print(szamok)

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
atlag = szum/len(szamok)
print(atlag)

print("-------------------------------------------------------------------")

file = open("Feladat file/file4.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
atlag = szum/len(szamok)
print(atlag)

print("-------------------------------------------------------------------")

#Nem működik

file = open("Feladat file/file5.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(2, len(sorok)-1):
    szamok.append(int(sorok[i].strip()))
print(szamok)

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
atlag = szum/len(szamok)
print(atlag)

print("-------------------------------------------------------------------")

#Nem működik

file = open("Feladat file/file6.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(2, len(sorok)-1):
    szamok.append(int(sorok[i].strip()))
print(szamok)

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
atlag = szum/len(szamok)
print(atlag)