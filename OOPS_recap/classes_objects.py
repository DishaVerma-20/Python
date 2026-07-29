class Student:
    # attributes: classe ke andar variable
    # inka bhi koi use nahi hai as such.. hum seedhe seedhe constructor or initializer ki help le sakte haiii
    # name = ''
    # age = 0
    # gender = ''

    # methods
    # function inside class
    def __init__(self, name:str, age:int, gender:str) -> None:
        print("This is a constructor or initializer")
        # attributes
        self.name = name
        self.age = age
        self.gender = gender
    def display(self) -> None :  # ye method kuch return nahi kara raha haii, aise python mai show karte haii
        # print("This is a display function.")
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")
    def get_age(self) -> int:
        return self.age
    # def set_info(self):
    #     self.name = input("Enter your name: ")
    #     self.age = int(input("Enter age: "))
    #     self.gender = input("Enter your sex: ")
    # def set_info(self, name, age, gender):
    # type annotations"!
    # jab hmare paas constructor hai toh hame iski need he nahi pdegi ab..
    def set_info(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender
# s1 = Student()
# # this is an object
# s1.name = "Disha"
# s1.age = 21
# s1.gender = "Female"
# print(s1)
# print(s1.name)
# print(s1.age)
# print(s1.gender)

# # another object s2
# s2 = Student()
# print(s2.name)
# s1.display()

# sbse phle object bnayge
s1 = Student("Disha", 21, "Female")
# s1.set_info("Disha", 21, "Female")
s1.display()
print(s1.get_age())