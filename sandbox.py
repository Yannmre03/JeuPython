
def handle_player_movement(player_position, orientation, grilleAdminF, grilleJoueurF, tailleIF,tailleJF):
    key_pressed = input("choix i,j,k,l")
    print(key_pressed)
    if key_pressed == orientation:
        #déplacement
        if key_pressed == "i":
            if grilleAdminF[player_position[0] - 1][player_position[1]] == "M":
                print("Attention un mur")
            else:
                player_position = [player_position[0] - 1, player_position[1]]
                grilleJoueurF[player_position[0]][player_position[1]] = "▲"
                grilleJoueurF[player_position[0] + 1][player_position[1]] = "X"
                grilleAdminF[player_position[0]][player_position[1]] = "▲"
                grilleAdminF[player_position[0] + 1][player_position[1]] = "X"

        elif key_pressed == "j":
            if grilleAdminF[player_position[0]][player_position[1] - 1] == "M":
                print("Attention un mur")
            else:
                player_position = [player_position[0], player_position[1] - 1]
                grilleJoueurF[player_position[0]][player_position[1]] = "◄"
                grilleJoueurF[player_position[0]][player_position[1] + 1] = "X"
                grilleAdminF[player_position[0]][player_position[1]] = "◄"
                grilleAdminF[player_position[0]][player_position[1] + 1] = "X"

        elif key_pressed == "k":
            if grilleAdminF[player_position[0] + 1][player_position[1]] == "M":
                print("Attention un mur")
            else:
                player_position = [player_position[0] + 1, player_position[1]]
                grilleJoueurF[player_position[0]][player_position[1]] = "▼"
                grilleJoueurF[player_position[0] - 1][player_position[1]] = "X"
                grilleAdminF[player_position[0]][player_position[1]] = "▼"
                grilleAdminF[player_position[0] - 1][player_position[1]] = "X"

        elif key_pressed == "l":
            if grilleAdminF[player_position[0]][player_position[1] + 1] == "M":
                print("Attention un mur")
            else:
                player_position = [player_position[0], player_position[1] + 1]
                grilleJoueurF[player_position[0]][player_position[1]] = "►"
                grilleJoueurF[player_position[0]][player_position[1] - 1] = "X"
                grilleAdminF[player_position[0]][player_position[1]] = "►"
                grilleAdminF[player_position[0]][player_position[1] - 1] = "X"
    #orientation
    else:
        if key_pressed == "i":
            grilleAdminF[player_position[0]][player_position[1]] = "▲"
            grilleJoueurF[player_position[0]][player_position[1]] = "▲"
            if grilleAdminF[player_position[0] - 1][player_position[1]] == "P" or grilleAdminF[player_position[0] - 1][
                player_position[1]] == "N":
                # change la couleur du joueur

                print("attention, vou etes en face d'une situation")

        elif key_pressed == "j":
            grilleAdminF[player_position[0]][player_position[1]] = "◄"
            grilleJoueurF[player_position[0]][player_position[1]] = "◄"
            if grilleAdminF[player_position[0]][player_position[1] - 1] == "P" or grilleAdminF[player_position[0]][
                player_position[1] - 1] == "N":
                # change la couleur du joueur
                print("attention, vou etes en face d'une situation")

        elif key_pressed == "k":
            grilleAdminF[player_position[0]][player_position[1]] = "▼"
            grilleJoueurF[player_position[0]][player_position[1]] = "▼"
            if grilleAdminF[player_position[0] + 1][player_position[1]] == "P" or grilleAdminF[player_position[0] + 1][
                player_position[1]] == "N":
                # change la couleur du joueur
                print("attention, vou etes en face d'une situation")

        elif key_pressed == "l":
            grilleAdminF[player_position[0]][player_position[1]] = "►"
            grilleJoueurF[player_position[0]][player_position[1]] = "►"
            if grilleAdminF[player_position[0]][player_position[1] + 1] == "P" or grilleAdminF[player_position[0]][
                player_position[1] + 1] == "N":
                # change la couleur du joueur
                print("attention, vou etes en face d'une situation")
    orientation = key_pressed
    return player_position, orientation, grilleJoueurF







