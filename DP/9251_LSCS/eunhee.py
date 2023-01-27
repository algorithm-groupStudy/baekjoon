string1 = list(input())
string2 = list(input())
n1=len(string1)
n2=len(string2)





def dp_solve(n_min,n_max,s_min,s_max):
    dp=[[0 for _ in range(n_max+1)] for _ in range(n_min)]
    print("s_min,s_max",(s_min,s_max))
    for i in range(n_min):
        for j in range(n_max):
            print(s_max[j],s_min[i])
            if s_max[j]==s_min[i]:
                dp[j][i]=dp[j-1][i-1]+1
            print("dp:",dp)
    res=0    
    for arr in dp:
        res=max(max(arr),res)
    return res

res=0
if n1>n2:
    res=dp_solve(n2,n1,string2,[0]+string1)
else:
    res=dp_solve(n1,n2,string1,[0]+string2)
print(res)