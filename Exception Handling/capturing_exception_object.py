# Zero Division Error
# Value Error

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(f"num1/num2 = {num1/num2}")
# except:
#     print("Some error occured")

except Exception as e:
    # print(type(e))
    # for name only
    print(type(e).__name__)
    print(f"Error message = {e}")