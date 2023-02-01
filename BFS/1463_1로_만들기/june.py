
x = int(input())
dp = [0 for _ in range(x+1)]

if x<4:
    for i in range(x,1,-1):
        dp[i]=1    
else:
    dp[2]=1
    dp[3]=1
    for i in range(4,x+1):
        if i%3==0:
            dp[i] = min(dp[i//3],dp[i-1])+1
        if i%2==0:
            dp[i]=min(dp[i//2],dp[i-1])+1
        if (i%2!=0) and (i%3!=0):
            dp[i] = dp[i-1]+1

print(dp[x])
