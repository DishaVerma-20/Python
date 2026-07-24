# Given two numbers, N and K. Create another number by concatenating N, K 
# times. Then repeatedly add all the digits of the resultant number, until you 
# # end up with a single digit number.


# digital root
# if (num % 9==0):
#     print(9)
# else:
#     print(num%9)


def single_digit(num):
     sums=0
     while num>0:
            mod = num % 10
            sums = sums + mod
            num = num // 10
     return sums

N = int(input())
K = int(input())

num = single_digit(N)*K
while num >= 10:
    num=single_digit(num)
print(num)
