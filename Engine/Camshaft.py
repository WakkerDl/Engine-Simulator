import math
import Crankshaft

"""
Коленвал крутит распредвал (В коленвале пишим метод для вращения распредвала)
        из метода коленвала в распредвал идёт количество оборотов
Распредвал получает количество оборотов
    метод calculate_rotation для вычисления поворота в зависимости от кол-ва оборотов
    метод draw_camshaft для отрисовки распредвала
    и метод rotate_camshaft для поворота распредвала со скоростью 
"""

def rotate_point(point, center, angle):
    x, y = point
    cx, cy = center
    new_x = cx + (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle)
    new_y = cy + (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle)
    return (new_x, new_y)



class Camshaft:
    """
    Распредвал
    """
    def __init__(self, lobes, advance):
        self.lobes = lobes # Номер кулочка распредвала
    
    def rotate(self, rpm):
        # RPM Приходит от коленвала
        # ВОЗВРАЩАЕТСЯ подсчитанная по формуле скорость поворота
        pass


camshaft = Camshaft(lobes = 8)

crankshaft = Crankshaft(10,10,10,10)

camshaft.rotate(rpm=crankshaft.rpm)