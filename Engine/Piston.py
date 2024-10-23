class Piston:
    def __init__(self, diameter_piston, conrod_length, mass, piston_height, displacement):
        self.diameter_piston = diameter_piston #Диаметр поршня
        self.conrod_length = conrod_length # Длина шатуна 
        self.mass = mass # Масса
        self.piston_height = piston_height # Высота поршня 
        self.displacement = displacement # Вытесняемый объём жидкости поршнем