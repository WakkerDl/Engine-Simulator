import Const
import keyboard

# СТАРТ


class Starter:
    def __init__(self, rpm):
        self.voltage = Const.voltage_car_system 
        self.rpm = rpm



def StarterEnable():
    Starter.rpm = 0
    while True:
        if keyboard.is_pressed('s'):
            if Starter.rpm < 200:  
                Starter.rpm += 1 
            

    




if __name__ == "__main__":
    import pygame
    import Starter
    import sys
    

    pygame.init()
    screen_width, screen_height = 800,400
    screen = pygame.display.set_mode((screen_width,screen_height))
    
    starter = Starter.rpm(0)

    starter.rpm 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.flip() 