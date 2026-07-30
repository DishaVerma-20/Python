def check_age(age:int):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif (age >= 150):
        raise ValueError("Age is not realistic")
    print("Your age is good")
    
# check_age(1000)

try:
    check_age(abc)
except ValueError as e:
    print(e)
except Exception as e:
    print(type(e).__name__)
    print(e)