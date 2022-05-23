from Actions import *
from Clean import clean_it

def main():
    c = input(" 1 pour enregistrer un docteur \n 2 pour enregistrer un patient \n \
3 pour rechercher un ou plusieurs patient(s) a partir d'un nom \n \
4 pour atteindre un patient gràce à son numero du dossier \n \
5 pour afficher tous les patients enregistrés \n \
6 pour afficher tous les docteurs enregistrés \n \
7 pour enregistrer une plainte \n \
8 pour personnaliser l'horaire d'un medecin \n \
9 pour vérifier la disponibilité d'un medecin \n \
10 pour afficher la liste des plaintes d'un patient \n \
11 pour afficher l'IMC (indice de masse corporelle) \n \
et 0 pour quitter. \
\n\n  >>> Choisissez une action à faire: ")
    if c == "1":
        clean_it()
        enreg_docteur(input("Entrez le nom:"), input("Entrez le post-nom:"), \
        input("Entrez le prenom:"), input("Entrez le numero de téléphone:"), \
                      input("Entrez une specialisation:"))
        main()
    elif c == "2":
        clean_it()
        try:
            enreg_patient(input("Entrez le nom:"), input("Entrez le post-nom:"), \
            input("Entrez le prenom:"), input("Entrez le numero de téléphone:"), \
            float(input("Entrez le poids (Juste la valeur numerique en Kg):")), \
            float(input("Entrez la taille (Juste la valeur numerique en mettre):")), \
            input("Entrez le genre (Masc ou Fem):"),  int(input("Entrez l'age (Juste la valeur numerique):")))
        except ValueError:
             clean_it()
        main()
    elif c == "3":
        clean_it()
        chercher_nom_patient(input("Entrez le nom:"), input("Entrez le post-nom:"), \
        input("Entrez le prenom:"))
        main()
    elif c == "4":
        clean_it()
        try:
             chercher_num_dossier(int(input("Entrez le numero du dossier à atteindre:")))
        except ValueError:
             clean_it()
        main()
    elif c == "5":
        clean_it()
        aff_patients()
        main()
    elif c == "6":
        clean_it()
        aff_docteurs()
        main()
    elif c == "7":
        clean_it()
        try:
            enreg_plainte(int(input("Entrez le numero du dossier du patient:")), input("Entrez la nouvelle plainte:"))
        except ValueError:
             clean_it()
        main()
    elif c == "8":
        clean_it()
        try:
            enreg_horaire(input("Entrez le matricule du medecin"),\
            int(input("Entrez le numero du dossier du patient à prendre en charge:")))
        except ValueError:
             clean_it()
        main()
    elif c == "9":
        clean_it()
        disponibilite_medecin(input("Entrez le matricule du medecin"))
        main()
    elif c == "10":
        clean_it()
        try:
            aff_plaintes(int(input("Entrez le numero du dossier du patient:")))
        except ValueError:
             clean_it()
        main()
    elif c == "11":
        clean_it()
        try:
            afficher_IMC(int(input("Entrez le numero du dossier à atteindre:")))
        except ValueError:
             clean_it()
        main()
    elif c == "0":
        clean_it()
    else:
        clean_it()
        main()

main()
