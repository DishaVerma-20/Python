class Student:
    # attributes: classe ke andar variable
    name = ''
    age = 0
    gender = ''

    # methods
    # function inside class
    def display(self):
        # print("This is a display function.")
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

    # def set_info(self):
    #     self.name = input("Enter your name: ")
    #     self.age = int(input("Enter age: "))
    #     self.gender = input("Enter your sex: ")

    # def set_info(self, name, age, gender):
    # type annotations
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
s1 = Student()
s1.set_info("Disha", 21, "Female")
s1.display()

