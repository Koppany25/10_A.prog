import file_fvk2 as file

sorok = file.beolvas("Feladat file/file7.txt")
print(sorok)

szamok = file.StringSzetszedoToIntLst(sorok[0])
print(szamok)

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
atlag = szum/len(szamok)
print(atlag)

print("-------------------------------------------------------------------")

#Nem működik

sorok = file.beolvas("Feladat file/file8.txt")
print(sorok)

szamok = file.StringSzetszedoToIntLst(sorok[0], " ", 1)
print(szamok)

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
atlag = szum/len(szamok)
print(atlag)