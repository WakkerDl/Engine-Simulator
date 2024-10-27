if __name__ == "__main__":
    import pygame
    import Starter
    import sys
    

    pygame.init()
    screen_width, screen_height = 800,400
    screen = pygame.display.set_mode((screen_width,screen_height))

    
    Starter.StarterEnable()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.flip() 