

from CRobotMobile import CRobotMobile


robots_mobiles = [
    CRobotMobile("Type Roulant", "RM-1V"),
    CRobotMobile("Type Volant", "RM-1V", 10, 20, CRobotMobile.SUD),
    CRobotMobile("Type Marchant", "RM-1R",8, 7, CRobotMobile.EST, "En reparation"),
    CRobotMobile("type: Flottant", "RM-1F", 0, 0, status = "Hors service")
]

# Instanciation et utilisation des robots
print()
print("************** ROBOT AVANT MODIFICATION **************")
robots_mobiles[0].afficher()
robots_mobiles[0].setOrientation(CRobotMobile.EST)
robots_mobiles[0].setEtat("En reparation")
robots_mobiles[0].avancer(10)
robots_mobiles[0].tourner("droite")
robots_mobiles[0].avancer(5)
print("************** ROBOT APRES MODIFICATION **************")
robots_mobiles[0].afficher()
print()
print("************** AUTRES ROBOTS **************")

for robot in robots_mobiles[1:]:
    robot.afficher()
    print()