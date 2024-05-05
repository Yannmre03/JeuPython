
import readchar
from readchar import readkey, key
import os
import json
import csv
from colorama import Back, Fore, Style, deinit, init
from random import randint
import random

#test2
#Fonction grille
def initialiser_grille():
    tailleGrillei = random.randint(9, 19)

    tailleGrillej = random.randint(19, 39)
    GrilleJoueur = [[(Back.BLACK + " " + Style.RESET_ALL)] * (tailleGrillej) for _ in range(tailleGrillei)]
    positionJoueur = [random.randint(0,tailleGrillei-1), random.randint(0,tailleGrillej-1)]
    GrilleJoueur[positionJoueur[0]][positionJoueur[1]] = (Fore.RED + "▲" + Style.RESET_ALL) #on place le joueur
    GrilleV1 = [[""] * tailleGrillej for _ in range(tailleGrillei)]
    GrilleV1[positionJoueur[0]][positionJoueur[1]] =  (Fore.RED + "▲" + Style.RESET_ALL) #on place le joueur
    tailleSituation = int(0.025*tailleGrillej*tailleGrillei)
    tailleMur = int(0.1*tailleGrillej*tailleGrillei)
    for i in range(tailleSituation): #positifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == "":
                GrilleV1[chiffreX][chiffreY] = "P"
                break
    for i in range(tailleSituation): #negatifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == "":
                GrilleV1[chiffreX][chiffreY] = "N"
                break
    for i in range(tailleMur): #negatifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == "":
                GrilleV1[chiffreX][chiffreY] = "M"
                break
    while True:
        chiffreX = random.randint(0, tailleGrillei-1)
        chiffreY = random.randint(0, tailleGrillej-1)
        if GrilleV1[chiffreX][chiffreY] == "":
            GrilleV1[chiffreX][chiffreY] = "S"
            break
    return GrilleJoueur, GrilleV1, positionJoueur, tailleGrillei-1, tailleGrillej-1


def afficher_grille(ma_grille):
    print((Fore.BLUE+"┌"+Style.RESET_ALL) + (Fore.BLUE+"───┬"+Style.RESET_ALL) * (len(ma_grille[0]) - 1) + (Fore.BLUE+"───┐"+Style.RESET_ALL))
    for i, ligne in enumerate(ma_grille):
        if i != 0:
            print((Fore.BLUE+"├"+ Style.RESET_ALL) + (Fore.BLUE+"───┼"+ Style.RESET_ALL) * (len(ligne) - 1) + (Fore.BLUE+"───┤"+Style.RESET_ALL))
        for valeur in ligne:
            print((Fore.BLUE+"│ "+Style.RESET_ALL) + valeur + " ", end="")

        print(Fore.BLUE+"│"+Style.RESET_ALL)
    print((Fore.BLUE+"└")+(Fore.BLUE+"───┴"+Style.RESET_ALL) * (len(ligne) - 1) + (Fore.BLUE+"───┘"+Style.RESET_ALL))

def afficher_accueil():
    print("Bienvenue dans le jeu !")
    print("Le jeu le plus amusant de tous les temps !")
    print("Créé par Ines et Albane en 2024")
    input("Appuyez sur Entrée pour continuer...")

def afficher_menu():
    print("Menu principal :")
    print("1. Jouer")
    print("2. Voir les règles")
    print("3. Quitter")
    choix = input("Entrez votre choix : ")
    return choix

def afficher_regles():
    print("Règles du jeu :")
    # Ajouter ici les règles du jeu
    input("Appuyez sur Entrée pour revenir au menu principal...")

def afficher_jeu():

    print("Save the Fish!")
    print("Légende des cases")
    print("Grille de jeu")
    grilleJ, GrilleAdmin, posJoueur, tailleI, tailleJ = initialiser_grille()
    afficher_grille(grilleJ)
    print("Score actuel : [score]")
    print("Indications pour le joueur")
    return grilleJ, GrilleAdmin, posJoueur, tailleI, tailleJ


