

from CRobot import CRobot


robots = [
    CRobot("Type Roulant", "AP-1V"),
    CRobot("Type Volant", "AP-1V", CRobot.SUD),
    CRobot("Type Marchant", "AP-1R",CRobot.EST, "En reparation"),
    CRobot("type: Flottant", "AP-1F", status = "Hors service")
]

# Instanciation et utilisation des robots
print()
print("************** ROBOT AVANT MODIFICATION **************")
robots[0].afficher()
robots[0].setOrientation(CRobot.EST)
robots[0].setEtat("En reparation")
robots[0].tourner()
print("************** ROBOT APRES MODIFICATION **************")
robots[0].afficher()
print()
print("************** AUTRES ROBOTS **************")

for robot in robots[1:]:
    robot.afficher()
    print()