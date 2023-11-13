
'''def fejlec(cim):
    szelesseg = 30
    csillagok = "*"*szelesseg
    kozepso_cs = "*"*int(szelesseg - len(cim)/2)
    cuz = " "
    print(csillagok)
    print(kozepso_cs+cuz+cim+cuz+kozepso_cs)
    print(csillagok)

prog_neve = "Programcíme"
fejlec(prog_neve)

teszt=" "
for i in range(2,20):
    teszt += "c"
    fejlec(teszt)'''

x = 11_123_321
print(x+1)

#8-as számrendszer
print(0o123)
#hexa
print(0xABBA)
#bi
print(0b11000000)

print("------------------------------")

x = int("345", 36) #tetszőleges számrendszer
print(x)

x = oct(321) #vált 8-asba
print(x)

x = hex(40096) #vált 6-osba
print(x)

x = bin(192) #vált 2-esbe
print(x)

print("------------------------------------")

print(1/100000000) #1e 08

print("------------------------------------")

str = 'Any azt mondta hogy: "Érj haza időben!"'
print(str)

'''str = "Any azt mondta hogy: \"Érj haza időben!""
print(str)'''

print("------------------------------------")

x = 6/4 #1.5
y = 6//4 #1
ys = 6//-4 #-2
z = 6%4 #2
zs = 2**5 #32

print(9 % 6 % 2) #1

print("------------------------------------")

def abba():
         print("dgjdgj")

abba = 60
print(abba())