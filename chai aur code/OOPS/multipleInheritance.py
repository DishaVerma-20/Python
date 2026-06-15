# Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    # def __init__(self, battery):
    #     self.battery = battery

    def battery_size (self):
        return "This is battery" # fixed output

class Engine:
    # def __init__(self, engine):
    #     self.engine = engine

    def engine_info(self):
        return "This is Engine"
    
class ElectricCar(Battery, Engine):
    pass

my_new = ElectricCar() # object bnao
print(my_new.battery_size())
print(my_new.engine_info())