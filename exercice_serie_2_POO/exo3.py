
# Exercice 3


class Carte:

    # Initialise une carte avec une valeur et un motif (1: Pique, 2: Coeur, 3: Carreau, 4: Trèfle)
    def __init__(self, valeur, motif):
        self.valeur = valeur
        self.motif = motif


    # Renvoie une représentation textuelle de la carte
    def __str__(self):
        motifs = {1: "Pique", 2: "Coeur", 3: "Carreau", 4: "Trèfle"} 
        valeurs = {11: "Valet", 12: "Dame", 13: "Roi", 14: "As"}
        valeur_str = valeurs.get(self.valeur, str(self.valeur))
        motif_str = motifs[self.motif]
        
        return f"{valeur_str} de {motif_str}"
    

    # Définir l'opérateur < pour comparer les valeurs des cartes
    def __lt__(self, autre):
        return self.valeur < autre.valeur


    # Définir l'opérateur == pour comparer les valeurs des cartes
    def __eq__(self, autre):
        return self.valeur == autre.valeur
    


class Paquet:

    # Initialise un paquet de cartes, vide par défaut
    def __init__(self, cartes=None):
        if cartes is None:
            self.cartes = []
        else:
            self.cartes = cartes


    # Renvoie une représentation textuelle du paquet de cartes
    def __str__(self):
        return ' ; '.join(str(carte) for carte in self.cartes)


    # Ajoute une carte au paquet
    def ajouter_carte(self, carte):
        self.cartes.append(carte)


    # Enlève une carte spécifique ou la première carte du paquet si aucune carte n'est spécifiée
    def enlever_carte(self, carte=None):
        if carte:
            if carte in self.cartes:
                self.cartes.remove(carte)
                return carte
            else:
                return None
        else: 
            if self.cartes:
                return self.cartes.pop(0)
            else:
                return None


    # Remet la première carte du paquet à la fin du paquet
    def repositionner_carte(self):
        if self.cartes:
            self.ajouter_carte(self.enlever_carte())


    # Renvoie le nombre de cartes dans le paquet
    def __len__(self):
        return len(self.cartes)
    


import random

# Crée un paquet complet de 52 cartes
def creer_paquet_jeu_complet():
    cartes = []
    for valeur in range(2, 15):  # 2 à 14 (14 pour l'As)
        for motif in range(1, 5):  # 1 à 4 pour les motifs
            cartes.append(Carte(valeur, motif))
    return Paquet(cartes)


# Mélange les cartes et distribue 8 cartes à chaque joueur
def distribuer_cartes(paquet_complet):
    paquet_complet.cartes = random.sample(paquet_complet.cartes, len(paquet_complet.cartes))
    return Paquet(paquet_complet.cartes[:8]), Paquet(paquet_complet.cartes[8:16])


# Fonction principale pour jouer un jeu de bataille
def jouer_bataille():
    paquet_complet = creer_paquet_jeu_complet()
    paquet_joueur, paquet_ordinateur = distribuer_cartes(paquet_complet)
    
    print("Début du jeu de bataille simplifié !")
    print()
    
    for i in range(8):  # Réduire à 8 tours pour correspondre aux 8 cartes par joueur
        carte_joueur = paquet_joueur.enlever_carte()
        carte_ordinateur = paquet_ordinateur.enlever_carte()
        
        if not carte_joueur or not carte_ordinateur: 
            break
        
        print(f"Tour {i+1}: - Joueur - {carte_joueur} / - Ordinateur - {carte_ordinateur}")
        print("----------------------------------------------------------------")
        print()

        if carte_joueur > carte_ordinateur:
            print(">>>  Joueur gagne ce tour  <<<")
            paquet_joueur.ajouter_carte(carte_joueur)
            paquet_joueur.ajouter_carte(carte_ordinateur)
        elif carte_joueur < carte_ordinateur:
            print("<<<  Ordinateur gagne ce tour  >>>")
            paquet_ordinateur.ajouter_carte(carte_joueur)
            paquet_ordinateur.ajouter_carte(carte_ordinateur)
        else:
            print("Égalité, les cartes sont remises à la fin du paquet.")
            paquet_joueur.ajouter_carte(carte_joueur)
            paquet_ordinateur.ajouter_carte(carte_ordinateur)
    
    print()
    print(f"Cartes restantes - Joueur: {len(paquet_joueur)} vs Ordinateur: {len(paquet_ordinateur)}")
    print()
    
    if len(paquet_joueur) > len(paquet_ordinateur):
        print(f"Le joueur gagne avec {len(paquet_joueur)} cartes contre {len(paquet_ordinateur)} cartes.")
    elif len(paquet_joueur) < len(paquet_ordinateur):
        print(f"L'ordinateur gagne avec {len(paquet_ordinateur)} cartes contre {len(paquet_joueur)} cartes.")
    else:
        print(f"Égalité parfaite avec {len(paquet_joueur)} cartes chacun.")

