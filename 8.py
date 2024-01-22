import math as m
"""def f(x: int,y: int):
    
        #f(x,y) = 3x+2y
    
    return 3*x+2*y

print(f(2,3))
print(f(3,2))

f(y=8, x=4)
print("wefuhde", end=" ")

def ki(x: any):
    print(x)
    return

x = print("szia")
print(x)

if (print("valami")) == None:
    print("None-al tért vissza")

x = ki("géza")
if x == None:
    print("Nem volt visszatérési érték")

print("-------------------------------------------------------")

def masodfok(a: float, b: float, c: float):
    
    #return -1: x = 0
    #return -2: d < 0
    #return int: 1 zérushely
    #returntuple: 2 zérushely
    
    if a == 0:
        return -1
    d = b**2-4*a*c
    if d < 0:
        return -2
    x1 = (-b + m.sqrt(d)) / (2*a)
    x2 = (-b - m.sqrt(d)) / (2*a)
    return x1, x2

x = masodfok(1, 3, 1)
if x == -1:
    print("Az  a érték 0 volt")
if x == -2:
    print("A diszkrimináns kisebb mint 0")
elif type(x) == type(tuple()):
    print("Két zérushelyünk van")
if type(x) == type(int()):
    print("Egy zérushelyünk van")

print("-------------------------------------------------------")

class A_NULLA(Exception):
    pass
class DISZKRIMINANS_KISEBB_NULLANAL:
    pass

def masodfok_h(a: float, b: float, c: float):
    
    #return x = 0: Hiba
    #return d < 0: Hiba
    #return int: 1 zérushely
    #returntuple: 2 zérushely
    
    if a == 0:
        raise A_NULLA
    d = b**2-4*a*c
    if d < 0:
        raise DISZKRIMINANS_KISEBB_NULLANAL
    x1 = (-b + m.sqrt(d)) / (2*a)
    x2 = (-b - m.sqrt(d)) / (2*a)
    return x1, x2

try:
    x = masodfok_h(0, 1, 2)
except A_NULLA:
    print("AZ 'a' értéle 0")
except DISZKRIMINANS_KISEBB_NULLANAL:
    print("A diszkrimináns kisebb nullánál")"""

print("-------------------------------------------------------")

def osszegzes(l: list):
    """
    összegzés prog tétel
    return elemek összege
    """
    s = 0
    for i in range(len(l)):
        s =+ l[i]
    return s

print(osszegzes[1,2,3,4])

print("-------------------------------------------------------")

def megszamlalas(l: list):
    """
    megszámlálás ptog tétel
    return darab
    """
    db = 0
    for i in range(len(l)):
        db =+ 1
    return db

print(megszamlalas[1,2,3,4])

print("-------------------------------------------------------")

def legnagyobb_ertek(l: list):
    """
    legnagyobb_érték ptog tétel
    return max
    """
    m = 0
    me = 0
    for i in range(len(l)):
        if l[i] > me:
            m = i
            me = l[i]
    return m,me

print(legnagyobb_ertek[1,2,3,4])

print("-------------------------------------------------------")

def kereses(l: list):
    """
    keresés ptog tétel
    return van, sorszám
    """
    v = False
    s = 0
    for i in range(len(l)):
        if :
            v = True
            s = i
    return v, s

print(kereses[1,2,3,4])

print("-------------------------------------------------------")

def eldontes(l: list):
    """
    eldöntés ptog tétel
    return 
    """
    
    for i in range(len(l)):
        if :
    return 

print(eldontes[1,2,3,4])

print("-------------------------------------------------------")

def kivalasztas(l: list):
    """
    kiválasztás ptog tétel
    return 
    """
    
    for i in range(len(l)):
        if :
    return 

print(kivalasztas[1,2,3,4])

print("-------------------------------------------------------")























