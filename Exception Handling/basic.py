# ValueError
try:
    age = int(input("Enter the age: "))
    if age>=18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
except:
    print("Some error occured")

print("Done")

# ZeroDivisionError
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(f"num1/num2 = {num1/num2}")
# except:
#     print("Some error occured")
# specification show krne ke liye
except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter proper integers")

# koi bhi aur error ho
except:
    print("Some error occured")

try:
    num = int(input("Enter the num"))
    result = 100/num
except(ValueError, ZeroDivisionError):
    print("Invalid input, try again")

# do not write except only, try to write each exception separately