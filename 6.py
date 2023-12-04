print(5 & 6) #4
print(5 | 6) #7
print(5 ^ 6) #3
print(~ 5) #-6
print(~ 6) #-7
#bit eltolás (balra)
print(5 << 1) #10
print(5 << 2) #20
#bit eltolás (jobbra)
print(5 >> 1) #2
print(5 >> 2) #1

print("------------------------")

l = [2, 3, 4]
print(l)

l.append(6) # [2, 3, 4, 6]
print(l[1]) #1
print(len(l)) #4
l[2] = 10 #[2, 3, 10, 6]
del l[0] #[3, 10, 6]
print(l[-1]) #6
print(l[-2]) #10

print("------------------------")

fajlnave = "index.txt"
f = open(fajlnave, "r") #read
sorok = f.readlines()
f.close

print(sorok)

for i in range(len(sorok)):
    sorok[i] = sorok[i].strip()
print(sorok[0])

sum = int(sorok[1]) + int(sorok[2])
print(sum)

print("------------------------")

l1 = [2, 3, 4]
l2 = l1 #[2, 3, 4]
l2[1] = 10 #[2, 10, 4]
print(l1) #[2, 10, 4]

print("------------------------")

l1 = [2, 3, 4]
l2 = l1[:] #[2, 3, 4]
l2[1] = 10 #[2, 10, 4]
print(l1) #[2, 3, 4]

print("------------------------")

l1 = [2, 3, 4, 6, 12, 28]
print(l1[1:3]) #3, 4
print(l1[4:]) #12, 28
print(l1[:2]) #2, 3
print(l1[::3]) #2, 6
print(l1[1:5:2]) #3, 6
#keresés
print(3 in l1) #True
print(120 in l1) #False
print(120 not in l1) #True

print("------------------------")

#hatvány
for i in range(10):
    l.append(i**2) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(l)

l = [i ** 2 for i in range(10)]
print(l) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("------------------------")

l = [[2, 3, 3, 4],
    [3, 4, 5, 8], 
    [3, 4, 5, 10, 6]]

for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])