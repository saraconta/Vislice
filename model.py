#Izdelava modela
#Ustvarite datoteko model.py

#Definirajte konstante

#STEVILO_DOVOLJENIH_NAPAK z vrednostjo 10.
#PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA nastavljene na tri različne konstante, npr. '+', 'o', '-'.
#ZMAGA, PORAZ nastavljeni na dve različni konstanti, npr. 'W' in 'X'.
#====

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'Z'

#====
#Napišite nov razred Igra, ki vsebuje:

#Metodo __init__, ki nastavi vrednosti spremenljivk
#   -niz geslo [beseda, ki jo igralec poskuša uganiti]
#   -seznam crke [dosedanji poskusi igralca]
#====

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke[:]

#====
#Metodi napacne_crke in pravilne_crke, ki vrneta seznam pravilnih oz. napačnih ugibanj igralca.
#====

    def napacne_crke(crke):
       return [crka for crka in self.crke if crka not in self.geslo]
    
    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
#====
#Metodo stevilo_napak, ki izračuna koliko napačnih ugibov je igralec že naredil.
#====

    def stevilo_napak(self):
        return len(self.napacne_crke())

#====
#Metodi zmaga in poraz, ki preverita ali trenutno stanje določa zmago oz. poraz.
#====

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        #vse_crke = all(crka in self.crke for crka in self.geslo)
        return vse_crke and STEVILO_DOVOLJENIH_NAPAK >= self.stevilo_napak()
    
    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()
#====
#Metodo pravilni_del_gesla, ki vrne niz z že uganjenim delom gesla, tako da neznane črke zamenja s podčrtajem.
#====

    def pravilni_del_gesla(self):
        delni = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for crka in self.geslo:
            if crka.upper() in ugibanje:
                delni += crka + ' '
            else:
                delni += '_ '
        return delni.strip()
#====
#Metodo nepravilni_ugibi, ki vrne niz, ki vsebuje s presledkom ločene nepravilne ugibe igralca.
#====

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

#====
#Metodo ugibaj, ki sprejme črko, jo pretvori v veliko črko, in vrne primernega od PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA, ZMAGA, PORAZ.
#====

    def ugibaj(crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else: 
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
#====
#V datoteki napišite kodo, ki iz datoteke besede.txt izlušči nabor besed in ga shrani v seznam bazen_besed.
#====

with open('besede.txt', 'r', encoding='utf-8') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]

#====
#Napišite funkcijo nova_igra, ki zgradi in vrne novo igro, ki ima za geslo naključno izbrano besedo iz seznama bazen_besed.

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


#testno_geslo = "DEŽUJE"
#testne_crke = ['A', 'E', 'I', 'O', 'U', 'D', 'J', 'K']
#igra = Igra(testno_geslo, testne_crke)
