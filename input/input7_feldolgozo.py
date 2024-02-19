import file_fvk as file

sorok = file.beolvas("input7.txt")
print(sorok)

szamok = file.stringSzetszedoToIntList(sorok[1], ";")
print(szamok)
