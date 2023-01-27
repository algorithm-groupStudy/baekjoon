N = int(input())
A = list(map(int,input().split()))
L = len(A)
dp = [0 for _ in range(L+1)]
A.insert(0,0)

for i in range(1,L+1):
    for j in range(i):
        if A[i]>A[j]:
            dp[i]=max(dp[j]+1,dp[i])

print(max(dp))