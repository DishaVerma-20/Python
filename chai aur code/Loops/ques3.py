# Multiplication table printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration. 

num = int(input())
for i in range (1, 11):
    if (i == 5):
        continue
    # current iteration skip karke loop ko next iteration par bhej deta hai
    print(i * num)
