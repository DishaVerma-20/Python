# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input())
day = input()

# if (day == "wednesday"):
#     if age < 18:
#         ticket = 8-2
#         print(ticket)
#     else:
#         print(12 - 2)
# else:
#     if age<18:
#         ticket = 8
#         print(ticket)
#     else:
#         print(12)



price = 12 if age>= 18 else 8

if day == "wednesday":
    price = price-2
print(price)