import Starter

class Crankshaft:
    def __init__(self, flywheel_mass, rodJournals, mass, rpm):
        self.flywheel_mass = flywheel_mass #Масса маховика
        self.rodJournals = rodJournals # Вкладыши 
        self.mass = mass # Масса коленвала
        # rpm зависит от стартера 
        self.rpm = rpm 
        self.pos_x = 0
        self.pos_y = 0