def handle_player_movement(player_position, orientation, grilleAdminF, grilleJoueurF, tailleIF,tailleJF):
    key_pressed = input("choix i,j,k,l")
    print(key_pressed)
    orientationBis = ""


    if (key_pressed == "i" or key_pressed == "8") and orientation == "i" and player_position[0] > 0 :
        if grilleAdminF[player_position[0]-1][player_position[1]] == "M":
            print("Attention un mur")
        else:
            player_position = [player_position[0]-1, player_position[1]]
            grilleJoueurF[player_position[0]][player_position[1]] = "▲"
            grilleJoueurF[player_position[0]+1][player_position[1]] = "X"
            grilleAdminF[player_position[0]][player_position[1]] = "▲"
            grilleAdminF[player_position[0]+1][player_position[1]] = "X"

    elif (key_pressed == "j" or key_pressed == "4")and orientation == "j" and player_position[1] > 0:
        if grilleAdminF[player_position[0]][player_position[1]-1] == "M":
            print("Attention un mur")
        else:
            player_position = [player_position[0], player_position[1]-1]
            grilleJoueurF[player_position[0]][player_position[1]] = "◄"
            grilleJoueurF[player_position[0]][player_position[1]+1] = "X"
            grilleAdminF[player_position[0]][player_position[1]] = "◄"
            grilleAdminF[player_position[0]][player_position[1]+1] = "X"

    elif (key_pressed == "k" or key_pressed == "5" or key_pressed == "2") and orientation == "k" and player_position[0] < tailleIF:
        if grilleAdminF[player_position[0]+1][player_position[1]] == "M":
            print("Attention un mur")
        else:
            player_position = [player_position[0]+1, player_position[1]]
            grilleJoueurF[player_position[0]][player_position[1]] = "▼"
            grilleJoueurF[player_position[0] - 1][player_position[1]] = "X"
            grilleAdminF[player_position[0]][player_position[1]] = "▼"
            grilleAdminF[player_position[0]-1][player_position[1]] = "X"

    elif (key_pressed == "l" or key_pressed == "6") and orientation == "l" and player_position[0] < tailleJF:
        if grilleAdminF[player_position[0]][player_position[1]+1] == "M":
            print("Attention un mur")
        else:
            player_position = [player_position[0], player_position[1]+1]
            grilleJoueurF[player_position[0]][player_position[1]] = "►"
            grilleJoueurF[player_position[0]][player_position[1]-1] = "X"
            grilleAdminF[player_position[0]][player_position[1]] = "►"
            grilleAdminF[player_position[0]][player_position[1] - 1] = "X"
    elif key_pressed == "i":
        orientationBis = "i"
        grilleAdminF[player_position[0]][player_position[1]] = "▲"
        grilleJoueurF[player_position[0]][player_position[1]] = "▲"
        if grilleAdminF[player_position[0]-1][player_position[1]] == "P" or grilleAdminF[player_position[0]-1][player_position[1]] == "N" :
            #change la couleur du joueur

            print("attention, vou etes en face d'une situation")
    elif key_pressed == "j":
        orientationBis = "j"
        grilleAdminF[player_position[0]][player_position[1]] = "◄"
        grilleJoueurF[player_position[0]][player_position[1]] = "◄"
        if grilleAdminF[player_position[0]][player_position[1]-1] == "P" or grilleAdminF[player_position[0]][player_position[1]-1] == "N":
            # change la couleur du joueur
            print("attention, vou etes en face d'une situation")
    elif key_pressed == "k":
        orientationBis = "k"
        grilleAdminF[player_position[0]][player_position[1]] = "▼"
        grilleJoueurF[player_position[0]][player_position[1]] = "▼"
        if grilleAdminF[player_position[0]+1][player_position[1]] == "P" or grilleAdminF[player_position[0]+1][player_position[1]] == "N":
            # change la couleur du joueur
            print("attention, vou etes en face d'une situation")
    elif key_pressed == "l":
        orientationBis = "l"
        grilleAdminF[player_position[0]][player_position[1]] = "►"
        grilleJoueurF[player_position[0]][player_position[1]] = "►"
        if grilleAdminF[player_position[0]][player_position[1]+1] == "P" or grilleAdminF[player_position[0]][player_position[1]+1] == "N":
            # change la couleur du joueur
            print("attention, vou etes en face d'une situation")
    orientation = orientationBis
    return player_position, orientation, grilleJoueurF






