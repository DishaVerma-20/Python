# Leap year checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400). 

year = int(input())

# If the year is not divisible by 4 → Not a leap year
# If the year is divisible by 4 but not by 100 → Leap year
# If the year is divisible by 100 but not by 400 → Not a leap year
# If the year is divisible by 400 → Leap year

if (year%4 == 0 and year%100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print("not a leap year")


