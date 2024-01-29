def osszegzes(l: list, func):
    """
    összegzés prog tétel
    return elemek összege
    """
    s = l[0]
    for i in range(1, len(l)):
        s =func(s, l[i])
    return s

osszead = lambda num1, num2: num1+num2
osszeszor = lambda num1, num2: num1*num2

print(osszegzes[1,2,3,4], osszead)
print(osszegzes[1,2,3,4], osszeszor)

print("-------------------------------------------------------")

def megszamlalas(l: list, t):
    """
    megszámlálás prog tétel
    return darab
    """
    c = 0
    for i in range(len(l)):
        if t(l[i]):
            c += 1
    return c

par = lambda num: num%2==0

print(megszamlalas[1,2,3,4], par)

print("-------------------------------------------------------")

def legkisebb_ertek(l: list, t):
    """
    legkisebb_érték prog tétel
    return min
    """
    m = 0
    me = l[0]
    for i in range(len(l)):
        if t(l[i], me):
            m = i
            me = l[i]
    return m,me

kisebb = lambda num1, num2: num1 < num2

print(legkisebb_ertek[1,2,3,4], kisebb)

print("-------------------------------------------------------")

osszead = lambda num1, num2: num1+num2
print(osszead(2,3))

print("-------------------------------------------------------")

banner = lambda szoveg: print(30*"*"+"\n"+(30-len(szoveg))//2*"*"+"\n"+30*"*")
banner("Szia")
banner("Aha")

print("-------------------------------------------------------")

lista = [2,3,7,6,4,3,2,9]

otnel = lambda num: num < 5

c = 0
for i in range(len(lista)):
    if otnel(lista[i]):
        c += 1
print(c)



























































































































