# OPERAATTORIT JA VALINTARAKENTEET
# ================================

etunimi = 'Jonne'
ika = 16

# Oppivelvollinen, jos alle 18 v

if ika < 18:
    print('Opiskelija on oppivelvollinen')
else:
    print('Ei ole pakko tulla kouluun')

henkilo1 = {'etunimi': 'Tiina', 'ika': 27}
henkilo2 = {'etunimi': 'Jaana', 'ika': 44}
henkilo3 = {'etunimi': 'Iida', 'ika': 7}

# Henkilö lasketaan nuorisoon 13 - 30
ika = henkilo2['ika']
etunimi = henkilo2['etunimi']

if ika > 12 and ika < 30:
    print(etunimi, 'kuuluu nuorisoon')
elif ika < 13:
    print(etunimi, 'on lapsi')
else:
    print(etunimi, 'on aikuinen')

# Vaihtoehtoinen ratkaisu
if ika >= 30:
    print('Tervetuloa aikuiseksi', etunimi)
elif ika >= 13:
    print('Olet nuorisohuligaani', etunimi)
else:
    print('Olet pahainen kakara', etunimi)

# Paljon vaihtoehtoja sisältävä ehtorakenne

sisalto = {'Ohjelmointi': 'Kehitysmpäristö ja ohjelmointikielet', 'Ohjelmistokehittäjänä toimiminen': 'Projektityöskentely, tietovarastot, versiointi ja julkaisu', 'Komponenttikirjasto': 'Django, Node.js, Qt ja muut kirjastot', 'Sulautetut järjestelmät': 'C-ohjelmointi, Arduino ja Raspberry Pi'}

while True:
    kysymys = input('Minkä tutkinnon osan sisällön haluat nähdä? ')
    if kysymys == '':
        break
    try:
        vastaus = sisalto[kysymys]
    except Exception as e:
        vastaus = 'Ei semmoista tutkinnon osaa ole olemassa'

    print(vastaus)

