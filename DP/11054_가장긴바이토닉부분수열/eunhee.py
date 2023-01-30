a=int(input())
arr=list(map(int,input().split()))
dp_up=[1 for _ in range(a)]
dp_down=[1 for _ in range(a)]

for i in range(1,a):
    for j in range(i):
        if arr[i]>arr[j]:
            dp_up[i]=max(dp_up[j]+1,dp_up[i]) 
        elif arr[i]<arr[j]:
            dp_down[i]=max(dp_down[j]+1,dp_down[i])

print(dp_up)
print(dp_down)

# def dp_up(lst):
#     dp=[1 for _ in range(len(lst))]
#     for i in range(1,len(lst)):
#         for j in range(i):
#             if lst[i]>lst[j]:
#                 dp[i]=max(dp[j]+1,dp[i])
#     return dp

# def dp_down(lst):
#     dp=[1 for _ in range(len(lst))]
#     for i in range(1,len(lst)):
#         for j in range(i):
#             if lst[i]<lst[j]:
#                 dp[i]=max(dp[j]+1,dp[i])
#     return dp

# dp_up=dp_up(arr)
# dp_down=dp_down(arr)
# res=0
# for i in range(a-1):
#     up=max(dp_up[:i+1])
#     lst=dp_down[i+1:]
#     print(lst)
#     down=max(dp_up(lst))
    
#     res=max(res,up+down)

# print(res)


