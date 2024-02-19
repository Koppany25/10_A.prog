import file_fvk as file

sorok = file.beolvas("file.txt")
print(sorok)

lista = []
lista.append(file.StringSzetszedoToIntLst(sorok[0], separator=" ", elejerol_ennyi_nem_kell= 1, vegerol_ennyi_nem_kell= 0))
lista.append(file.StringSzetszedoToIntLst(sorok[2], separator=" ", elejerol_ennyi_nem_kell= 1, vegerol_ennyi_nem_kell= 0))
lista.append(file.StringSzetszedoToIntLst(sorok[3], separator=" ", elejerol_ennyi_nem_kell= 1, vegerol_ennyi_nem_kell= 0))
print(lista)

for i in range(len(lista)):
    osszeg = 0
    for j in range(len(lista[i])):
        osszeg += lista[i][j]
    print(osszeg)
