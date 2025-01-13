# PERIYTYMINEN INHERITANCE
# ========================

# KIRJASTOT JA MODUULIT
# ---------------------
# import oliot # Tuodaan koko oliot.py moduulin sisältö
import datetime
import oliot # Tuodaan oliot moduulista Student-luokka 

# YLILUOKKA ELI ÄITILUOKKA (SUPER / PARENT CLASS)
# -----------------------------------------------
class Person():
    """Common class for all person in Raseko"""

    def __init__(self, givenName: str, surName: str):
        """Creates a Person object

        Args:
            givenName (str): A first name
            surName (str): A last name
        """
        self.givenName = givenName
        self.surName = surName

    def calculteAge3(self, isoBirthday: str) -> float:
        birthday = datetime.datetime.fromisoformat(isoBirthday)
        age = datetime.datetime.now() - birthday
        ageInYears = age.days / 365
        return ageInYears
    
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
    def __init__(self, givenName: str, surName: str, studentNumber: int):
        """Creates a studen object

        Args:
            givenName (str): Student's first name
            surName (str): Student's last name
            studenNumber (int): Student's ID
        """
        super().__init__(givenName, surName) # Määritellään tapahtuvaksi yliluokan mukaan
        self.studentNumber = studentNumber # Ei määritelty yliluokassa

class RasekoTeacher(Person):
    """Creates a teacher inheriting the Person class

    Args:
        Person (class): Name of the super class
    """
    def __init__(self, givenName: str, surName:str, groups: list[str]):
        """Constructo method for Teacher objects

        Args:
            givenName (str): Teacher's given name
            surName (str): Teacher's surname
            luokat (list[str]): List of student groups
        """
        super().__init__(givenName, surName)
        self.groups = groups

if __name__ == "__main__":
    rasekoStudent = RasekoStudent('Jonne', 'Janttari', '12345')
    print(rasekoStudent.givenName)

    groups = ['TiVi23A', 'TiVi23B', 'TiVi20oa']
    rasekoTeacher = RasekoTeacher('Markku', 'Kynsijärvi', groups)

    print(f'{rasekoTeacher.givenName} opettaa ryhmiä {rasekoTeacher.groups}')

    # Luodaan moduulista oliot.py Student-olio
    student = Student('Tuittu Kiukkunen', 'Auto22B','2007-10-23')
    print(f'{student.name} on {student.calculateAge()}')

    ika = Person.calculateAge('2008-03-22')
    print(ika)

    ika2 = Person.calculateAge2('1978-12-10')
    print(ika2)

    person1 = Person('Calle', 'Keckelberg')
    ika3 = person1.calculteAge3('2009-10-22')
    print(f'Henkilön {person1.givenName} ikä on {ika3} vuotta')
    
