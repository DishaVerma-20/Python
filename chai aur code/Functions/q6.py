# Lambda Function

# Problem: Create a lambda function to compute the cube of a number.

def cubes(a): # parameters, placeholders
    return a * a * a
    # return a ** 3 , uppr vale return ka pdega srf uske baad nahii
print(cubes(int(input("Enter number: "))))

cube = lambda x: x*x*x # short functions, frameworks mai use hota hai, flask, on the GO chije
print(cube(9)) # arguments
