#### TP-ROBOT

## 1. CRobot.py : Créer une classe CRobot qui crée un robot défini par :
— Les caractéristiques suivantes
 — Type
 — SN : Numéro de Série
 — Orientation
 — Status (En service, Hors service, En réparation)
 — Les méthodes suivantes :
 — Constructeur Robot () ou Robot (type, sn)
 — getType () : retourne le type de robot
 — getSN () : retourne le numéro de série du robot
 — getOrientation () : retourne l’orientation du robot
 — getStatus () : retourne le status du robot
 — setOrientation (…) : définit l’orientation du robot
 — setEtat (…) : définit l’état du robot
 — tourner (…) : tourne le robot d’un 1/4 de tour
 — afficher () : affiche les informations du robot
— orientation est un attribut de type entier qui désigne l’orientation du robot.
 1 : NORD, 2 : EST, 3 : SUD, 4 : OUEST
— tourner permet de tourner le robot, par défaut vers la gauche
— afficher permet d’afficher l’état, l’orientation, le numéro de série et le type du robot.
Instancier cette classe sur un tableau de 4 robots en utilisant l’ensemble des
fonctions pour au moins l’un d’eux.

## 2. CRobotMobile.py : Créer un classe CRobotMobile qui
— hérite de CRobot
— se caractérise en plus avec les attributs entiers abs et ord qui définissent la
position du RobotMobile
— possède une méthode avancer (…) qui permet d’avancer le Robot selon son
orientation
 — si on avance de x vers l’Est, l’abscisse augmente de x
 — si on avance de x vers l’Ouest, l’abscisse diminue de x
 — si on avance de x vers le Nord, l’ordonnée augmente de x
 — si on avance de x vers le Sud, l’ordonnée diminue de x
— possède une méthode affichePosition () qui affiche la position (coordonnées)

- (a) Écrire un constructeur sans argument de la classe CRobotMobile.
- (b) Écrire un constructeur à quatre arguments (type, sn, abs, ord) de la classe
CRobotMobile.
- (c) Redéfinissez la méthode affiche tout en utilisant celle de la classe mère et la méthode
affichePosition ().