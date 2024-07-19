
### 6.  Écriture d’une fonction fabrique (factory) renvoyant une instance de classe.
###     Définir une classe CasNormal contenant une méthode uneMethode qui affiche "normal".
###     Définir une classe CasSpecial contenant une méthode uneMethode qui affiche "spécial".
###     Enfin définir la fonction fabrique (factory) casQuiConvient avec un paramètre estNormal iniatialisé par défaut à True.
###     Si le paramètre est vérifié, le corps de la fonction renvoie une instance de la classe CasNormal, sinon il renvoie une instance de la classe CasSpecial. 
###     Dans le programme principal, créez l’instance que vous désirez grâce à la fabrique (factory), puis vérifiez son type en appelant dessus la méthode uneMethode.



# Declaration de la classe CasNormal.
class CasNormal:
    def uneMethode(self):
        print("normal")

# Declaration de la classe CasSpecial. 
class CasSpecial:
    def uneMethode(self):
        print("spécial")

# Declaration de la fonction factory 'cas_qui_convient'.
def cas_qui_convient(estNormal=True):
    if estNormal:
        #print("Le cas est normal")
        return CasNormal()
    else:
        #print("Le cas est spécial")
        return CasSpecial()        

# Création d'une instance de CasNormal
cas1 = cas_qui_convient(estNormal = 1) # True = 1
print(type(cas1))  # Affiche <class '__main__.CasNormal'>
cas1.uneMethode()  # Affiche "normal"

# Création d'une instance de CasSpecial
cas2 = cas_qui_convient(estNormal = 0) # False = 0
print(type(cas2))  # Affiche <class '__main__.CasSpecial'>
cas2.uneMethode()  # Affiche "spécial"