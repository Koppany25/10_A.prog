#Adatok:
#   Fájlban: Dolgozók nevei
#               Mellette hogy mennyi palacsintát ettek meg

#1.Olvasd be a fájlt

name = "imput.txt"
file = open(name, "r")
file_l = file.readlines()
file.close()

name_l = []
pk_l = []

for i in range(len(file_l)):
    _lista = file_l[i].strip()
    print(_lista)
    _lista_p = _lista.split()
    name_l.append(_lista_p[0])

    _l = []
    for j in range(1, len(_lista_p)):
        _l.append(int(_lista_p[j]))
    pk_l.append(_l)

print(name_l)
print(pk_l)
for i in range(len(pk_l)):
    print(len(pk_l[i]))

#2. Írd ki az adatokat
#   "Név\tJanuar\tFebruar\tMarch\tApril\tMay\tAugust\tSeptember\tOctober\tDecember"