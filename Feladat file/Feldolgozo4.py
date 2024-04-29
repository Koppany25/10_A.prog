file = open("Feladat file/file12.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(sorok[i].strip())
print(szamok)

print("-----------------------------------------------------")

