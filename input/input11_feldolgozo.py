import file_fvk as file

sorok = file.beolvas("input/input11.txt")
print(sorok)

szamok = file.stringSzetszedoToIntList(sorok[0], " ", 1, 1)
print(szamok)