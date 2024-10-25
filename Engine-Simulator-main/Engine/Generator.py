import Const

class Generator:
    def __init__(self, rpm, charging):
        self.rpm = rpm #Оборот/мин
        self.charging = charging #Зарядка
        self.power = Const.power_generator #Мощность 