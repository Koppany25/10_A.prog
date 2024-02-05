def beolvas(filename: str):
    """
    1.Egy filet megynit
    2.Sorait beleteszi egy listába
    3.Bezárja
    """
    file = open(filename)
    sorok = file.readlines()
    file.close()
    return sorok

def str_int(sorok: list[str], elsosor: int=0, a_vegerol_ennyi_sor_nem_kell: int=0):
    """
    1.Elem:
        -leveszi a felesleget
        -integerré alakít
    """
    szamok = []
    for i in range(elsosor, len(sorok)-a_vegerol_ennyi_sor_nem_kell):
        szamok.append(int(sorok[i].strip()))
    return szamok

def stringSzetszedoToIntList(szoveg: str, separator = " "):
    egysor = szoveg[0].split(separator)
    szamok = str_int(egysor)
    return szamok