# Validate Input
# Keep asking the user for input until they enter a number between 1 and 10.

# number = int(input())
# while number>10 or number<1:
#     number = int(input())
#     if (number<10 and number>1):
#         print(number, "ispr break hua haii!")
#         break

# while number <= 1 or number >= 10:
#     number = int(input())

# print("Valid number", number)


while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1<= number <=10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again!")