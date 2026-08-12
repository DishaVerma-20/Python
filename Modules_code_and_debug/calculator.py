# now this is a module named calculator.. files he module hoti hai

def add(a:int, b:int) -> int:
    return a+b

def sub(a:int, b:int) -> int:
    return a-b

def mul(a:int, b:int) -> int:
    return a*b

def divide(a:int, b:int) -> float:
    return a/b # this is true division

PI = 3.14 # capital mai iss liye cause i know it will never change

if __name__ == "__main__":
    print(f"Calculator file __name__ = {__name__}")
    print("Testing this code -- Start")
    result = add(10, 20)
    print(f"Addition answer = {result}")
    print("Testing this code -- End")

# "Run this code only when this file is run directly, not when it is imported."

# How python finds module?
'''1) current directory - where your script runs 
2) PYTHONPATH - environment variables
3) Standard library - built-in
4) Site-packages - download from the internet, pip installs
5) last mai agar nahi mila then it will throw error'''