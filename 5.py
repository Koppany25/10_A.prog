#x = input("x = ")
#input("y = ")

print("------------------------------------")

x = "ha"*3
print(x)

print("------------------------------------")

x = 3 == 2
x = 3 !=2

print("------------------------------------")

x = 2
if x ==2:
    print("x értéke 3")
elif x < 3:
    print("x kisebb mint 3")
else:
    print("x nem <= 3")

print("------------------------------------")

Sx = 5
feltetel = True
while feltetel:
    print("ciklusmag")
    if x == 7:
        feltetel = False
    x += 1
print(x)

i = 1
while not True:
    print("szeretem a puskast!", i)
    i += 1

print("------------------------------------")

'''while True:
    pass'''

print("------------------------------------")

for i in range(10):
    pass #0-9

for i in range(2,5):
    pass #2,3,5

for i in range(1,2,3):
    pass #2, 5, 8

print("------------------------------------")

#break "ciklus megszakítása"
#continue "folytatja a ciklust"

x = "szia"

for i in x:
    print(i)

'''x = 5
while x < 4:
    pass
else:
    print('nem lépett a ciklusba')

for l in range(12,10):
    print(l)
else:
    print('else ág:', l)'''

print("------------------------------------")

x = 3
y = 6
print(x > y)
print(not x > y)
print(not x <= y)

print(True and True)
print(True and False)
print(True and False and True)

print(True or False or False)

print( 1 and 0)
print(1 and 1)

print((1 and 1) and (1 and 0))

print((1 or 1) or (1 or 0))
print((1 or 0) or (0 or 0))

print((1 or 0) and (1 or 0))

a,b,c,d = 1,1,1,1
print((a or b) and (c or d))
print((a and b) or (c and d))

print(1 ^ 0)
print(1 ^ 1)

print(1 & 0)
print(3 & 2)
#3 = 11
#2 = 10
#eredmény = 10
print(3 | 2)
#eredmény = 11

print( ~5)
#5 = 101
#~5 = 010
print("------------------------------------")



print("------------------------------------")