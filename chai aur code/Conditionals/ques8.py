# Password Strength Checker

# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong). 

password = input()
count = 0
for i in password:
    count += 1
if (count < 6):
    print("Weak")
elif (count < 11):
    print("Medium")
else:
    print("Strong")

# or check length 
length = len(password) 