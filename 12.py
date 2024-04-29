import random

lista = []
x = 0
while x < 10 or x > 20:
    x = int(input("10..20: "))
    if x < 10 or x > 20:
        print("Hibás adatbevitel! Próbáld újra!")
    else:
        i = 0
        while i < x:
            lista.append(random.randint(1, 5))
            i += 1
print(lista)

print("-----------------------------------------------")

summ = 0
for i in range(len(lista)):
    summ += i
print(f"A listában levő elemek összege: {summ}")

print("-----------------------------------------------")

maxx = 0
index = 0
for i in range(len(lista)):
    if lista[i] > maxx:
        maxx = lista[i]
        index = i
print(f"A listában levő legnagyobb elem {maxx}, helye: {index}")