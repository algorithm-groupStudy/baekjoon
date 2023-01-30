n,k=map(int,input().split())
coin_arr=[int(input()) for _ in range(n)]
dp=[0 for _ in range(k+1)]
dp[0]=1
for c in coin_arr:
    for j in range(c,k+1):
        dp[j]=dp[j-c]+dp[j]

print(dp[-1])