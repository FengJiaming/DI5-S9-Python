#TP1_Fichier Fichier

#1. Afficher « Bonjour le monde ! »
print("Bonjour le monde!")

#2. En mode console, proposez un petit menu
import os

def func():
    choix = '0'
    filename = ''


    while choix != '9':
        print("1.Choisir un nom de fichier")
        print("2.Ajouter un texte")
        print("3.Afficher le fichier complet")
        print("4.Vider le fichier")
        print("9.Quitter le programme")

        choix = input("Votre choix:")

        # Choix 1.choisir un nom du fichier
        if choix == '1':
            for f in os.listdir(os.getcwd()):
                print(f)
            filename = input("Entrez un nom du fichier:")
            print("Vous avez choisi le fichier ", filename)

        # Choix 2.Ajouter un texte
        elif choix == '2':
            if not filename:
                print("Le nom du fichier est vide! Veuillez choisir un nom du fichier!")
            else:
                print("Nom du fichier: ", filename)
                if filename not in os.listdir(os.getcwd()):
                    print("Le fichier n'existe pas. On le crée.")
                with open(filename, "a") as fic:
                    texte = input("Entrez le texte:")
                    fic.write(texte)
                    fic.close()

        # Choix 3.Afficher le fichier complet
        elif choix == '3':
            if not filename:
                print("Le nom du fichier est vide! Veuillez choisir un nom du fichier!")
            else:
                print("Nom du fichier: ", filename)
                if filename in os.listdir(os.getcwd()):
                    with open(filename, "r") as fic:
                        print(fic.read())
                        fic.close()
                else:
                    print("Le fichier n'existe pas. On le crée.")
                    with open(filename, "x") as fic:
                        fic.close()

        # Choix 4.Vider le fichier
        elif choix == '4':
            if not filename:
                print("Le nom du fichier est vide! Veuillez choisir un nom du fichier!")
            else:
                print("Nom du fichier: ", filename)
                if filename in os.listdir(os.getcwd()):
                    with open(filename, "w+") as fic:
                        fic.truncate()
                        fic.close()
                else:
                    print("Le fichier n'existe pas. Vous ne pouvez pas le vider.")

if __name__ == "__main__":
    try:
        func()
    except Exception as exception_retournee:
        print("Voici l'erreur :", exception_retournee)

