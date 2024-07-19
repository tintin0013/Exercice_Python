
###   Définissez ci-dessous une classe Fraction dont les attibuts sont : num et den, des entiers représentants le numérateur et le dénominateur.
###   Le dénominateur sera nécessairement un entier strictement positif, sans quoi le constructeur de cette classe devra lever une erreur (à l'aide d'un "assert").
###   Puis créez une méthode spéciale **str (self) qui permettra d'obtenir 'numerateur/denominateur' ou seulement 'numerateur' si le dénominateur vaut 1, en tapant print(F)** où F est une instance de la classe Fraction .

###   Tapez ci-dessous le code permettant de créer les instances F1, F2, F3 et F4 qui représentent les fractions 3/4 , -8/1 , 2/3 et 21/28. Puis faites afficher ces instances à l'aide de la méthode spéciale **str (self)** créée juste avant.


class InvalidDenominatorError(Exception):
    pass

class Fraction():
    def __init__(self, num, den):
        # assert den > 0, "Dénominateur doit être strictement positif"
        # self.num = num
        # self.den = den
         match den:
            case 0:
                raise InvalidDenominatorError("Le dénominateur ne peut pas être zéro.")
            case _ if den < 0:
                raise InvalidDenominatorError("Le dénominateur doit être strictement positif.")
            case _:
                self.num = num
                self.den = den

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            result = self.num/self.den
            return f"{self.num}/{self.den} = {result}" 


print()
F = Fraction(8, 2)   
F1 = Fraction(3, 4)
F2 = Fraction(-8, 1)
F3 = Fraction(2, 3)
F4 = Fraction(21, 28)
print(f"F = {F}") 
print()
print(f"F1 = {F1}")
print()
print(f"F2 = {F2}")
print()
print(f"F3 = {F3}")
print()
print(f"F4 = {F4}")
print()

# Tentative de création d'une fraction avec un dénominateur non positif
try:
    F5 = Fraction(17, 0)
    print(F5)
except InvalidDenominatorError as e:
    print(f"Erreur: {e}")

try:
    F6 = Fraction(13, -3)
    print(F6)
except InvalidDenominatorError as e:
    print(f"Erreur: {e}")

       


