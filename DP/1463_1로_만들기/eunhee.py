n = int(input())
dp = [0 for _ in range(n+1)]

dp[0], dp[1] = 0, 0

for i in range(2, n+1):
    dp[i] = min(dp[i//2]+i % 2, dp[i//3]+i % 3)+1
print(dp[n])
