"""int = int(input("szám: "))

if int % 2 == 0:
    print("a szám páros")
else:
    print("a szám páratlan")

print("-----------------------------------------------")

str = "Sajttorta"
i = 0
N = len(str)

while i < N and not (str[i] == "a"):
    i += 1
van = i < N

print("-----------------------------------------------")

'''
mermaid
---
title: cím
---
flowchart TD
    i := 1
'''

print("-----------------------------------------------")

str = "A páva finom, de a szarvas finomabb. What do you think?"
c = 0

for i in range(len(str)):
    if str[i] == "." or str[i] == "!" or str[i] == "?":
        c += 1
if c > 1:
    print("több mondatból áll")
else:
    print("nem több mondat")"""

print("-----------------------------------------------")

lista = [["Béla", "f", "18:00"],
      ["Judit", "n", "18:01"],
      ["Zoli", "f", "18:06"],]
i = 0

'''for i in range(len(lista)):
    #print(lista[i])
    #for j in range(len(lista[i])):
        #print(lista[i][j])
    egysor = ""
    for j in range(len(lista[i])):
        egysor += lista[i][j] + " "
    print(egysor)'''

while not(lista[i][1] == "n"):
    i = i + 1
print(lista[i][0])