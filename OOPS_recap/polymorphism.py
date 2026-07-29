class Animal:
    def move(self):
        print("I am moving")

class Dog(Animal):
    def move(self):
        print("I am running on 4 legs")

dog = Dog()
dog.move()
