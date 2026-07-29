class Animal:
    def __init__(self, name:str, age:int) -> None:
        self. name = name
        self.age = age
        
    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

class Dog(Animal): # inherits from animal
    def __init__(self, name:str, age:int, breed:str): # uppr vala init nahi chal payga bina iske
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print("I am barking")

    def display(self):
        print(f"Hey, this is {self.name} and my age is {self.age}, also breed is {self.breed}.")

# object
# dog = Dog() Error 
dog = Dog("Bruno", 4, "Pomerian")
dog.bark()
dog.eat()
dog.sleep()
dog.display()
