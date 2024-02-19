import file_fvk as file

sorok = file.beolvas("input10.txt")
print(sorok)

szamok = file.stringSzetszedoToIntList(sorok[0], e_e_n_k=1)
print(szamok)