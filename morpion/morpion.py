
def main():
    # Affiche le message de bienvenue
    print()
    print("* * Bienvenue Dans le JEU DU MORPION (Tic-tac-toe) * *")
    print()

    # Demande le nom des joueurs et les convertit en majuscules
    joueur1 = input("Entrez le nom du Joueur 1: ")
    joueur1 = joueur1.upper()
    print()
    joueur2 = input("Entrez le nom du Joueur 2: ")
    joueur2 = joueur2.upper()
    print()

    # Affiche quel joueur joue avec quel symbole
    print(f' -Bonjour {joueur1} vous joué avec la "X" \n\n -Bonjour {joueur2} vous joué avec la "O"')

    # Crée un dictionnaire pour associer les joueurs à leurs symboles
    joueur = {joueur1: "X", joueur2: "O"}
    symboles = {"X": joueur1, "O": joueur2}
    joueur_actuel = "X"  # X commence toujours

    compteur = 9  # Compteur de tours (il y a 9 cases)
    deja_jouer = []  # Liste pour suivre les cases déjà jouées
  
    # Initialise le plateau de jeu
    plateau = [["." for _ in range(3)] for _ in range(3)]

    # Fonction pour afficher le plateau de jeu
    def plateau_jeu():
        for i in range(3):
            for j in range(3):
                print(plateau[i][j], end=" ")
            print()
    print()

    # Fonction pour changer de joueur
    def change_joueur(joueur_actuel):
        return "O" if joueur_actuel == "X" else "X"
            
    # Fonction pour vérifier si le joueur actuel a gagné
    def verifier_victoire(plateau, joueur_actuel):
        # Vérifie les lignes et les colonnes
        for i in range(3):
            if all([plateau[i][j] == joueur_actuel for j in range(3)]) or all([plateau[j][i] == joueur_actuel for j in range(3)]):
                return True
        # Vérifie les diagonales
        if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur_actuel or plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur_actuel:
            return True
        return False         
        
    # Boucle principale du jeu
    while compteur > 0:
        plateau_jeu()
        print()
        choix = input(f"{symboles[joueur_actuel]} Choisissez une case de 1 à 9 ou tapez 'quit' pour quitter.")
        
        # Vérifie si le joueur veut quitter
        if choix.lower() in ['quit', 'exit']:
            print(" * * Partie terminée. * * ")
            return
        
        # Essaye de convertir le choix en un nombre entier
        try:
            choix = int(choix) - 1
        except ValueError:
            print("------------------------------------------------")
            print("!!! Veuillez entrer un nombre entier valide !!!")
            print("------------------------------------------------")
            continue
        
        # Calcule la ligne et la colonne à partir du choix
        col = choix % 3
        row = choix // 3

        # Vérifie si la case est déjà jouée
        if choix in deja_jouer:
            print()
            print("----------------------------------------")
            print(f"!!!!! ce chiffre a deja etait joué !!!!!")
            print("----------------------------------------")
            print()
        
        # Vérifie si le choix est en dehors des limites
        elif choix < 0 or choix > 8:
            print(" Veuillez entrer un nombre entre 1 et 9. ")
        
        # Joue le coup
        else:
            deja_jouer.append(choix)
            plateau[row][col] = joueur_actuel
            compteur -= 1

            # Vérifie si le joueur actuel a gagné
            if verifier_victoire(plateau, joueur_actuel):
                plateau_jeu()
                print("----------------------------------------------")
                print(f"* * * Félicitations {symboles[joueur_actuel]}, vous avez gagné! * * * ")
                print("----------------------------------------------")
                return
            
            # Change de joueur
            joueur_actuel = change_joueur(joueur_actuel)
    
    # Si aucun joueur n'a gagné, c'est un match nul
    plateau_jeu()
    print("Match NUL !!!")

# Appelle la fonction principale pour démarrer le jeu
main()



