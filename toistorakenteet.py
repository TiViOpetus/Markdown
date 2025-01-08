# TOISTORAKENTEET
# ===============

# WHILE-SILMUKAT
# --------------

# Ikuinen silmukka
while True:
    print('Pyörin ikuisesti')
    poistu = input('Haluantko jatkaa? K/e ')
    if poistu == 'e':
        break # Poistutaan silmukasta

# Kierrosmääräinen silmukka
laskuri = 0
while laskuri < 10:
    print('Nyt on menossa kierros', laskuri)
    laskuri += 1 # Tai laskuri = laskuri + 1

# FOR-SILMUKAT
# ------------

# Rakentteellisen muuttujan arvojen läpikäynti
lista = ['Jonne', 'Tuittu', 'Jakke', 'Calle']
for jasen in lista:
    print(jasen, 'kuuluu listaan')

# Kierrosmääräinen silmukka

teksti = ''
for laskuri in range(30):
    teksti += 'X'
    print(teksti)

# Range-komento mahdollistaa alun, lopun ja askeleet

for parilliset_kymmenet in range(20,100,20):
    print(parilliset_kymmenet)