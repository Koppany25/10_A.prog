# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename="input.txt"

file=open(filename, "r")
file_lista=file.readlines()
file.close()

name_list=[]
pancake_list=[]
for i in range(len(file_lista)):
    _lista=file_lista[i].strip()
    _lista_parts=_lista.split()

    # így is lehet: _lista_parts=file_lista[i].strip().split()
    name_list.append(_lista_parts[0])

    _l=[]
    for j in range(1,len(_lista_parts)):
        _l.append(int(_lista_parts[j]))
    pancake_list.append(_l)

print(name_list)
print(pancake_list)
for i in range(len(pancake_list)):
    print(len(pancake_list[i]))

# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
fejlec = ["Név", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


ho = 13 #sor
na = len(name_list) + 1 #oszlop
lst = [[0]*ho for j in range(na)]

#név
j = 0
for i in range(1, na):
        lst[i][0] = name_list[j]
        j += 1


for x in range(len(lst)):
    lst[0] = fejlec


'''j = 0
k = 0
for i in range(1, na):
    for j in range(1, ho):
        lst[i][j] = pancake_list[j][k]
        k += 1
        j += 1'''


for x in lst:
    for y in x:
        print("%3s" %(y), end = " ")
    print("\n")


# 3) Add meg, hogy márciusban ki sütötte a legtöbb palacsintát!
# 4) Add meg, hogy ki sütötte az évben a legkevesebb palacsintát!
# 5) Add meg, hogy az a személy, akinek B-vel kezdődik a neve, Májusban hány palacsintát sütött.
# 6) Volt-e olyan személy, akinek az évben változó teljesítménye volt?
#       Pl: sütött valamennyit, majd a következő hónapban többet, a következőben az előzőnél kevesebbet stb
#       írd ki a személy nevét!






























