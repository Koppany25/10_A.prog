import file_fvk as file

sorok = file.beolvas("input/input13.txt")
print(sorok)

szamok = file.stringSzetszedoToIntList(sorok[1], " ", 1, 1)
print(szamok)