
import readchar
from readchar import readkey, key
import os
import json
import csv
from colorama import Back, Fore, Style, deinit, init
from random import randint
import random

def initialiser_grille():
    tailleGrillei = random.randint(9, 19)

    tailleGrillej = random.randint(19, 39)
    GrilleJoueur = [[(Back.BLACK + " " + Style.RESET_ALL)] * (tailleGrillej) for _ in range(tailleGrillei)]
    positionJoueur = [random.randint(0,tailleGrillei-1), random.randint(0,tailleGrillej-1)]
    GrilleJoueur[positionJoueur[0]][positionJoueur[1]] = (Fore.RED + "▲" + Style.RESET_ALL) #on place le joueur
    GrilleV1 = [[" "] * tailleGrillej for _ in range(tailleGrillei)]
    GrilleV1[positionJoueur[0]][positionJoueur[1]] =  (Fore.RED + "▲" + Style.RESET_ALL) #on place le joueur
    tailleSituation = int(0.025*tailleGrillej*tailleGrillei)
    tailleMur = int(0.1*tailleGrillej*tailleGrillei)
    for i in range(tailleSituation): #positifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == " ":
                GrilleV1[chiffreX][chiffreY] = "P"
                break
    for i in range(tailleSituation): #negatifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == " ":
                GrilleV1[chiffreX][chiffreY] = "N"
                break
    for i in range(tailleMur): #negatifs
        while True:
            chiffreX = random.randint(0,tailleGrillei-1)
            chiffreY = random.randint(0,tailleGrillej-1)
            if GrilleV1[chiffreX][chiffreY] == " ":
                GrilleV1[chiffreX][chiffreY] = "M"
                break
    while True:
        chiffreX = random.randint(0, tailleGrillei-1)
        chiffreY = random.randint(0, tailleGrillej-1)
        if GrilleV1[chiffreX][chiffreY] == " ":
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
    print("2. Continuer une partie")
    print("3. Voir les règles")
    print("4. Tableau des scores")
    print("5. Quitter")


def afficher_regles():
    print("Règles du jeu :")
    # Ajouter ici les règles du jeu
    input("Appuyez sur Entrée pour revenir au menu principal...")


def afficher_jeu():

    print("Save the Fish!")
    grilleJ, GrilleAdmin, posJoueur, tailleI, tailleJ = initialiser_grille()
    afficher_grille(grilleJ)
    print("Score actuel : 0")
    return grilleJ, GrilleAdmin, posJoueur, tailleI, tailleJ


