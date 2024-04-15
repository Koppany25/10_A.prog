'''import sys

filename = sys.argv[1]

f = open(filename)
sorok = f.readlines()
f.close()'''

print("------------------------")

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nevek = ["Szandi", "Sári", "Laci"]

def MaxKivKedd(matrix, oszlop):
    oszlop = 1
    maxert = matrix[0][oszlop]
    maxsor = 0
    for i in range(1, len(matrix)):
        if maxert < matrix[i][oszlop]:
            maxert = matrix[i][oszlop]
            maxsor = i

print("------------------------")

def SorOsszeg(lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]
    return s

def MaxSorosszeg(mx):
    maxertek = SorOsszeg(mx[0])
    maxindex = 0
    for i in range(1, len(mx)):
        if maxertek < SorOsszeg(mx[i]):
            maxertek = SorOsszeg(mx[i])
            maxindex = i
    return maxindex, maxertek

'''index, max = MaxSorosszeg(l)
print(f"{nevek[index]}")
    ennyit készített a heten: max'''