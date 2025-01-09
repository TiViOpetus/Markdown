# FUNKTIOT
# ========

# Funktio, joka ei palauta arvoa eikä käytä argumentteja

def tervehdys():
    """Prints Hyvää huomenta on the screen
    """
    print('Hyvää huomenta!')

tervehdys()

def toivotus(nimi, aika):
    """Greets user differently according to the time of day

    Args:
        nimi (str): user's name
        aika (int): hour in military format
    """
    if aika > 16:
        viesti = f'Hyvää iltaa {nimi}!'
    elif aika > 10:
        viesti = f'Hyvää päivää {nimi}!'
    else:
        viesti = f'Hyvää huomenta {nimi}!'

    print(viesti)

toivotus('Mika', 9)

alkuLitania = 'Milloin minä olisn työt tehnyt?'

def tyoMotivaatio(paiva: str) -> str:
    """Returns the motto of day in Finnish

    Args:
        paiva (str): Weekday name in Finnish

    Returns:
        str: The motto of the day
    """
    mottoDictionary = {'maanantai': 'na en malttanut',
             'tiistai': 'na en tietänyt',
             'keskiviikko': 'na en kerennyt',
             'torstai': 'na en tohtinut',
             'perjantai': 'on paha päivä',
             'lauantai': 'on pyhän aatto',
             'sunnuntai': 'suuri juhla'}
    
    dailyMotto = f'{alkuLitania} {paiva.capitalize()}{mottoDictionary[paiva]}.'
    return dailyMotto

print(tyoMotivaatio('torstai'))  


