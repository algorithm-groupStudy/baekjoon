import sys
sys.stdin = open("test.txt")
n = int(input())
lst = list(map(int, input().split()))
dp = [1000000000 for _ in range(n)]
dp[0] = 0
for i in range(1, n):
    for j in range(i):
        dp[i] = min(dp[i], max((i-j)*(1+abs(lst[i]-lst[j])), dp[j]))

print(dp[-1])
