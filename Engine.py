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

        # Define torque curve parameters
        self.max_torque = 400.0  # Max torque at peak torque RPM (Nm)
        self.peak_torque_rpm = 3000  # RPM at which max torque occurs
        self.max_power_rpm = 6000  # RPM at which max power occurs

    def calculate_torque(self):
        """Calculate torque based on current RPM using a polynomial approximation."""
        if self.rpm < self.idle_rpm:
            return 0.0  # No torque below idle RPM
        elif self.rpm <= self.peak_torque_rpm:
            return (self.max_torque / self.peak_torque_rpm) * self.rpm
        elif self.rpm <= self.max_power_rpm:
            return (self.max_torque - (self.max_torque / (self.max_power_rpm - self.peak_torque_rpm)) * (self.rpm - self.peak_torque_rpm))
        else:
            return 0.0  # No torque above max power RPM

    def simulate(self, throttle):
        """Simulate engine performance based on throttle input."""
        if not self.is_running:
            self.rpm, self.torque, self.power = 0.0, 0.0, 0.0
            return

        effective_throttle = min(max(throttle, 0), 1)
        throttle_response = effective_throttle ** 2
        
        if effective_throttle > 0:
            self.rpm = min(self.idle_rpm + throttle_response * (self.max_power_rpm - self.idle_rpm), self.max_power_rpm)
        else:
            self.rpm = self.idle_rpm
        
        # Torque and power calculations
        self.torque = self.calculate_torque()
        omega = (self.rpm * (math.pi / 30))  # Convert RPM to rad/s
        self.power = (self.torque * omega) / 1000  # Convert to kW

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
        f"Throttle: {throttle:.2f}"
    ]

    screen.fill((30, 30, 30))  
    for i, text in enumerate(metrics_texts):
        rendered_text = font.render(text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50 + i * 50))

    pygame.draw.rect(screen, (0, 255, 0), (50, 250, throttle * 300, 20)) 

    instructions_text = font.render("Press 'S' to Start | 'O' to Stop | UP to Throttle", True, (255, 255,255))
    screen.blit(instructions_text, (50,280))

def draw_engine_visual(screen, rpm):
    """Draw a detailed visual representation of the engine components with animations."""
    center_x = screen.get_width() // 2 + 100
    center_y = screen.get_height() // 2
    
    # Draw Cylinder Block
    pygame.draw.rect(screen,(100 ,100 ,100), (center_x -60 , center_y -40 ,120 ,80))  
    
    # Draw Crankshaft with rotation effect based on RPM
    crankshaft_width = int(120 * rpm / engine.max_power_rpm)
    
    crankshaft_angle_offset = math.sin(pygame.time.get_ticks()) * 3
    
    pygame.draw.rect(screen,
                     (50 ,50 ,50),
                     (center_x - crankshaft_width //2 + crankshaft_width //4 + crankshaft_angle_offset,
                      center_y +30 , crankshaft_width //2 ,10))

    # Draw Pistons with animation based on RPM
    piston_height_base = int(40) 
    for i in range(engine.cylinders):
        piston_height = piston_height_base + int(rpm / engine.max_power_rpm *20)  
        
        piston_x = center_x - ((engine.cylinders -1) *25)/2 + i * (25) 
        pygame.draw.rect(screen,(200 ,200 ,200), (piston_x , center_y - piston_height ,15 ,piston_height))
    
    # Draw Cylinder Head and Valves
    pygame.draw.rect(screen,(150 ,150 ,150), (center_x -60 , center_y -40 ,120 ,10))
    
    valve_positions = [-45 + i *30 for i in range(engine.cylinders)]
    
    for pos in valve_positions:
        pygame.draw.circle(screen,(255 ,255 ,255), (center_x + pos , center_y -55),5)

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

        # Start/stop the engine with 'S' and 'O'
        if keys[pygame.K_s]:
            engine.start()  
        
        if keys[pygame.K_o]:
            engine.stop()  
        
        # Increase throttle with UP arrow key
        if keys[pygame.K_UP]:
            throttle += 0.01  
            throttle = min(throttle,1.0) 
        
        elif not keys[pygame.K_UP] and throttle > 0.0:
            throttle -= 0.01  
            throttle = max(throttle,0.0) 
        
        engine.simulate(throttle)

        draw_metrics(screen, engine, throttle)
        
        draw_engine_visual(screen, engine.rpm)
        
        pygame.display.flip()  
        
if __name__ == "__main__":
    main()
