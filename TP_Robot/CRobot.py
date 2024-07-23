
class CRobot():
    # Initialisation des constantes d'orientation
    NORD = 1
    EST = 2
    SUD = 3
    OUEST = 4

    def __init__(self, type = "unknown", sn = "1234", orientation = NORD, status = "En service"):
        self.type = type
        self.sn = sn 
        # self.orientation = CRobot.NORD
        # self.status = "En service"
        self.setOrientation(orientation) # Utilisation de la méthode pour valider l'orientation
        self.setEtat(status)             # Utilisation de la méthode pour valider le status

    def getType(self):
        return self.type

    def getSN(self):
        return self.sn
    
    def getOrientation(self):
        return self.orientation
    
    def getStatus(self):
        return self.status
    
    def setOrientation(self, new_orientation):
        if new_orientation in [CRobot.NORD, CRobot.EST, CRobot.SUD, CRobot.OUEST]:
            self.orientation = new_orientation
        else:
            raise ValueError("Orientation invalide")    
        
    def setEtat(self, new_status):
        if new_status in ["En service", "Hors service", "En reparation"]:
            self.status = new_status
        else:
            raise ValueError("Status invalide")
        
    def tourner(self, direction = "gauche"):
        if direction == "gauche":
            self.orientation = CRobot.NORD if self.orientation == CRobot.OUEST else self.orientation + 1
        elif direction == "droite":
            self.orientation = CRobot.OUEST if self.orientation == CRobot.NORD else self.orientation - 1
        else: 
            raise ValueError("Direction invalide")    
        
    def afficher(self):
        orientations = {
            CRobot.NORD: "NORD",
            CRobot.EST: "EST",
            CRobot.SUD: "SUD",
            CRobot.OUEST: "OUEST"
        }
        print()
        print(f"Type: {self.getType()}")
        print()
        print(f"Numero de Serie: {self.getSN()}")
        print()
        print(f"Orientation: {orientations[self.getOrientation()]}")
        print()
        print(f"Satus: {self.getStatus()}")
        print()





