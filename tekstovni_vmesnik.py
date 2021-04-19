#Izdelava tekstovnega vmesnika
#Ustvarite datoteko tekstovni_vmesnik.py.
#====

import model
PONOVNI_ZAGON = 'p'
IZHOD = 'i'

#====
#Napišite funkcije izpis_igre, izpis_zmage, izpis_poraza, ki sprejme igro in glede na stanje vrne niz, ki bi ga želeli izpisati. (Pozor, niza še ne izpišejo!)
#====

def izpis_igre(igra):
    tekst =f"""#################################\n
    {igra.pravilni_del_gesla()}\n
    Število poskusov: {1 + model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}\n 
    Nepravilne črke: {igra.nepravilni_ugibi()}
#################################\n"""
    return tekst

def izpis_zmage(igra):
    tekst = f"""#################################\n
    Bravo! Zmagali ste!\n
    Uganili ste geslo: {igra.pravilni_del_gesla()}\n 
    #################################\n"""
    return tekst


def izpis_poraza(igra):
    tekst = f"""#################################\n
    Porabili ste vse poskuse.\n
    Pravilno geslo: {igra.geslo}\n 
    #################################\n"""
    return tekst

#====
#Napišite funkcijo zahtevaj_vnos, ki od uporabnika zahteva, da poskuša uganiti črko, in vrne črko.
#====

def zahtevaj_vnos():
    return input('Vnesite črko:')

def zahtevaj_moznost():
    return input('Vnesite možnosti')

def ponudi_moznosti():
    tekst = f""" Vpišite črko za izbor naslednjih možnosti:\n
    {PONOVNI_ZAGON}: ponovni zagon igre\n
    {IZHOD}: izhod\n
    """
    return tekst

def izberi_ponovitev():
    print(ponudi_moznosti())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == PONOVNI_ZAGON:
        igra = model.nova_igra()
        print(izpis_igre(igra))
        return igra
    else:
        return IZHOD

#====
#Napišite funkcijo pozeni_vmesnik, ki zgradi novo igro, ter nato v neskončni zanki čaka na ugibanja igralca, ter sproti posodablja igro in izpisuje trenutno stanje. Ko se igra konča, izpiše primeren izpis in prekine zanko.
#====

def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        if odziv == model.ZMAGA:
            print (izpis_zmage(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        elif odziv == model.PORAZ:
            print(izpis_poraza(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        else:
            print(izpis_igre(igra))

#====
#Vmesnik lahko dodatno nadgradite:
#   -Vmesnik naj preverja, ali je igralčev vnos smiseln in ga v nasprotnem primeru opozori.
#   -Ko je igra zaključena, naj vmesnik igralcu ponudi ponoven zagon igre.
#   -Vmesnik naj namesto točk izrisuje stanje na vislicah.
#          _____
#          |   |
#          |   o
#          |  /|\
#          |  / \
#         _|______ 
#
#====

pozeni_vmesnik()