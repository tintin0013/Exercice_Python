### 4.  Définir une classe Point avec un constructeur fournissant les coordonnées par défaut d’un point du plan (par exemple : x = 0.0 et y = 0.0). 
###     Définir une classe Segment dont le constructeur possède quatre paramètres : deux pour l’origine et deux pour l’extrémité. Ce constructeur définit deux attributs : orig et extrem, instances de la classe Point.
###     De cette manière, vous concevez une classe composite : La classe Segment est composée de deux instances de la classe Point. Ajouter une méthode d’affichage.
###     Enfin écrire un auto-test qui affiche une instance de Segment initialisée par les valeurs1, 2, 3 et4. 


# Declaration de la classe Point.
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    # Méthode d'affichage des points
    def afficher(self):
        print(f"Point(x={self.x}, y={self.y})") 


# Declaration de la classe Segment.
class Segment:
    def __init__(self, x1=0.0, y1=0.0, x2=1.0, y2=1.0):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)

    # Méthode d'affichage des segments.
    def afficher(self):
        print("Segment Origine:")
        self.orig.afficher()
        print("Segment Extrémité:")
        self.extrem.afficher()                 


# Programme principal 
# Instanciation d'un Segment.
segment = Segment(1.0, 2.0, 3.0, 4.0)

# Affichage du Segment.
print("\nAffichage d'une instance de Segment :")
segment.afficher()      

# Creation et Affichage auto-test.
auto_test_segment = Segment(1, 2, 3, 4)
print("\nAuto-test - Affichage d'une instance de Segment :")
auto_test_segment.afficher()