import EngineBlock
import CylinderHead
import Intake
import ExhaustSystem
import Piston
import Fuel 

class Engine:
    def __init__(self, engine_block, cylinder_head, intake, exhaust_system, piston, fuel):
        self.engine_block = engine_block
        self.cylinder_head = cylinder_head
        self.intake = intake,
        self.exhaust_system = exhaust_system
        self.piston = piston
        self.fuel = fuel
        return
    

    # def build(self, engine_block, cylinder_head, intake, exhaust_system, piston, fuel):
    #     """
    #     Метод для сборки двигателя
    #     """
    #     self.engine_block = engine_block
    #     self.cylinder_head = cylinder_head
    #     self.intake = intake,
    #     self.exhaust_system = exhaust_system
    #     self.piston = piston
    #     self.fuel = fuel


    def start(self):
        pass 
