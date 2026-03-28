# Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.


class Car:
    def __init__(self, brand, model):
        self.__brand = brand # 2 underscore meaning private, class ke andar toh access kar payge but object nahi kr payga 
        self.model = model

    # def get_brand(self):
    def chai_brand(self): # yha pr chai not good practice
        return self.__brand +  " !"

my_car = Car("Tata", "Safari")
# print(my_car) # ye reference
# print(my_car.brand) # abhi bhi access hai
print(my_car.chai_brand())