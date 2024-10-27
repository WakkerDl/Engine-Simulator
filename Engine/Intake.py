class Intake:
    def __init__(self):
        self.dleThrottlePlatePosition = 0.985 #Положение дроссельной заслонки на холостом ходу
        self.fuel_amount = 1  # кол-во топлива
        self.air_amount = 15  # кол-во воздуха
        

    def start(self):
        """
        Метод впуска
        """
        
