try:
    num = int(input("Enter a number: "))
    res = 100/num
except ValueError:
    print("not a valid number")
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print(f"result = {res}")
finally:
    print("Calculation attempt complete")