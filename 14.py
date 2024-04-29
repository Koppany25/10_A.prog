import random

lista = []
x = 0
while x < 5 or x > 25:
    x = int(input("5..25: "))
    if x < 5 or x > 25:
        print("Hibás adatbevitel! Próbáld újra!")
    else:
        i = 0
        while i < x:
            lista.append(random.randint(-10, 10))
            i += 1
print(lista)

print("-----------------------------------------------")

summ = 0
for i in range(len(lista)):
    summ += i
print(f"A listában levő elemek összege: {summ}")

print("-----------------------------------------------")

nul = 0
neg = 0
for i in range(len(lista)):
    if lista[i] == 0:
        nul += 1
    elif lista[i] < 0:
        neg += 1

if nul > neg:
    print("A listában több nulla van mint negatív!")
else:
    print("Az állítás hamis!")