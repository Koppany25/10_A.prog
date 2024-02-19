import file_fvk as file

sorok = file.beolvas("input4.txt")
szamok = file.str_int(sorok, 1, 1)
print(szamok)

print("-------------------------------------------")#db

db = len(szamok)
print(db)

print("-------------------------------------------")#összeg

szum = 0
for i in range(len(szamok)):
    szum += szamok[i]
print(szum)

print("-------------------------------------------")#szorzat

szor = 1
for i in range(len(szamok)):
    szor *= szamok[i]
print(szor)

print("-------------------------------------------")#max

mx = 0
for i in range(len(szamok)):
    if mx < szamok[i]:
        mx = szamok[i]
print(mx)

print("-------------------------------------------")#3.szám értéke

print(szamok[2])

print("-------------------------------------------")#min páratlan

mn = 100000000

for i in range(len(szamok)):
    if szamok[i]%2 == 1 and mn > szamok[i]:
        mn = szamok[i]
print(mn)