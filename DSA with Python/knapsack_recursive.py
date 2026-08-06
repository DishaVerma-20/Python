def knapsack_recursive(weights, values, capacity, n):
    if n==0 or capacity == 0:
        return 0
    # shop mai item hai he nahi, ya phir chor bori lekar he nahi gaya haiii..
    if weights[n-1]>capacity:
        return knapsack_recursive(weights, values, capacity, n-1)

    # agar hum uss item ko include krte hai
    include = values[n-1] + knapsack_recursive(weights, values, capacity - weights[n-1], n-1)
    exclude = knapsack_recursive(weights, values, capacity, n-1)

    return max(include, exclude)

# ---------- Input ----------
n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter capacity of knapsack: "))

# ---------- Output ----------
ans = knapsack_recursive(weights, values, capacity, n)

print("Maximum Value =", ans)