# PYTEST-TESTAUSFUNKTIOT
# ======================

# MODUULIEN JA KIRJASTOJEN LATAUKSET
# ----------------------------------

# Käyttöjärjestelmän virhelimoitusten testaus vaatii pytest:n lataamisen
import pytest # Jos et testaa virheilmoituksia, voi jättää pois

# Ladataa testattava moduuli
import periytyminen

# Luodaan testiolioita eri luokista testausta varten

person = periytyminen.Person('Assi', 'Kalma')

student = periytyminen.RasekoStudent('Jonne', 'Janttari', 45678)

teacher = periytyminen.RasekoTeacher('Mikko', 'Viljanen', ['TiVi20oa', 'TiVi20ka', 'Tivi22'])


# TESTAUSFUNKTIOT ELI YKSIKKÖTESTIT
# ---------------------------------

def test_person_properties():
    assert person.givenName == 'Assi'
    assert person.surName == 'Kalma'

def test_person_age3():
    assert round(person.calculteAge3('2008-12-31')) == 16

def test_student_properties():
    assert student.studentNumber == 45678
