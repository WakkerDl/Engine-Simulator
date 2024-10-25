import Const

class IgnitionModule:
    def __init__(self, cylinder_counter):
        self.cylinder_counter = cylinder_counter
        self.output_voltage = Const.output_voltage_ignition_coil

class SparkPlug:
    def __init__(self):
        self.the_size_of_the_spark_gap = Const.the_size_of_the_spark_gap