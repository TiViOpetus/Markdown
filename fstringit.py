# MUUTTUJAT MERKKIJONOSSA
# =======================

# Sanakirjat
henkilo1 = {'etunimi': 'Tiina', 'ika': 27}
henkilo2 = {'etunimi': 'Jaana', 'ika': 44}
henkilo3 = {'etunimi': 'Iida', 'ika': 7}

# Perinteinen ratkaisu
print(henkilo1['etunimi']+'n', 'ikä on', henkilo1['ika'], 'vuotta')

# Sama muotoiltuna merkkijonona (fstring)

muotoiltu_merkkijono = f'{henkilo1["etunimi"]}n ikä on {henkilo1["ika"]} vuotta'
print(muotoiltu_merkkijono)