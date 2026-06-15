# Prime Number Checker
# Check if a number is prime.

number = int(input("Enter a number: "))
if (number <= 1):
    print("Not a prime number")
else:
    for i in range (2, number):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
            print("Prime number")


# using flag
number = 29
is_prime = True
if number > 1:
     for i in range (2, number):
          if number % i == 0:
               is_prime = False
               break
if is_prime == True: # jyada better hoga, if is_prime:
     print("Prime number")
else:
     print("Not prime")

    
    