a=int(input())
arr=list(map(int,input().split()))
dp_up=[1 for _ in range(a)]
dp_down=[1 for _ in range(a)]

def dp_up(lst):
    dp=[1 for _ in range(len(lst))]
    print("lst:",lst)
    print("dp:",dp)
    for i in range(1,len(lst)):
        for j in range(i):
            if lst[i]>lst[j]:
                dp[i]=max(dp[j]+1,dp[i])
    return dp

def dp_down(lst):
    dp=[1 for _ in range(len(lst))]
    for i in range(1,len(lst)):
        for j in range(i):
            if lst[i]<lst[j]:
                dp[i]=max(dp[j]+1,dp[i])
    return dp

dp_up=dp_up(arr)
dp_down=dp_down(arr)
print("dp_down:",dp_down)
res=0
for i in range(a-1):
    up=max(dp_up[:i+1])
    lst=dp_down[i+1:]
    print(lst)
    down=max(dp_up(lst))
    
    res=max(res,up+down)

print(res)


