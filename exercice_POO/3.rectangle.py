
### 3.  Définir une classe Rectangle avec un constructeur donnant des valeurs (longueur et largeur) par défaut et un attribut nom = "rectangle", une méthode d’affichage et une méthode surface renvoyant la surface d’une instance.
###     Définir une classe Carre héritant de Rectangle et qui surcharge l’attribut d’instance : nom = "carré". 
###     Dans le programme principal, instanciez un Rectangle et un Carre et affichez-les.


# Declaration de la classe Rectangle.
class Rectangle:
    def __init__(self, longueur=1, largeur=1):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"

    # Méthode d'affichage parametres du rectangle.
    def afficher(self):
        print(f"{self.nom} : longueur = {self.longueur}, largeur = {self.largeur}")  

    # Méthode de calcul de la surface.
    def surface(self):
        return self.longueur * self.largeur


# Declaration de la classe Carre avec appel a rectangle dans le constructeur.
# class Carre(Rectangle):
#     def __init__(self, cote=1):
#         Rectangle.__init__(self, longueur=cote, largeur=cote) 
#         self.nom = "carré"
    
# Declaration de la classe Carre avec utilisation de super() dans le constructeur.
class Carre(Rectangle):
    def __init__(self, cote=1):
        super().__init__(longueur=cote, largeur=cote)
        self.nom = "carré"    


# Programme principal
# Instanciation d'un Rectangle.
rect = Rectangle(4, 2)
rect.afficher()  # rectangle : longueur = 4, largeur = 2
print(f"Surface du {rect.nom} : {rect.surface()}")  # Surface du rectangle : 8

# Instanciation d'un Carre.
carre = Carre(3)
carre.afficher()  # carré : longueur = 3, largeur = 3
print(f"Surface du {carre.nom} : {carre.surface()}")  # Surface du carré : 9                     



