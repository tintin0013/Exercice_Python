import random

# Liste de mots pour le jeu
liste_mots = ["java", "python", "javascript", "typescript", "angular", "react"]

# Permets de selectionner un mot aleatoirement dans la liste
mot_aleatoire = random.choice(liste_mots)

# Initialisation des variables du jeu
mot_cache = ["_" for _ in mot_aleatoire]
tentative = 10
lettre_joueur = []

# Boucle principale du jeu
while True:
    # Afficher l'état actuel du mot à deviner
    print("Mot à deviner : " + " ".join(mot_cache))
    print()
    print(f"Tentatives restantes : {tentative}")
    print()
    # Demander une lettre à l'utilisateur
    joueur_input = input("Entrez une lettre : ").lower()
    
    # Vérifier si la lettre a déjà été devinée
    if joueur_input in lettre_joueur:
        print("Cette lettre a déjà été trouvée, essayez une autre lettre.")
        print()
        continue
    
    lettre_joueur.append(joueur_input)
    
    # Mettre à jour le mot caché ou les tentatives restantes
    if joueur_input in mot_aleatoire:
        for index, letter in enumerate(mot_aleatoire):
            if letter == joueur_input:
                mot_cache[index] = joueur_input
        if "_" not in mot_cache:
            print("Mot à deviner : " + " ".join(mot_cache))
            print("BRAVO !!!  Vous avez Gagné !!!")
            break
    else:
        tentative -= 1
        if tentative == 0:
            print(f"PERDU. Vous avez utilisé toutes vos tentatives. Le mot était : {mot_aleatoire}")
            break