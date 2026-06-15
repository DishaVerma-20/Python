# Default Parameter Value

# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "Disha"):
    # print("Good morning", name) 
    # we can also use return
    return "Hello" + name + "!"
greet()
greet("Verma")
# greet(Verma) Verma is not defined

# jo bhi parameter hota hai vo required ho jaat haiii