# Subscriptions

# A new TV streaming service was recently started in Chefland called the Chef-TV.
# A group of N friends in Chefland want to buy Chef-TV subscriptions. We know that 6 people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is 
# X rupees. Determine the minimum total cost that the group of N friends will incur so that everyone in the group is able to use Chef-TV.

T = int(input())
for i in range(T):
    N, X = map(int, input().split())
    rem = N // 6
    if (N % 6 == 0):
        print(rem * X)
    else:
        print((rem+1)*X)