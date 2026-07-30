def check_age() -> None:
    try:
        age = int(input("Enter your age: "))
        if age<0:
            print("Age cannot be negative")
        elif age>=150:
            print("Age is not realistic")
    except ValueError as e:
        print(f"Inside function error = {e}")
        raise # bahar vale funxn ko bhi pta chal jayga raise krne ke baad
    except Exception as e:
        print(f"Inside function error = {e}")

try:
    check_age()
except Exception as e:
    print(f"Outside function error = {e}")
else:
    print("Success")