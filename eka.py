# Se ihan ensimmäinen hei maailma -esimerkki

print('Hello World')

print('Ja tämän sovelluksen koodasi Jakke Jäynä')

# ESIMERKKEJÄ MUUTTUJIEN KÄYTÖSTÄ
# ===============================

# YKSINKERTAISET MUUTTUJAT
# ------------------------


etunimi = 'Jonne' # Merkkijono string (str)
ika = 16 # Kokonaisluku integer (int)
ytoaineiden_keskiarvo = 2.5 # Liukuluku floating point number (float)
valmistunut = False # Totuusarvo boolean (bool)
print(etunimi, 'sai keskiarvoksi YTO-aineista', ytoaineiden_keskiarvo)
print(etunimi, 'on valmistunut', valmistunut )

# RAKENTELLISET MUUTTUJAT
# -----------------------

nimilista = ['Jonne', 'Jasmiina', 'Aleksanteri'] # Lista list
print('Listassa ensimmäisenä on', nimilista[0]) # Indeksissä 0 oleva arvo
jasenia = len(nimilista) # Listan jäsenmäär selviää len-komennolla
print('nimilistassa on', jasenia, 'henkilöä')
nimilista.sort() # Järjestää listan aakkosjärjetykseen
print('Aakkostettu lista on ', nimilista)

ryhmat = ('TiVi24A', 'TiVi23B', 'TiVi20oa') # Monikko tuple
print('Meidän ryhmä on', ryhmat[2]) 
# ryhmat[2] = 'Tivi20ka' # Yksittäistä jäsentä ei voi muuttaa
ryhmat = ('TiVi24A', 'TiVi23B', 'TiVi20ka') # Koko monikon voi muuttaa
print('Meidän uusi ryhmä on', ryhmat[2]) 

joukko = {'Tuittu', 'Assi', 'Calle'} # Joukko set
print('Ja joukkoon kuuluvat', joukko) # Huomaa järjestys
# print(joukko[2]) ei toimi, koska jäseneen ei voi viitata indeksillä 

# Sanakirja dictionary (dict)
henkilotiedot = {'etunimi': 'Jonne', 'sukunimi': 'Janttari', 'ika': 16}

print('Opiskelijan', henkilotiedot['etunimi'], 'ikä on', henkilotiedot['ika'])

opiskelija1 = {'etunimi': 'Jonne', 'sukunimi': 'Janttari', 'ika': 16}
opiskelija2 = {'etunimi': 'Iina', 'sukunimi': 'Urpo', 'ika': 17}
opiskelija3 = {'etunimi': 'Tuittu', 'sukunimi': 'Kiukkunen', 'ika': 27}

# Lista sanakirjoista -> Taulukko
opiskelijalista = [opiskelija1, opiskelija2, opiskelija3]
print('Opiskelijalista on', opiskelijalista)

uusi_opiskelija = {'etunimi': 'Assi', 'sukunimi': 'Kalma', 'ika': 65}

# Lisätään uusi arvo olemassa olevaan listaan
opiskelijalista.append(uusi_opiskelija)

# Tulostetaan opiskelijalistan ensimmäinen ja viimeinen jäsen
print('Listassa ensimmäisenä on', opiskelijalista.pop(0))
print('Ja viimeisenaä on', opiskelijalista.pop())