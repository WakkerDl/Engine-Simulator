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
        self.advance = advance # Профиль кулочка распредвала

    
    def rotate(self, rpm):
        # RPM Приходит от коленвала
        # ВОЗВРАЩАЕТСЯ подсчитанная по формуле скорость поворота
        pass
        







if __name__ == "__main__":
    import pygame
    import sys
    import math
    

    pygame.init()
    screen_width, screen_height = 800,400
    screen = pygame.display.set_mode((screen_width,screen_height))
    color = (255, 0, 0)  # Красный цвет

    # Список координат вершин многоугольника
    pointlist = [(100, 100), (200, 50), (300, 100), (200, 200), (100, 200)]
    pygame.display.set_caption("Распредвал")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.draw.polygon(screen, color, pointlist, 0)
            pygame.display.flip()