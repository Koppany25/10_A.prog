import file_fvk as file

sorok = file.beolvas("input6.txt")
print(sorok)

egysor = sorok[0].split(",")
print(egysor)

szamok = file.str_int(egysor)
print(szamok)