import pygame
import sys
import math

class Engine:
    def __init__(self, cylinders=4, displacement=2.0, idle_rpm=800):
        self.cylinders = cylinders
        self.displacement = displacement  # in liters
        self.rpm = 0.0  # Revolutions per minute
        self.torque = 0.0  # Torque in Nm
        self.power = 0.0  # Power in kW
        self.is_running = False  # Engine state
        self.idle_rpm = idle_rpm  # Idle RPM
        self.normal_temperature = 30.0
        self.max_temperature = 120.0
        self.cooling_rate = 1.5

        # Define torque curve parameters
        self.max_torque = 400.0  # Max torque at peak torque RPM (Nm)
        self.peak_torque_rpm = 5000  # RPM at which max torque occurs
        self.max_power_rpm = 6000  # RPM at which max power occurs

        # Valve states
        self.intake_valve_open = [False] * cylinders  # List to hold intake valve states for each cylinder
        self.exhaust_valve_open = [False] * cylinders  # List to hold exhaust valve states for each cylinder
        self.valve_timer = 0  # Timer for valve operation
        self.valve_duration = 30  # Duration for which valves stay open

    def temperature(self):
        """Update the engine temperature based on RPM and throttle."""
        if not self.is_running:
            return
        
        if self.rpm > 0:
            temperature_increase = self.rpm / 1000
            self.cooling_rate = self.rpm / 1000 + 0.001
            if self.rpm > 799 and self.rpm < 2000:
                self.cooling_rate -= 0.0095
                self.normal_temperature += temperature_increase
                self.normal_temperature = 80
        
        if self.normal_temperature >= self.max_temperature:
                print("Warning: Engine overheating!")
                self.normal_temperature = self.max_temperature
        
        #else :
        if self.normal_temperature > 30:  
                self.normal_temperature -= self.cooling_rate
        


    def calculate_torque(self):
        """Calculate torque based on current RPM using a polynomial approximation."""
        if self.rpm < self.idle_rpm:
            return 0.0
        elif self.rpm <= self.peak_torque_rpm:
            return (self.max_torque / self.peak_torque_rpm) * self.rpm
        elif self.rpm <= self.max_power_rpm:
            return (self.max_torque - (self.max_torque / (self.max_power_rpm - self.peak_torque_rpm)) * (self.rpm - self.peak_torque_rpm))
        else:
            return 0.0

    def simulate(self, throttle):
        """Simulate engine performance based on throttle input."""
        if not self.is_running:
            self.rpm, self.torque, self.power = 0.0, 0.0, 0.0
            return
        
        effective_throttle = min(max(throttle, 0), 1)

        throttle_response = effective_throttle ** 3
        
        if effective_throttle > 0:
            target_rpm = min(self.idle_rpm + throttle_response * (self.max_power_rpm - self.idle_rpm), self.max_power_rpm)
            self.rpm += (target_rpm - self.rpm) * 0.1  
        else:
            self.rpm += (self.idle_rpm - self.rpm) * 0.1
        
        # Torque and power calculations
        self.torque = self.calculate_torque()
        omega = (self.rpm * (math.pi / 30))  
        self.power = (self.torque * omega) / 1000  

        if self.rpm > 1000:  
            self.valve_timer += 1
            
            for i in range(self.cylinders):
                if (self.valve_timer // (self.valve_duration // len(self.intake_valve_open))) % len(self.intake_valve_open) == i:
                    self.intake_valve_open[i] = True
                else:
                    self.intake_valve_open[i] = False
                
                if (self.valve_timer // (self.valve_duration // len(self.exhaust_valve_open))) % len(self.exhaust_valve_open) == i:
                    self.exhaust_valve_open[i] = True
                else:
                    self.exhaust_valve_open[i] = False
        
        self.temperature()

    def start(self):
        """Start the engine."""
        if not self.is_running:
            print("Engine started.")
            self.is_running = True
            self.rpm = self.idle_rpm

    def stop(self):
        """Stop the engine."""
        if self.is_running:
            print("Engine stopped.")
            self.is_running = False
            self.rpm = 0.0

def draw_metrics(screen, engine, throttle):
    """Draw the engine metrics on the screen."""
    font = pygame.font.Font(None, 36)

    metrics_texts = [
        f"RPM: {engine.rpm:.2f}",
        f"Torque: {engine.torque:.2f} Nm",
        f"Power: {engine.power:.2f} kW",
        f"Throttle: {throttle:.2f}",
    ]

    screen.fill((30, 30, 30))  
    for i, text in enumerate(metrics_texts):
        rendered_text = font.render(text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50 + i * 50))

    pygame.draw.rect(screen, (0, 255, 0), (50, 250, throttle * 300, 20)) 

    instructions_text = font.render("Press 'S' to Start | 'O' to Stop | UP to Throttle", True, (255,255 ,255))
    screen.blit(instructions_text, (50,280))

def draw_gauge(screen, engine):
    """Draw a visual representation of the temperature gauge."""
    gauge_x = screen.get_width() - 150
    gauge_y = screen.get_height() // 2 - 50
    pygame.draw.rect(screen, (200,200,200), (gauge_x -10, gauge_y -10, 20, 110))   # Gauge outline
    current_temp_height = int((engine.normal_temperature / engine.max_temperature) * 100)
    pygame.draw.rect(screen,(255 - current_temp_height*2.55, current_temp_height*2.55, 0),
    (gauge_x -5 , gauge_y + (100 - current_temp_height),10,current_temp_height))   # Temperature bar
    temp_label_text = f"{engine.normal_temperature:.1f} °C"
    font = pygame.font.Font(None,36)
    rendered_label_text = font.render(temp_label_text ,True,(255 ,255 ,255))
    screen.blit(rendered_label_text ,(gauge_x -40 ,gauge_y +120))


def draw_camshaftlobe(surface, color, center_x, center_y, size):
    """Draw a camshaft lobe at specified position."""
    points = []
    for i in range(8):
        angle = math.radians(60 * i)
        x = center_x + size * math.cos(angle)
        y = center_y + size * math.sin(angle)
        points.append((x, y))
    
    pygame.draw.polygon(surface, color, points)

def draw_engine_visual(screen, engine):
    """Draw a detailed visual representation of the engine components with animations."""
    center_x = screen.get_width() // 2 + 100
    center_y = screen.get_height() // 2
    
    pygame.draw.rect(screen,(100 ,100 ,100), (center_x -60 , center_y -40 ,120 ,80))  
    
    crankshaft_width = int(120 * engine.rpm / engine.max_power_rpm)
    
    crankshaft_angle_offset = math.sin(pygame.time.get_ticks() * 0.001) * 3
    
    pygame.draw.rect(screen,(50 ,50 ,50),(center_x - crankshaft_width //2 + crankshaft_width //4 + crankshaft_angle_offset,center_y +30 , crankshaft_width //2 ,10))

    crank_angle_per_revolution = engine.rpm / 60 * (360 / engine.cylinders)   
    current_angle = pygame.time.get_ticks() * (engine.rpm / engine.max_power_rpm) % 360

    firing_ignition_order = [i for i in range(engine.cylinders)]

    for i in firing_ignition_order:
        
        angle_offset = i * crank_angle_per_revolution + current_angle
        
        piston_base_height = int(30)
        
        if angle_offset < 180:  
            piston_height = piston_base_height + int(math.sin(math.radians(angle_offset)) * (engine.rpm / engine.max_power_rpm * 20))
        else:
            piston_height = piston_base_height - int(math.sin(math.radians(angle_offset -180)) * (engine.rpm / engine.max_power_rpm * 20))

        piston_x = center_x - ((engine.cylinders -1) *25)/2 + i * (25) 
        pygame.draw.rect(screen,(200 ,200 ,200), (piston_x , center_y - piston_height ,14 ,piston_height))
    
    pygame.draw.rect(screen,(150 ,150 ,150), (center_x -60 , center_y -50 ,120 ,10))
    
    valve_positions_intake = [-20 + i *15 for i in range(engine.cylinders)]  
    valve_positions_exhaust = [-20 + i *15 for i in range(engine.cylinders)]  

    for i in range(engine.cylinders):
        
        draw_camshaftlobe(screen,(255 ,255 ,255), center_x + valve_positions_intake[i], center_y -55,5) 
        
        if engine.intake_valve_open[i]:
            draw_camshaftlobe(screen,(200 ,50 ,50), center_x + valve_positions_intake[i] +7 , center_y -55 ,5)  
        
        draw_camshaftlobe(screen,(100 ,100 ,100), center_x + valve_positions_exhaust[i], center_y -55-10,5) 
        
        if engine.exhaust_valve_open[i]:
            draw_camshaftlobe(screen,(200 ,50 ,50), center_x + valve_positions_exhaust[i] +7 , center_y -55-12 ,5)  

def main():
    pygame.init()
    
    screen_width, screen_height = 800,400
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Engine Simulator")

    global engine 
    engine = Engine()
    
    throttle = 0.0

    while True:
        
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

       keys = pygame.key.get_pressed()

       if keys[pygame.K_s]:
           engine.start()  
       
       if keys[pygame.K_o]:
           engine.stop()  
       
       if keys[pygame.K_UP]:
           throttle += 0.00035  
           throttle = min(throttle,1.0) 
       
       elif not keys[pygame.K_UP] and throttle > 0.0:
           throttle -= 0.00035  
           throttle = max(throttle,0.0) 
       
       engine.simulate(throttle)

       engine.temperature()
       
       draw_metrics(screen, engine, throttle)
       
       draw_engine_visual(screen, engine)

       draw_gauge(screen, engine)

       
       pygame.display.flip()  

if __name__ == "__main__":
   main()