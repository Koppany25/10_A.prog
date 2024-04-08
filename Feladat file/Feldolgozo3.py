file = open("Feladat file/file12.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(sorok[i].strip())
print(szamok)

print("-----------------------------------------------------")

file = open("Feladat file/file13.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(1, len(sorok)):
    szamok.append(sorok[i].strip())
print(szamok)

print("-----------------------------------------------------")

file = open("Feladat file/file14.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(1, len(sorok)-1):
    szamok.append(sorok[i].strip())
print(szamok)

print("-----------------------------------------------------")

file = open("Feladat file/file15.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(1, len(sorok)):
    szamok.append(sorok[i].strip())
print(szamok)