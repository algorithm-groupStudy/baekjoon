import sys
sys.stdin = open("test.txt")
n, k = map(int, input().split())
dp = [100001 for _ in range(100001)]
dp[0] = 0
lst = [int(input()) for _ in range(n)]
for i in lst:
    for j in range(i, k+1):
        dp[j] = min(dp[j-i]+1, dp[j])
res = dp[k]

if dp[k] >= 100001:
    res = -1

print(res)
