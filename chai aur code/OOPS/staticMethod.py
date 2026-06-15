# Static Method

# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @staticmethod
    # static method mai self likhna he nahi hai, kyuki baat he nahi krni isko apne objects se, taar kaato objects ke saath
    def general_description():
        return "Cars are amazing"
    
    @property
    def model(self):
        return self.__model
# print(my_car.brand)
# print(my_car.model)
# print(my_car.general_description())
# print(Car.general_description())
my_car = Car("Tata", "Safari")
# my_car.model = "City"
# print(my_car.model()) ye acces nahi kar payge
print(my_car.model) # property ki trh access milega isme
# but ham change nahi krna chahte hai, read only bnana hai srf
# 1st attribute ko private bnao