def handle_player_movement(player_position, orientation, grilleAdminF, grilleJoueurF, tailleIF, tailleJF, IsSituation):
    key_pressed = input("choix i,j,k,l")
    print(key_pressed)
    IsMur = False
    OnSituationPos = False
    OnSituationNeg = False
    if key_pressed == orientation:
        # déplacement
        if key_pressed == "i" and player_position[0] > 0 :
            if grilleAdminF[player_position[0] - 1][player_position[1]] == "M":
                IsMur = True
            else:
                if grilleAdminF[player_position[0]-1][player_position[1]] == "S":#distinction in et on
                    OnSituationPos = True
                    print("situation jouée")
                elif grilleAdminF[player_position[0]-1][player_position[1]] == "N":
                    OnSituationNeg = True
                player_position = [player_position[0] - 1, player_position[1]]
                grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "▲")
                grilleJoueurF[player_position[0] + 1][player_position[1]] = " "
                grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "▲")
                grilleAdminF[player_position[0] + 1][player_position[1]] = " "

        elif key_pressed == "j" and player_position[1] > 0:
            if grilleAdminF[player_position[0]][player_position[1] - 1] == "M":
                IsMur = True
            else:
                if grilleAdminF[player_position[0]][player_position[1]-1] == "S":  # distinction in et on
                    OnSituationPos = True
                    print("situation jouée")
                elif grilleAdminF[player_position[0]][player_position[1]-1] == "N":
                    OnSituationNeg = True
                player_position = [player_position[0], player_position[1] - 1]
                grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "◄")
                grilleJoueurF[player_position[0]][player_position[1] + 1] = " "
                grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "◄")
                grilleAdminF[player_position[0]][player_position[1] + 1] = " "


        elif key_pressed == "k" and player_position[0] < tailleIF-1:
            if grilleAdminF[player_position[0] + 1][player_position[1]] == "M":
                IsMur = True
            else:
                if grilleAdminF[player_position[0]+1][player_position[1]] == "S":  # distinction in et on
                    OnSituationPos = True
                    print("situation jouée")
                elif grilleAdminF[player_position[0]+1][player_position[1]] == "N":
                    OnSituationNeg = True
                player_position = [player_position[0] + 1, player_position[1]]
                grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "▼")
                grilleJoueurF[player_position[0] - 1][player_position[1]] = " "
                grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "▼")
                grilleAdminF[player_position[0] - 1][player_position[1]] = " "


        elif key_pressed == "l" and player_position[1] < tailleJF:
            if grilleAdminF[player_position[0]][player_position[1] + 1] == "M":
                IsMur = True
            else:
                if grilleAdminF[player_position[0]][player_position[1]+1] == "S":  # distinction in et on
                    OnSituationPos = True
                    print("situation jouée")
                elif grilleAdminF[player_position[0]][player_position[1]+1] == "N":
                    OnSituationNeg = True
                player_position = [player_position[0], player_position[1] + 1]
                grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "►")
                grilleJoueurF[player_position[0]][player_position[1] - 1] = " "
                grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "►")
                grilleAdminF[player_position[0]][player_position[1] - 1] = " "

    # orientation
    else:
        if key_pressed == "i":
            grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "▲")
            grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "▲")
            if grilleAdminF[player_position[0] - 1][player_position[1]] == "P" or grilleAdminF[player_position[0] - 1][
                player_position[1]] == "N":
                # change la couleur du joueur

                IsSituation = True
            else:
                IsSituation = False

        elif key_pressed == "j":
            grilleAdminF[player_position[0]][player_position[1]] =(Fore.RED +"◄")
            grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED +"◄")
            if grilleAdminF[player_position[0]][player_position[1] - 1] == "P" or grilleAdminF[player_position[0]][
                player_position[1] - 1] == "N":
                # change la couleur du joueur
                IsSituation = True
            else:
                IsSituation = False

        elif key_pressed == "k":
            grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "▼")
            grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "▼")
            if grilleAdminF[player_position[0] + 1][player_position[1]] == "P" or grilleAdminF[player_position[0] + 1][
                player_position[1]] == "N":
                # change la couleur du joueur
                IsSituation = True
            else:
                IsSituation = False
        elif key_pressed == "l":
            grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "►")
            grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "►")
            if grilleAdminF[player_position[0]][player_position[1] + 1] == "P" or grilleAdminF[player_position[0]][
                player_position[1] + 1] == "N":
                # change la couleur du joueur
                IsSituation = True
            else:
                IsSituation = False
    orientation = key_pressed
    return player_position, orientation, grilleJoueurF, grilleAdminF, IsSituation, IsMur, OnSituationPos, OnSituationNeg
