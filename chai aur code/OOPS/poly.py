# Polymorphism

# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand 
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, __brand, model):
        super().__init__(__brand, model)
    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model S")
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

# yha pr depend kr rha hai on object type, car aur electric car