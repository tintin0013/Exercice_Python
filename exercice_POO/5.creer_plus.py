
### 5.  Définir une fonction fabrique 'creer_plus' renvoyant une fonction fermeture 'plus'.
###     cree_plus a un argument ajout. Son code ne renferme que la fonction plus qui, elle aussi, possède un argument increment et dont le code se contente de renvoyer la somme : (ajout + increment). 
###     Dans le programme principal, créez deux fonctions, par exemple p = creer_plus(23) et p = creer_plus(42), puis affichez les valeurs données par p(100) et q(100). 


# Creation de la fonction fabrique (factory) 'creer_plus'.
def creer_plus(ajout):
    # Creation de la fonction fermeture 'plus'.
    def plus(increment):
        return ajout + increment
    return plus

# Programme principal
p = creer_plus(23)
q = creer_plus(42)

print(p(100))  # Devrait afficher 123
print(q(100))  # Devrait afficher 142

print(p(127)) # Devrait afficher  150
print(q(108)) # Devrait afficher  150 