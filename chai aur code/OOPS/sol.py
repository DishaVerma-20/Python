# Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
# class Car:
#     brand = None
#     model = None

# my_car = Car() # ab yeh object
# print(my_car)

# blank form
class Car:
    def __init__(self, brand, model): # telephonr line
        # init = constructor
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)