def handle_player_movement(player_position, orientation, grilleAdminF, grilleJoueurF, tailleIF, tailleJF, IsSituation, debogageF):
    key_pressed = input("choix i,j,k,l")
    print(key_pressed)
    IsMur = False
    OnSituationPos = False
    OnSituationNeg = False
    SortieF = False
    Quit = False
    RelancerF = False
    if key_pressed == orientation:
        # déplacement
        if key_pressed == "i" and player_position[0] > 0 :
            if grilleAdminF[player_position[0] - 1][player_position[1]] == "M":
                IsMur = True
            else:
                if grilleAdminF[player_position[0]-1][player_position[1]] == "P":#distinction in et on
                    OnSituationPos = True
                    
                elif grilleAdminF[player_position[0]-1][player_position[1]] == "N":
                    OnSituationNeg = True
                    
                player_position = [player_position[0] - 1, player_position[1]]
                if grilleAdminF[player_position[0]][player_position[1]] == "S":
                    SortieF = True
                grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "▲")
                grilleJoueurF[player_position[0] + 1][player_position[1]] = (Back.WHITE+" "+Style.RESET_ALL)
                grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "▲")
                grilleAdminF[player_position[0] + 1][player_position[1]] = " "
                if player_position[0] != 0:
                    if grilleAdminF[player_position[0]-1][player_position[1]] == "P" or grilleAdminF[player_position[0]-1][player_position[1]] == "N":
                        IsSituation = True
                    else:
                        IsSituation = False
                else:
                    IsSituation = False
        elif key_pressed == "j" and player_position[1] > 0:
            if grilleAdminF[player_position[0]][player_position[1] - 1] == "M":
                IsMur = True
            else:
                if grilleAdminF[player_position[0]][player_position[1]-1] == "P":  # distinction in et on
                    OnSituationPos = True
                    
                elif grilleAdminF[player_position[0]][player_position[1]-1] == "N":
                    OnSituationNeg = True
                    
                player_position = [player_position[0], player_position[1] - 1]
                if grilleAdminF[player_position[0]][player_position[1]] == "S":
                    SortieF = True
                grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "◄")
                grilleJoueurF[player_position[0]][player_position[1] + 1] = (Back.WHITE+" "+Style.RESET_ALL)
                grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "◄")
                grilleAdminF[player_position[0]][player_position[1] + 1] = " "
                if player_position[1] != 0:
                    if grilleAdminF[player_position[0]][player_position[1]-1] == "P" or grilleAdminF[player_position[0]][player_position[1]-1] == "N":
                        IsSituation = True
                    else:
                        IsSituation = False
                else:
                    IsSituation = False

        elif key_pressed == "k" and player_position[0] < tailleIF:
            if grilleAdminF[player_position[0] + 1][player_position[1]] == "M":
                IsMur = True
            else:
                if grilleAdminF[player_position[0]+1][player_position[1]] == "P":  # distinction in et on
                    OnSituationPos = True
                    
                elif grilleAdminF[player_position[0]+1][player_position[1]] == "N":
                    OnSituationNeg = True
                    
                player_position = [player_position[0] + 1, player_position[1]]
                if grilleAdminF[player_position[0]][player_position[1]] == "S":
                    SortieF = True
                grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "▼")
                grilleJoueurF[player_position[0] - 1][player_position[1]] = (Back.WHITE+" "+Style.RESET_ALL)
                grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "▼")
                grilleAdminF[player_position[0] - 1][player_position[1]] = " "
                if player_position[0] != tailleIF:
                    if grilleAdminF[player_position[0]+1][player_position[1]] == "P" or grilleAdminF[player_position[0]+1][player_position[1]] == "N":
                        IsSituation = True
                    else:
                        IsSituation = False
                else:
                    IsSituation = False
        elif key_pressed == "l" and player_position[1] < tailleJF:
            if grilleAdminF[player_position[0]][player_position[1] + 1] == "M":
                IsMur = True
            else:
                if grilleAdminF[player_position[0]][player_position[1]+1] == "P":  # distinction in et on
                    OnSituationPos = True
                    
                elif grilleAdminF[player_position[0]][player_position[1]+1] == "N":
                    OnSituationNeg = True
                    
                player_position = [player_position[0], player_position[1] + 1]
                if grilleAdminF[player_position[0]][player_position[1]] == "S":
                    SortieF = True
                grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "►")
                grilleJoueurF[player_position[0]][player_position[1] - 1] = (Back.WHITE+" "+Style.RESET_ALL)
                grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "►")
                grilleAdminF[player_position[0]][player_position[1] - 1] = " "
                if player_position[1] != tailleJF:
                    if grilleAdminF[player_position[0]][player_position[1]+1] == "P" or grilleAdminF[player_position[0]][player_position[1]+1] == "N":
                        IsSituation = True
                    else:
                        IsSituation = False
                else:
                    IsSituation = False


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
                IsSituation = True
            else:
                IsSituation = False

        elif key_pressed == "k":
            grilleAdminF[player_position[0]][player_position[1]] = (Fore.RED + "▼")
            grilleJoueurF[player_position[0]][player_position[1]] = (Fore.RED + "▼")
            if grilleAdminF[player_position[0] + 1][player_position[1]] == "P" or grilleAdminF[player_position[0] + 1][
                player_position[1]] == "N":
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
    if IsSituation:
        grilleJoueurF[player_position[0]][player_position[1]] = (Back.GREEN + grilleJoueurF[player_position[0]][player_position[1]]+ Style.RESET_ALL)
        grilleAdminF[player_position[0]][player_position[1]] = (
                Back.GREEN + grilleAdminF[player_position[0]][player_position[1]] + Style.RESET_ALL)
    if key_pressed == "d" and debogageF == False:
        debogageF = True
    elif key_pressed == "d" and debogageF == True:
        debogageF = False
    if key_pressed == "q":
        Quit = True
    if key_pressed == "r":
        RelancerF = True
    return player_position, orientation, grilleJoueurF, grilleAdminF, IsSituation, IsMur, OnSituationPos, OnSituationNeg, debogageF, SortieF, Quit, RelancerF

#FONCTIONS STOCKAGE

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

