
# Exercice 1

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