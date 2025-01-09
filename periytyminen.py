# PERIYTYMINEN INHERITANCE
# ========================

# KIRJASTOT JA MODUULIT
# ---------------------
# import oliot # Tuodaan koko oliot.py moduulin sisältö
import datetime
from oliot import Student # Tuodaan oliot moduulista Student-luokka 

# YLILUOKKA ELI ÄITILUOKKA (SUPER / PARENT CLASS)
# -----------------------------------------------
class Person():
    """Common class for all person in Raseko"""

    def __init__(self, etunimi: str, sukunimi: str):
        """Creates a Person object

        Args:
            etunimi (str): A first name
            sukunimi (str): A last name
        """
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    # Staattinen metodi, joka laskee iän. Staattisessa metodissa ei luoda oliota lainkaan
    # vaan metodia voi käyttää suoraan luokasta käsin
    @staticmethod
    def calculateAge(birthday) -> float:
        """Calculates student's current age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(birthday)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)
    
    # Luokkametodi on myös staattinen, eli ei vaadi olion muodostamista
    # Huomaa luokkaan viittaava cls, joka korvaa perinteisen self:n
    @classmethod
    def calculateAge2(cls, birthday):
        """Calculates student's current age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(birthday)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)
       
# ALILUOKKA ELI LAPSILUOKKA (SUB / CHILD CLASS)
# ---------------------------------------------
class RasekoStudent(Person):
    """The student class, inherits The Person class"""
    def __init__(self, etunimi: str, sukunimi: str, opiskelijanumero: str):
        """Creates a studen object

        Args:
            etunimi (str): Opiskelijan etunimi
            sukunimi (str): opiskelijan sukunimi
            opiskelijanumero (str): opiskelijanumero
        """
        super().__init__(etunimi, sukunimi) # Määritellään tapahtuvaksi yliluokan mukaan
        self.opiskelijanumero = opiskelijanumero # Ei määritelty yliluokassa

class RasekoTeacher(Person):
    """Creates a teacher inheriting the Person class

    Args:
        Person (class): Name of the super class
    """
    def __init__(self, etunimi: str, sukunimi:str, luokat: list[str]):
        """Constructo method for Teacher objects

        Args:
            etunimi (str): Teacher's given name
            sukunimi (str): Teacher's surname
            luokat (list[str]): List of student groups
        """
        super().__init__(etunimi, sukunimi)
        self.luokat = luokat

if __name__ == "__main__":
    rasekoStudent = RasekoStudent('Jonne', 'Janttari', '12345')
    print(rasekoStudent.sukunimi)

    luokat = ['TiVi23A', 'TiVi23B', 'TiVi20oa']
    rasekoTeacher = RasekoTeacher('Markku', 'Kynsijärvi', luokat)

    print(f'{rasekoTeacher.etunimi} opettaa ryhmiä {rasekoTeacher.luokat}')

    # Luodaan moduulista oliot.py Student-olio
    student = Student('Tuittu Kiukkunen', 'Auto22B','2007-10-23')
    print(f'{student.name} on {student.calculateAge()}')

    ika = Person.calculateAge('2008-03-22')
    print(ika)

    ika2 = Person.calculateAge2('1978-12-10')
    print(ika2)
    
