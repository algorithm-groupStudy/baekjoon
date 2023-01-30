len_prgs = int(input())
lst_prgs = list(map(int, input().split()))


dp = [0 for i in range(len_prgs)]

for i in range(len_prgs):
    for j in range(i):
        if lst_prgs[i] > lst_prgs[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))