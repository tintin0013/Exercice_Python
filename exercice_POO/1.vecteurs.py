
### 1.  Définir une classe Vecteur2D avec un constructeur fournissant les coordonnées par défaut d’un vecteur du plan (par exemple : x = 0 et y = 0).
###     Dans le programme principal, instanciez un Vecteur2D sans paramètre, un Vecteur2D avec ses deux paramètres, et affichez-les. 


# Declaration de la classe Vecteur2D.
class Vecteur2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Méthode d'affichage du vecteur.
    def afficher(self, nom_variable):
        print(f"{nom_variable} : Vecteur2D(x={self.x}, y={self.y})") 


## Programme principal 
        
# Instanciation sans paramètre.
vecteur_sans_parametre = Vecteur2D()
vecteur_sans_parametre.afficher("vecteur_sans_parametre")  # Vecteur2D(x=0, y=0)

# Instanciation avec des paramètres.
vecteur1 = Vecteur2D(1, 2)
vecteur2 = Vecteur2D(3, 4)

# Affichage des vecteurs.
vecteur1.afficher("vecteur1")  # vecteur1 : Vecteur2D(x=1, y=2)
vecteur2.afficher("vecteur2")  # vecteur2 : Vecteur2D(x=3, y=4) 