def fonction_Sortie(nomF, ScoreF):
    row = [nomF, ScoreF]
    with open('Scores.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)
    with open('PartieEnCours.csv', 'w', newline='') as csv_file:
        pass

def fonction_afficher_scores():
    Scores = []
    with open('Scores.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            Scores.append(row)

def fonction_Quitter(GrilleA, GrilleJ, ScoreJ, pseudo, posJ, tailleI, tailleJ, HistBug):
    GrilleA[posJ[0]][posJ[1]] = "X"
    GrilleJ[posJ[0]][posJ[1]] = "X"
    with open('GrilleAdmin.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in GrilleA:
            writer.writerow(row)
    with open('GrilleJoueur.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in GrilleJ:
            writer.writerow(row)
    with open('PartieEnCours.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([pseudo, str(ScoreJ), str(posJ[0]), str(posJ[1]), str(tailleI), str(tailleJ), HistBug])

def continuerPartie():
    Grille_admin = []
    with open('GrilleAdmin.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            Grille_admin.append([item for item in row])

    Grille_joueur = []
    with open('GrilleJoueur.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            Grille_joueur.append([item for item in row])

    DonneesPartie = []
    with open('PartieEnCours.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            DonneesPartie.append(row)
    Grille_joueur[int(DonneesPartie[0][2])][int(DonneesPartie[0][3])] = (Fore.RED + "▲")
    Grille_admin[int(DonneesPartie[0][2])][int(DonneesPartie[0][3])] = (Fore.RED + "▲")
    return Grille_joueur, Grille_admin, [int(DonneesPartie[0][2]),int(DonneesPartie[0][3])],int(DonneesPartie[0][4]), int(DonneesPartie[0][5]), DonneesPartie[0][0],int(DonneesPartie[0][1]),DonneesPartie[0][6]

def SelectionChoix():
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")
        if choix == "1":
            grilleJ2, GrilleAdmin2, posJoueur2, tailleI1, tailleJ1 = afficher_jeu()
            return grilleJ2, GrilleAdmin2, posJoueur2, tailleI1, tailleJ1,"", 0, False, False
        elif choix == "2":
            GrilleJ2, GrilleAdmin2, posJoueur2, tailleI1, tailleJ1, nom2, Score2, HistBool = continuerPartie()
            if HistBool == "True":
                HistBool = True
            else:
                HistBool = False
            return GrilleJ2, GrilleAdmin2, posJoueur2, tailleI1, tailleJ1, nom2, Score2, HistBool,False
        elif choix == "3":
            afficher_regles()
        elif choix == "4":
            pass
        elif choix == "5":
            return [0][0], [0][0], [0][0], 0, 0, "", 0, False, True
        else:
            print("Choix invalide. Veuillez réessayer.")

def fonctionPrincipale():

    while True:
        afficher_accueil()
        grilleJoueurG, GrilleAdminG, posJoueurG, tailleIG, tailleJG,nom,Score,HistDebogage, BoolQuitter = SelectionChoix()
        if BoolQuitter:
            break
        if nom == "":
            nom = input(" entrez votre pseudo puis cliquez enter: ")
            Score = 0
        else:
            afficher_grille(grilleJoueurG)
            HistDebogage = False
        orientationG = "i" #par défaut orienté vers le haut
        SituationBool = False
        Debogage = False
        while True:
            print(posJoueurG)
            posJoueurG, orientationG, grilleJoueurG, GrilleAdminG,SituationBool, MurBool,OnSituationPosG,OnSituationNegG, Debogage, Sortie, Quitter, Relancer = handle_player_movement(posJoueurG, orientationG, GrilleAdminG, grilleJoueurG, tailleIG,tailleJG, SituationBool,Debogage)
            if Debogage:
                afficher_grille(GrilleAdminG)
                HistDebogage = True
            else:
                afficher_grille(grilleJoueurG)
            if SituationBool:
                print("en face d'une situation")
            if MurBool:
                print("attention un mur")
            print("Votre score est de: "+str(Score))
            pos, neg = fonction_open_csv()
            if OnSituationPosG:
                randomInt = randint(0, len(pos)-1)
                print("Situation positive: "+pos[randomInt][0])
                print("Contenu de la situation: "+ pos[randomInt][1])
                Score += int(pos[randomInt][2])
                print("points obtenus: "+ pos[randomInt][2])
                print("Score total: " + str(Score))
                input("tapez ok puis enter: ")
            elif OnSituationNegG:
                randomInt = randint(0, len(neg) - 1)
                print("Situation négative: " + neg[randomInt][0])
                print("Contenu de la situation: " + neg[randomInt][1])
                Score -= int(pos[randomInt][2])
                print("points perdus: " + neg[randomInt][2])
                print("Score total: " + str(Score))
                input("tapez ok puis enter: ")
            if Sortie:
                if HistDebogage:
                    Score = 0
                print("Bravo"+nom+ "pour cette partie, Votre score est de: " + str(Score) + " !!")
                #afficher resultat avec Histdebogage pris en compte
                fonction_Sortie(nom, Score)
                break
            if Quitter:
                fonction_Quitter(GrilleAdminG, grilleJoueurG, Score, nom, posJoueurG, tailleIG, tailleJG, HistDebogage)
                break
            if Relancer:
                grilleJoueurG, GrilleAdminG, posJoueurG, tailleIG, tailleJG = initialiser_grille()
                afficher_grille(grilleJoueurG)
                SituationBool = False
                Debogage = False
                HistDebogage = False
                Relancer = False
                Score = 0





fonctionPrincipale()