import random
from Clean import clean_it

list_docteurs = [ ]
def enreg_docteur(nom, pnom, prenom, tel, special):
        horaire = "Disponible"
        docteur = [ ]
        docteur.append(nom)
        docteur.append(pnom)
        docteur.append(prenom)
        docteur.append(tel)
        if len(list_patients) > 0:
            for i in range (len(list_docteurs)):
                num_mat = random.randint(10000000, 100000000)
                while num_mat == list_docteurs[i][4]:
                    num_mat = random.randint(10000000, 100000000)
        else:
            num_mat = random.randint(10000000, 100000000)
        num_mat = str(num_mat)
        matricule = "DCT"+num_mat[1:]
        docteur.append(matricule)
        docteur.append(special)
        docteur.append(horaire)
        docteur.append(horaire)
        docteur.append(horaire)
        docteur.append(horaire)
        docteur.append(horaire)
        docteur.append(horaire)
        list_docteurs.append(docteur)
        return clean_it()

list_patients = [ ]
def enreg_patient(nom, pnom, prenom, tel, poids, taille, genre, age):
        patient = [ ]
        patient.append(nom)
        patient.append(pnom)
        patient.append(prenom)
        patient.append(tel)
        try:
            while poids <= 0:
                clean_it()
                poids = float(input("Poids invalide! Veuillez réessayer:"))
            patient.append(poids)
        except ValueError:
                return clean_it()
        try:
            while taille <= 0:
                clean_it()
                taille = float(input("Taille invalide! Veuillez réessayer:"))
            patient.append(taille)
        except ValueError:
                return clean_it()
        while genre.lower() != "masc" and genre.lower() != "fem":
            clean_it()
            genre = input("Le genre entré est invalide! Veuillez entrer \"Masc\" ou \"Fem\" svp:")
        patient.append(genre)
        try:
            while age < 0 or age > 150:
                clean_it()
                age = int(input("Age incorrect! Veuillez réessayer:"))
            patient.append(age)
        except ValueError:
                return clean_it()
        if len(list_patients) > 0:
            for i in range (len(list_patients)):
                num_dossier = random.randint(10000000, 100000000)
                while num_dossier == list_patients[i][8]:
                    num_dossier = random.randint(10000000, 100000000)
        else:
            num_dossier = random.randint(10000000, 100000000)
        patient.append(num_dossier)
        list_patients.append(patient)
        return clean_it()

def chercher_nom_patient(nom, pnom, prenom):
    if len(list_patients) > 0:
        noms_patients = [ ]
        for i in range(len(list_patients)):
            noms = list_patients[i][0]+list_patients[i][1]+list_patients[i][2]
            noms_patients.append(noms.lower())
        nouveau_nom = nom+pnom+prenom
        resultats = [ ]
        for i in range(len(list_patients)):
            if nouveau_nom.lower() == noms_patients[i]:
                resultats.append(list_patients[i])
        if resultats != [ ]:
            clean_it()
            for i in range(len(resultats)):
                print(" Nom: ", resultats[i][0], \
                      "\n Post-nom: ", resultats[i][1], \
                      "\n Prénom: ", resultats[i][2], \
                      "\n Telephonne: ", resultats[i][3], \
                      "\n Poids: ", resultats[i][4], " Kg", \
                      "\n Taille: ", resultats[i][5], " m.", \
                      "\n Genre: ", resultats[i][6]+".", \
                      "\n Age: ", resultats[i][7], " ans", \
                      "\n Dossier n° ", resultats[i][8], "\n")
        else:
            return clean_it()
    else:
        return clean_it()
        
def chercher_num_dossier(dossier):
    if len(list_patients) > 0:
        clean_it()
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                    print(" Nom: ", list_patients[i][0], \
                      "\n Post-nom: ", list_patients[i][1], \
                      "\n Prénom: ", list_patients[i][2], \
                      "\n Telephonne: ", list_patients[i][3], \
                      "\n Poids: ", list_patients[i][4], " Kg", \
                      "\n Taille: ", list_patients[i][5], " m.", \
                      "\n Genre: ", list_patients[i][6]+".", \
                      "\n Age: ", list_patients[i][7], " ans", \
                      "\n Dossier n° ", list_patients[i][8], "\n")
    else:
        return clean_it()

def aff_patients():
    if len(list_patients) > 0:
        for i in range(len(list_patients)):
            print (" Nom: ", list_patients[i][0], \
                      "\n Post-nom: ", list_patients[i][1], \
                      "\n Prénom: ", list_patients[i][2], \
                      "\n Telephonne: ", list_patients[i][3], \
                      "\n Poids: ", list_patients[i][4], " Kg", \
                      "\n Taille: ", list_patients[i][5], " m.", \
                      "\n Genre: ", list_patients[i][6]+".", \
                      "\n Age: ", list_patients[i][7], " ans", \
                   "\n Dossier n° ", list_patients[i][8], "\n")
    else:
        return clean_it()

