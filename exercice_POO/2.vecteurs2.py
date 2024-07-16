
### 1.  Définir une classe Vecteur2D avec un constructeur fournissant les coordonnées par défaut d’un vecteur du plan (par exemple : x = 0 et y = 0).
###     Dans le programme principal, instanciez un Vecteur2D sans paramètre, un Vecteur2D avec ses deux paramètres, et affichez-les. 

### 2.  Enrichissez la classe Vecteur2D précédente en lui ajoutant une méthode d’affichage et une méthode de surcharge d’addition de deux vecteurs du plan.
###     Dans le programme principal, instanciez deux Vecteur2D, affichez-les et affichez leur somme.


# Declaration de la classe Vecteur2D.
class Vecteur2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Méthode d'affichage du vecteur.
    def afficher(self, nom_variable):
        print(f"{nom_variable} : Vecteur2D(x={self.x}, y={self.y})")
 
    # Méthode d'addition de deux vecteurs.
    def ajouter(self, other):
        if isinstance(other, Vecteur2D):
            return Vecteur2D(self.x + other.x, self.y + other.y)
        raise TypeError("L'objet à ajouter doit être une instance de Vecteur2D")    


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

# Addition des vecteurs.
somme_vecteurs = vecteur1.ajouter(vecteur2)

# affichage de la somme des vecteurs.
somme_vecteurs.afficher("somme_vecteurs")  # somme_vecteurs : Vecteur2D(x=4, y=6)