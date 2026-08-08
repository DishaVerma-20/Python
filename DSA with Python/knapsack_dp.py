def knapsackDP(wt, value, capacity):
    n = len(wt)

    dp = [[0]*(capacity + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(capacity + 1):
            if (wt[i-1]<=w):
                dp[i][w] = max(dp[i-1][w], dp[])