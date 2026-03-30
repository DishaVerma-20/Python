# Class Variables

# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0
    # ye niche vala part constructor haii
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # self.total_car += 1
        # Python naya instance variable bana deta, jo galat hota
        Car.total_car += 1 # ese bhi kr skte haii
        # Ye correct way hai class variable update karne ka
    
my_car = Car("Tata", "Safari")
safari = Car("Tata", "Nexon")

print(my_car.brand)
print(my_car.model)

# agar hmne inherit kra hai aur parent class vo hai jha variable count vala hai toh, inherit class ka object bhi consider kra jaygaa

print(Car.total_car)
# python mai immediate garbage collection nahi hota haiii
# Python does not automatically decrease count on object deletion