def aff_docteurs():
    if len(list_docteurs) > 0:
        for i in range(len(list_docteurs)):
            print (" Nom: ", list_docteurs[i][0], \
                      "\n Post-nom: ", list_docteurs[i][1], \
                      "\n Prénom: ", list_docteurs[i][2], \
                      "\n Telephonne: ", list_docteurs[i][3], \
                      "\n Numero matricule: ", list_docteurs[i][4], \
                      "\n Specialisation: ", list_docteurs[i][5], "\n")
    else:
        return clean_it()

def enreg_plainte(dossier, plainte):
    if len(list_patients) > 0:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                list_patients[i].append(plainte)
                return clean_it()
    else:
        return clean_it()
            
def enreg_horaire(matricule, dossier):
    if len(list_docteurs) > 0 and len(list_patients) > 0:
        cle = -1
        for i in range(len(list_docteurs)):
            if matricule == list_docteurs[i][4]:
                cle = i
        cle2 = -1
        for i in range(len(list_patients)):
             if dossier == list_patients[i][8]:
                cle2 = i
        if cle != -1 and cle2 != -1 and len(list_patients[cle2]) > 9:
            clean_it()
            for i in range(9, len(list_patients[cle2])):
                print ("Plainte ",i-8, ": ", list_patients[cle2][i])
            try:
                c1 = int(input("Entrez le numero d'une plainte à ajouter"))
                while c1 >= len(list_patients[cle2])-8 or c1 <= 0:
                    c1 = int(input("Numero invalide! Entrez le numero d'une plainte à ajouter"))
            except ValueError:
                return clean_it()
            clean_it()
            c2 = input("Tapez en toute lettre un jour de la semaine (du lundi au samedi) auquel sera attachée la plainte:")
            while c2.lower() != "lundi" and c2.lower() != "mardi" and c2.lower() != "mercredi" and c2.lower() != "jeudi" and c2.lower() != "vendredi" and c2.lower() != "samedi":
                clean_it()
                c2 = input("Erreur! Veuillez réesayer svp (entre lundi et samedi uniquement! exemple: mercredi)")
            jour = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
            for i in range(len(jour)):
                if c2.lower() == jour[i]:
                    if list_docteurs[cle][6+i] == "Disponible":
                        list_docteurs[cle][6+i] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                        return clean_it()
                    else:
                        clean_it()
                        c3 = input("Le docteur "+list_docteurs[cle][2]+" "+ list_docteurs[cle][0]+ " n'est pas disponible "+jour[i]+". Voulez-vous ecraser l'ancien programme?")
                        while c3.lower() != "oui" and c3.lower() != "non":
                            clean_it()
                            c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                        if c3.lower() == "oui":
                            list_docteurs[cle][6+i] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                            return clean_it()
                        else:
                            return clean_it()
        else:
            return clean_it()
    else:
        return clean_it()

def disponibilite_medecin(matricule):
    if len(list_docteurs) > 0:
        cle = -1
        for i in range(len(list_docteurs)):
            if matricule == list_docteurs[i][4]:
                cle = i
        if cle != -1:
            clean_it()
            jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
            for i in range(len(jours)):
                print(jours[i],": ", list_docteurs[cle][i+6])
            ch = input("Tapez 1 pour ajouter un rendez-vous, ou 0 pour retourner au menu principal:")
            while ch != "1" and ch != "0":
                clean_it()
                ch = input("Veuillez taper 1(ajouter rendez-vous) ou 0(quitter) svp")
            if ch == "1":
                try:
                    clean_it()
                    enreg_horaire(matricule, int(input("Entrez le numero du dossier du patient à prendre en charge:")))
                except ValueError:
                    return clean_it()
            else:
                return clean_it()
        else:
            return clean_it()
    else:
        return clean_it()

def aff_plaintes(dossier):
    if len(list_patients) > 0:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                cle = i
        if cle != -1 and len(list_patients[cle]) > 9:
                clean_it()
                for i in range(9, len(list_patients[cle])):
                    print ("Plainte ",i-8, ": ", list_patients[cle][i])
        else:
            return clean_it()
    else:
        return clean_it()
                    
def afficher_IMC(dossier):
    if len(list_patients) >= 0:
        clean_it()
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                imc = list_patients[i][4]/list_patients[i][5]
                if imc < 18.5:
                    print(list_patients[i][2], list_patients[i][0], ": Insuffisance pondérale (maigreur)")
                elif imc >= 18.5 and imc < 25:
                    print(list_patients[i][2], list_patients[i][0], ": Corpulence normale")
                elif imc >= 25 and imc < 30:
                    print(list_patients[i][2], list_patients[i][0], ": Surpoids")
                elif imc >= 30 and imc < 35:
                    print(list_patients[i][2], list_patients[i][0], ": Obésité modérée")
                elif imc >= 35 and imc < 40:
                    print(list_patients[i][2], list_patients[i][0], ": Obésité sévère")
                else:
                    print(list_patients[i][2], list_patients[i][0], ": Obésité morbide ou massive")
    else:
        return clean_it()
                    
