#Izdelava modela
#Ustvarite datoteko model.py

#Definirajte konstante

#STEVILO_DOVOLJENIH_NAPAK z vrednostjo 10.
#PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA nastavljene na tri različne konstante, npr. '+', 'o', '-'.
#ZMAGA, PORAZ nastavljeni na dve različni konstanti, npr. 'W' in 'X'.
#====
import json

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'P'

DATOTEKA_S_STANJEM = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'

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

    def napacne_crke(self):
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

    def ugibaj(self, crka):
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

with open(DATOTEKA_Z_BESEDAMI, 'r', encoding='utf-8') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]

#====
#Napišite funkcijo nova_igra, ki zgradi in vrne novo igro, ki ima za geslo naključno izbrano besedo iz seznama bazen_besed.
#====

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


#testno_geslo = "DEŽUJE"
#testne_crke = ['A', 'E', 'I', 'O', 'U', 'D', 'J', 'K']
#igra = Igra(testno_geslo, testne_crke)

#Spletni vmesnik za vislice
#Priprava modela
#Da bo naš strežnik lahko hkrati uporabljalo več igralcev, bomo naš model razširili s krovnim razredom Vislice, ki bo vseboval podatke o vseh igrah ter njihovem trenutnem stanju (rezultatu metode ugibaj). Igre bomo predstavili s slovarjem, katerega ključi bodo IDji iger, vrednosti pa pari, v katerih bo prva komponenta objekt razreda Igra, druga komponenta pa njeno zadnje stanje (PONOVLJENA_CRKA, PRAVILNA_CRKA, ZMAGA, …).

#V datoteki model.py definirajte konstanto ZACETEK, ki se razlikuje od prej definiranih konstant.
#====

ZACETEK = 'Z'

#====
#V datoteki model.py napišite nov razred Vislice, ki vsebuje:
#====

class vislice:

#====
#Metodo __init__, ki nastavi vrednost atributa igre na prazen slovar.
#====

    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_z_besedami = datoteka_z_besedami

#====
#Metodo prost_id_igre, ki vrne ID, ki še ni uporabljen v atributu igre.
#====

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

#====
#Metodo nova_igra, ki s pomočjo funkcije nova_igra s prejšnjih vaj sestavi novo igro z naključnim geslom. Par igre ter njenega začetnega stanja ZACETEK naj v slovar shrani pod še ne zasedenim ključem, ki naj ga metoda tudi vrne.
#====

    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id_igre

#====
#Metodo ugibaj, ki sprejme id_igre in črko ter na ustrezni igri požene metodo ugibaj (iz razreda Igra) in nato igro ter vrnjeno stanje zapiše nazaj v slovar.
#====

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra, _ = self.igre[id_igre]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)
        self.zapisi_igre_v_datoteko()


    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, encoding='utf-8') as f:
            igre = json.load(f)
            self.igre = {int(id_igre): (Igra(geslo, crke), stanje) for id_igre, (geslo, crke, stanje) in igre.items()}

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            igre = {id_igre: (igra.geslo, igra.crke, stanje) for id_igre, (igra, stanje) in self.igre.items()}
            json.dump(igre, f)
