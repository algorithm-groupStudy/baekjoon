n = int(input())


def dp_cnt(n):
    global dp
    if n <= 2:
        return n
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 15746
    return dp[n]



dp = [0 for _ in range(n+1)]
print(dp_cnt(n))
