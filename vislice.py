#Priprava spletnega vmesnika
#S strani knjižnice Bottle si prenesite datoteko bottle.py.

#S spletne učilnice si prenesite osnovno HTML predlogo ter slike. Predlogo premaknite v mapo views, slike pa v mapo img.

#V glavni mapi repozitorija ustvarite datoteko vislice.py, kjer:

##Uvozite modula bottle in model.
#====

import bottle

import model

SKRIVNOST = 'moja_skrivnost'

#====
#Definirate spremenljivko vislice, ki naredi objekt razreda Vislice.
#====

vislice = model.vislice(model.DATOTEKA_S_STANJEM, model.DATOTEKA_Z_BESEDAMI)

#====
#Z dekoratorjem bottle.get na naslov "/" pošljete predlogo index.tpl.
#====

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

#====
#Na dnu datoteke zaženete server z bottle.run(reloader=True, debug=True).
#====

#====
#Računalnik ni našel slik, zato mu pomagamo.
#====

@bottle.get('/img/<picture>')
def serve_picture(picture):
    return bottle.static_file(picture, root='img')

#====
#Po vzoru predloge index.tpl pripravite predlogo igra.tpl, ki bo pokazala vse podatke o izbrani igri igra z IDjem id_igre ter stanjem stanje:

#-Trenutno uganjeni del gesla
#-Nepravilne črke
#-Stopnjo obešenosti
#====

#====
#-V datoteki vislice.py definirajte:
#-Funkcijo nova_igra, ki ob zahtevi strani /igra/ prek metode GET sestavi novo igro, pridobi njen ID id_igre in naredi preusmeritev na naslov /igra/.../ (kjer ... zamenjamo z ustreznim IDjem nove igre)
#====

@bottle.post('/nova-igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra/')
 
#====
#-Funkcijo pokazi_igro, ki ob zahtevi strani /igra/<id_igre:int>/ prek metode GET naloži igro z IDjem id_igre in njeno trenutno stanje ter oboje prikaže s predlogo igra.tpl.
#====

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, stanje=stanje)

#====
#-Funkcijo ugibaj, ki ob zahtevi strani /igra/<id_igre:int>/ prek metode POST najprej naloži igro z danim IDjem, pridobi trenutno črko iz obrazca s poljem crka, nato naredi ugib s podano črko in naredi preusmeritev nazaj na isti naslov (tokrat prek metode GET).
#====

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')

#====
#Z uporabo % if, % elif in % else sintakse v predlogi igra.tpl prikažete ali je igralec zmagal oz. izgubil in mu ponudite gumb za začetek nove igre, sicer pa vnosno polje (z imenom crka) in gumb, s katerim igralec ugiba novo črko.
#====

#====
#DODATNO:
#Preprečite, da bi uporabnik lahko ugibal več kot eno črko naenkrat.
#====

#====
#Z dekoratorjem @bottle.get opremite naslov '/img/<picture>', ki uporablja funkcijo bottle.static_file za serviranje slik. Parameter root nastavite na 'img'. Nato stopnjo obešenosti v templatu igra.tpl prikažite preko slik.
#====

#====

bottle.run(reloader=True, debug=True)