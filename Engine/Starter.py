import Const
import keyboard

# СТАРТ


class Starter:

    def __init__(self):
        # self.voltage = Const.voltage_car_system 
        self.rpm = 0
        self.rpm_speed = 1


    def toggle(self):
        if keyboard.is_pressed('s'):
            if self.rpm < 200:  
                self.rpm += self.rpm_speed 

    def get_rpm(self):
        return self.rpm

    def set_rpm_speed(self, speed):
        self.rpm_speed =  speed



if __name__ == "__main__":
    import pygame
    import sys
    

    pygame.init()
    screen_width, screen_height = 800,400
    screen = pygame.display.set_mode((screen_width,screen_height))
    starter = Starter()
    starter2 = Starter()
    starter2.set_rpm_speed(2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            starter.toggle()
            starter2.toggle()
            print("rpm1:", starter.get_rpm(), "rpm2:", starter2.get_rpm())
            
            pygame.display.flip() 




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    
#     def get_info(self):
#         return (self.name, self.age)



# alex = Person(name="Alex", age=18)
#         # Person("Alex", 18)
# mike = Person(name='Mike', age=12)

# print(alex.get_info())
# print(mike.get_info())