print()
print("****************************************************************")
print("*                                                              *")
print("*                       *** TEST ***                           *")
print("*                                                              *")
print("****************************************************************")
print()


################################################################
#                                                              #        
#                       *** TEST ***                           #
#                                                              #
################################################################

# Tests pour la méthode __str__ de la classe Carte        
def test_carte_str():
    assert str(Carte(2, 1)) == "2 de Pique"
    assert str(Carte(11, 2)) == "Valet de Coeur"
    assert str(Carte(14, 4)) == "As de Trèfle"
    print("Tous les tests pour la méthode __str__ de Carte sont passés avec succès.")
    

# Tests pour les comparaisons de cartes
def test_comparaison_cartes():
    c1 = Carte(6, 1)   # 6 de Pique
    c2 = Carte(13, 2)  # Roi de Coeur
    c3 = Carte(13, 3)  # Roi de Carreau
    assert (c1 == c2) == False
    assert (c2 == c3) == True
    assert (c1 < c2) == True
    assert (c3 < c1) == False
    assert (c3 < c2) == False
    print("Tous les tests de comparaison de cartes sont passés avec succès.")


# Tests pour la méthode __str__ de la classe Paquet
def test_paquet_str():
    c1 = Carte(6, 1)   # 6 de Pique
    c2 = Carte(13, 2)  # Roi de Coeur
    c3 = Carte(13, 3)  # Roi de Carreau
    assert str(Paquet([])) == ""
    assert str(Paquet([c1])) == "6 de Pique"    
    assert str(Paquet([c1, c2, c3])) == "6 de Pique ; Roi de Coeur ; Roi de Carreau"  
    print("Tous les tests pour la méthode __str__ de Paquet sont passés avec succès.")
    

# Tests pour les opérations de la classe Paquet    
def test_paquet_operations():
    c1 = Carte(6, 1)   # 6 de Pique
    c2 = Carte(13, 2)  # Roi de Coeur
    c3 = Carte(13, 3)  # Roi de Carreau
    p1 = Paquet([c1, c2, c3])  
    p1.enlever_carte(c1)
    assert str(p1) == "Roi de Coeur ; Roi de Carreau"
    print()
    print("Test 1: OK")
    print()

    p1.ajouter_carte(c1)
    assert str(p1) == "Roi de Coeur ; Roi de Carreau ; 6 de Pique"
    print("Test 2: OK")
    print()

    p1.repositionner_carte()
    assert str(p1) == "Roi de Carreau ; 6 de Pique ; Roi de Coeur"
    print("Test 3: OK")
    print()
    print("Tous les tests de la classe Paquet sont passés avec succès.")

   
# Lancement des tests pour les classes Carte et Paquet
test_carte_str()
print()
test_comparaison_cartes()
print()
test_paquet_str()
test_paquet_operations()
print()
print("****************************************************************")
print("****************************************************************") 
print()

################################################################
################################################################


# Appel de la fonction jouer_bataille pour lancer le jeu
jouer_bataille()