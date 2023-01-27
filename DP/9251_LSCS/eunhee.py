string1 = [0]+list(input())
string2 = [0]+list(input())
n1=len(string1)
n2=len(string2)

dp=[[0 for _ in range(n1)] for _ in range(n2)]
for i in range(1,n2):
    num=0
    for j in range(1,n1):
        if string1[j]==string2[i]:
            num=dp[i-1][j-1]+1
        dp[i][j]=max(dp[i-1][j],num)
print(dp[-1][-1])


