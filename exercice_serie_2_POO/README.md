### Exercice 1:
 1.  Définissez ci-dessous une classe Etudiant dont les attibuts sont: nom, prenom, note_nsi, note_maths et note_phy.
     Puis créez une méthode spéciale **str (self) qui permettra d'afficher 'NOM Prenom a obtenu note_nsi en NSI, note_maths en Mathématiques et note_phy en Physique' en tapant print(E) où E est une instance de la classe Etudiant

 2. Tapez ci-dessous le code permettant de créer les instances E1, E2, E3 et E4 qui représentent:
    - l'étudiant SARR Junior qui a eu 18 en NSI, 18 en Maths et 15 en Physique,
    - l'étudiant FUSIL Morgan qui a eu 17 en NSI, 15 en Maths et 16 en Physique, 
    - l'étudiant BEYA Noa qui a eu 14 en NSI, 19 en Maths et 18 en Physique et 
    - l'étudiant BONNET Anne qui a eu 5 en NSI, 7 en Maths et 9 en Physique.
    Puis faites afficher ces instances à l'aide de la méthode spéciale **str (self)** créée juste avant.


### Exercie 2:
   Définissez ci-dessous une classe Fraction dont les attibuts sont : num et den, des entiers représentants le numérateur et le dénominateur.
   Le dénominateur sera nécessairement un entier strictement positif, sans quoi le constructeur de cette classe devra lever une erreur (à l'aide d'un "assert").
   Puis créez une méthode spéciale **str (self) qui permettra d'obtenir 'numerateur/denominateur' ou seulement 'numerateur' si le dénominateur vaut 1, en tapant print(F)** où F est une instance de la classe Fraction .

   Tapez ci-dessous le code permettant de créer les instances F1, F2, F3 et F4 qui représentent les fractions 3/4 , -8/1 , 2/3 et 21/28. Puis faites afficher ces instances à l'aide de la méthode spéciale **str (self)** créée juste avant.


### Exercice 3:
  Dans cet exercice on se propose de réaliser un jeu de bataille simplifié. Ce jeu se jouera à 2 (soi même contre l'ordinateur), et chaque joueur se verra distribuer un paquet de 8 cartes d'un jeu de 52 cartes.
  Chaque carte est définie par sa valeur (2 pour un 2, 3 pour un 3, ..., 11 pour un valet, 12 pour une dame ,...) et par son motif ('coeur', 'carreau', 'pique' ou 'trèfle').
  Pour chaque "combat", le joueur retournera la première carte de son paquet et la confrontera à la première carte du paquet de l'autre joueur.
  C'est le joueur qui retournera la carte qui a la plus grande valeur qui ramassera les 2 cartes et les remettra à la fin de son paquet. 
  En cas d'égalité de valeurs, les joueurs remettront cette carte à la fin de leur paquet et passeront à la suivante.
  Le gagnant sera le joueur pour lequel il restera le plus de cartes à la fin des 10 combats.
  Pour cela on va créer une classe Carte afin de définir les objets cartes, puis une classe Paquet afin de définir un objet paquet de cartes.
  Nous pourrons ensuite programmer ce jeu de bataille.

  1. Réfléchissez à ce que peuvent être les attributs d'une instance de la classe Carte, et en
     déduire ci-dessous le code permettant de créer la classe Carte et de définir ses attributs.

     Codez aussi une méthode spéciale str(self) permettant de renvoyer un affichage du type "2 de pique".
  2. Pour pouvoir comparer 2 éléments de la classe Carte, il sera utile de programmer les
     méthode spéciales **lt(self,other) et __ eq(self,other)** .
     Ci-dessus, en dessous la méthode spéciale str(self)__ de la classe Carte, codez ces 2 méthodes.

  3. Nous allons maintenant créer une classe Paquet. Chaque instance de cette classe sera
     constituée d'une liste de cartes. Cette liste sera donc l'unique attribut d'une instance de la classe Paquet.
     Créez ci-dessous le code permettant de créer la classe Paquet et de définir son attribut.
     Codez aussi une méthode spéciale **str(self)** permettant de renvoyer un affichage du paquet de cartes du type : 'as de pique ; roi de trèfle ; etc...'.

  4. Pour créer notre jeu de bataille, nous allons devoir être capable de :
     • ajouter une carte au paquet
     • supprimer une carte d'un paquet
     • repositionner la première carte du paquet à la fin du paquet (à l'aide des 2 premières méthodes).
     Pour cela, ci-dessus, en dessous la méthode spéciale str(self) de la classe Paquet, codez les méthode ajoute_carte(self,carte), puis enleve_carte(self,carte) et repositionne_carte(self).

  5. Pour terminer, nous allons programmer notre jeu de bataille en utilisant les objets créés dans les classes Carte et Paquet, ainsi que leurs méthodes.
     Complétez le code ci-dessous pas à pas.
     Réalisez au fur et à mesure des tests (en faisant afficher des résultats intermédiaires par exemples) pour vérifier pas à pas la bonne avancée du projet.