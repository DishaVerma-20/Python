# using loop
# Fibonacci sequence numbers ki ek series hai jisme har naya number pichhle do numbers ka sum hota hai.
n = int(input("enter for how many numbers?:- "))

a = 0
b = 1

for i in range (0, n):
    print(a, end = ' ')

    c = a+b
    a = b
    b = c

print()
# simply har iteration mai a ko print kr dege, a ki value chng hoti rhegi nh

# Recursive concept
def fib(n):
    if n==1 or n==2: # if sequence starts with 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(12))

print()

for i in range(1, n+1): # 0 se start nahi krr skte kyuki condn used, n==1 or n==2
    print(fib(i), end = ' ')
# if sequence starts with 0
# if n==0:
#     return 0
# elif n == 1:
#     return 1