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

def stringSzetszedoToIntList(szoveg: str, separator = " ", e_e_n_k = 0, v_e_n_k = 0, adat_szep = None):
    egysor = szoveg.split(separator)
    if adat_szep is not None:
        egysor = egysor[e_e_n_k:len(egysor)-v_e_n_k][0].split(adat_szep)
    szamok = str_int(egysor)
    return szamok