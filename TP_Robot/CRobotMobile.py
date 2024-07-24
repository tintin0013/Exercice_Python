from CRobot import CRobot


class CRobotMobile(CRobot):
    def __init__(self, type = "unknown", sn = "1234", abs = 0, ord = 0, orientation = CRobot.NORD, status = "En service"):
        super().__init__(type, sn, orientation, status)
        self.abs = abs
        self.ord = ord

    def avancer(self, x):
        if self.orientation == CRobot.EST:
            self.abs += x
        elif self.orientation == CRobot.OUEST:
            self.abs -= x
        elif self.orientation == CRobot.NORD:
            self.ord += x
        elif self.orientation == CRobot.SUD:
            self.ord -= x
        else:
            raise ValueError("Orientation invalide")
        
    def afficherPosition(self):
        print(f"Position:  ({self.abs}, {self.ord})")

    def afficher(self):
        super().afficher()
        self.afficherPosition()