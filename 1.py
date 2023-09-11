nemjo = True
while nemjo:
    szam_str = input("adj meg egy számot: ")
    if szam_str.isdecimal():
        nemjo = False
        szam = int(szam_str)

if szam < 3:
    print("x kissebb mint 3")
elif szam > 3:
    print("x nagyobb mint 3")
else:
    print("x egynelő 3")