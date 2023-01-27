n = int(input())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))

dp = [0 for _ in range(n)]
dp[0] = A[0][0]
for i in range(1,n):
    for j in range(i,-1,-1):
        if j==i:
            dp[j]= dp[i-1]+ A[i][j]
        elif j==0:
            dp[j] = dp[j]+A[i][j]
        else:
            dp[j]= max(dp[j]+ A[i][j],dp[j-1]+A[i][j])
print(max(dp))