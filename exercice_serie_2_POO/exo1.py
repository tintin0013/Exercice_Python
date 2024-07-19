
### 1.  Définissez ci-dessous une classe Etudiant dont les attibuts sont: nom, prenom, note_nsi, note_maths et note_phy.
###     Puis créez une méthode spéciale **str (self) qui permettra d'afficher 'NOM Prenom a obtenu note_nsi en NSI, note_maths en Mathématiques et note_phy en Physique' en tapant print(E) où E est une instance de la classe Etudiant

### 2. Tapez ci-dessous le code permettant de créer les instances E1, E2, E3 et E4 qui représentent:
###    - l'étudiant SARR Junior qui a eu 18 en NSI, 18 en Maths et 15 en Physique,
###    - l'étudiant FUSIL Morgan qui a eu 17 en NSI, 15 en Maths et 16 en Physique, 
###    - l'étudiant BEYA Noa qui a eu 14 en NSI, 19 en Maths et 18 en Physique et 
###    - l'étudiant BONNET Anne qui a eu 5 en NSI, 7 en Maths et 9 en Physique.
###    Puis faites afficher ces instances à l'aide de la méthode spéciale **str (self)** créée juste avant.


class Etudiant():
    def __init__(self, nom, prenom, note_nsi, note_maths, note_phy):
        self.nom = nom
        self.prenom = prenom
        self.note_nsi = note_nsi
        self.note_maths = note_maths
        self.note_phy = note_phy


    def __str__(self):
        return f"- {self.nom.upper()} {self.prenom} -  a obtenu {self.note_nsi} en NSI, {self.note_maths} en Mathématiques et {self.note_phy} en Physique"
    
E = Etudiant("Tournesol", "Tryphon", 19, 17, 18)
print()
print(E)  
E1 = Etudiant("HADDOCK", "Archibald", 18, 18, 15)
E2 = Etudiant("CASTAFIORE", "Bianca", 17, 15, 16)
E3 = Etudiant("RASTAPOPOULOS", "Roberto", 14, 19, 18)
E4 = Etudiant("WOLFF", "Frank", 5, 7, 9)
print() 
print(E1)
print() 
print(E2)
print() 
print(E3)
print() 
print(E4)
print()