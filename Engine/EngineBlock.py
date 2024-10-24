import Crankshaft
import Const

class EngineBlock:
    def __init__(self,count_cylinder, mass):
        self.diameter = Const.diameter # Диаметор цилиндра 
        self.count_cylinder = count_cylinder # Количество цилидров
        self.mass = mass # Масса