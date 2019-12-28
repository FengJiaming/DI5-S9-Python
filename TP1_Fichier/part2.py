import datetime


# 3. a. Concevoir une classe Date
class Date(object):

    # Constructeur
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # surcharge de "=="
    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    # surcharge de "<"
    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False

    def toString(self):
        return self.day + "-" + self.month + "-" + self.year

# 3. b. Concevoir une class Etudiant
class Etudiant(object):

    # Constructeur
    def __init__(self, nom, prenom, birthday):
        self.prenom = prenom
        self.nom = nom
        self.birthday = birthday

    #Pour afficher l'objet
    def __repr__(self):
        return "Etudiant: {} {}\nDate de naissance: {}\nAge: {}\nE-Mail: {}\n"\
            .format(self.nom, self.prenom, self.birthday.toString(), self.calculerAge(), self.adresselec())

    # Pour fabriquer l'adresse électronique prenom.nom@etu.univ-tours.fr
    def adresselec(self):
        return self.prenom.lower() + "." + self.nom.lower() + "@etu.univ-tours.fr";

    # La méthode pour calculer l'âge
    def calculerAge(self):
        today = datetime.date.today()
        formatted_today = today.strftime('%Y')
        return int(formatted_today) - int(self.birthday.year)

    # getters et setters
    # birthday
    def _get_birthday(self):
        return self._birthday
    def _set_birthday(self, birthday):
        if not isinstance(birthday, Date):
            raise TypeError("Une Date est attendue")
        self._birthday = birthday
    birthday = property(_get_birthday, _set_birthday, "Date d'anniversaire de l'étudiant")

    # nom
    def _get_nom(self):
        return self._nom
    def _set_nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("Une chaine de caractère est attendue")
        self._nom = nom
    nom = property(_get_nom, _set_nom, "Nom de l'étudiant")

    # prenom
    def _get_prenom(self):
        return self._prenom
    def _set_prenom(self, prenom):
        if not isinstance(prenom, str):
            raise TypeError("Une chaine de caractère est attendue")
        self._prenom = prenom
    prenom = property(_get_prenom, _set_prenom, "Prenom de l'étudiant")

# 3. c. Lire le fichier fichetu.csv et constituer une liste d'objets Etudiant.
if __name__ == "__main__":
    try:
        list_etudiant = []

        with open("fichetu.csv", 'r') as fic:
            for line in fic.readlines():
                strStudent = line.strip()
                name = strStudent.split(';')
                birth = name[2].split('/')
                etudiant = Etudiant(name[0], name[1], Date(birth[0], birth[1], birth[2]))
                list_etudiant.append(etudiant)

        for etu in list_etudiant:
            print(etu)

    except Exception as exception_retournee:
        print("Voici l'erreur :", exception_retournee)

