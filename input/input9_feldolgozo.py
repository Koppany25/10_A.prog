file = open("input9.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(2, len(sorok)-2):
    szamok.append(int(sorok[i].strip()))
print(szamok)