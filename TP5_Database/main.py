from TP5_Database.Database import *

# Réaliser le travail de TP
if __name__ == "__main__":
    try:
        # 1. Question 1: Créer une base de données
        print("Question 1 : Créer une base de données")
        db = Database()
        db.reset()
        print("La base de données créée avec succès!")
        db.extractCommunes("database/communes.csv")
        db.extractDepartements("database/departements.csv")
        db.extractRegions("database/regions.csv")
        print("Les données insérées avec succès!")


        # 2. Question 2: Les populations totales de chaque département et région
        print("Question 2 : Les populations totales de chaque département et région: ")
        db.computePopulation()

        # 3. Question 3: les communes ayant le même nom et un département différent
        print("Question 3 : Les communes ayant le même nom et un département différent: ")
        db.findDifferent()

        # 4. Question 4: database -> xml ; xml -> database
        print("Question 4.1 : Sauvegarder la base dans un fichier XML: ")
        db.saveXML("database.xml")
        print("Le fichier XML est créé")

        print("Question 4.2 : Charger la base à partir d'un fichier XML: ")
        db.chargeXML("database.xml")

        # 5. Question 5: NouvellesRegions
        print("Question 5: NouvellesRegions ")
        db.newRegion("database/zones-2016.csv","database/communes-2016.csv")
        db.computeNewPopulation()

    except Exception as exception_retournee:
        print("Voici l'erreur :", exception_retournee)