#FONCTIONS STOCKAGE

#fonctionOpenCSV: ouvrir un fichier csv et stocker son contenu
    #entrée: nom du fichier 'exemple.csv' (String)
    #sortie: variable avec le contenu (liste 1,2,3 ou ...n dimensions je crois dépendant du nombre de colonnes)
import csv

def fonction_open_csv():
    contenu  = []
    positive = []
    negative = []
    with open("Situations.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contenu.append(row)
        for i in range(len(contenu)):
            if contenu[i][0] == "Positive":
                positive.append(contenu[i][1:-1])
            if contenu[i][0] == "Negative":
                negative.append(contenu[i][1:-1])
    return positive, negative
## appel : contenu = fonction_open_csv('exemple.csv')

#fonctionOpenJSON: ouvrir un fichier json et stocker son contenu
    #entrée: nom du fichier 'exemple.json' (String)
    #sortie: variable avec le contenu (Dictionnaire)
import json

def fonction_open_json(nom_fichier):
    with open(nom_fichier, 'r') as json_file:
        contenu = json.load(json_file)
    return contenu
## appel : contenu = fonction_open_json('exemple.json')

#fonctionSaveCSV: stocke dans un fichier csv un contenu
    #entrées:
    # nom du fichier 'exemple.csv' (String)
    # variable avec contenu organisé à stocker (liste)
    #sortie: aucune (ou bool réussit ou non)



def fonction_save_csv(nom_fichier, contenu):
    try:
        with open(nom_fichier, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in contenu:
                writer.writerow(row)
        return True  # Succès de l'écriture dans le fichier
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False  # Échec de l'écriture dans le fichier

def fonction_save_json(nom_fichier, contenu):
    try:
        with open(nom_fichier, 'w') as json_file:
            json.dump(contenu, json_file, indent=4)
        return True  # Succès de l'écriture dans le fichier
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False  # Échec de l'écriture dans le fichier

def SelectionChoix(choix):
    while True:
        if choix == "1":
            grilleJ2, GrilleAdmin2, posJoueur2, tailleI1, tailleJ1 = afficher_jeu()
            return grilleJ2, GrilleAdmin2, posJoueur2, tailleI1, tailleJ1

        elif choix == "2":
            afficher_regles()
            break
        elif choix == "3":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def fonctionPrincipale():
    afficher_accueil()
    choixP =afficher_menu()
    grilleJoueurG, GrilleAdminG, posJoueurG, tailleIG, tailleJG = SelectionChoix(choixP)
    orientationG = "i" #par défaut orienté vers le haut
    SituationBool = False
    while True:
        print(posJoueurG)
        posJoueurG, orientationG, grilleJoueurG, GrilleAdminG,SituationBool, MurBool,OnSituationPosG,OnSituationNegG = handle_player_movement(posJoueurG, orientationG, GrilleAdminG, grilleJoueurG, tailleIG,tailleJG, SituationBool )
        afficher_grille(GrilleAdminG)
        if SituationBool:
            print("en face d'une situation")
        if MurBool:
            print("attention un mur")
        pos, neg = fonction_open_csv()
        if OnSituationPosG:
            randomInt = randint(0, len(pos)-1)
            print("Situation positive: "+pos[randomInt][0])
            print("Contenu de la situation: "+ pos[randomInt][1])
            print("points obtenus: "+ pos[randomInt][2])
            input("cliquez sur entrez: ")
        elif OnSituationNegG:
            randomInt = randint(0, len(neg) - 1)
            print("Situation négative: " + neg[randomInt][0])
            print("Contenu de la situation: " + neg[randomInt][1])
            print("points peruds: " + neg[randomInt][2])
            input("cliquez sur entrez: ")


fonctionPrincipale()