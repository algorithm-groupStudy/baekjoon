# 나중에 다시 풀 문제 !!!! 

a=int(input())
arr=list(map(int,input().split()))
arr_reverse=arr[::-1]
dp_up=[1 for _ in range(a)]
dp_down=[1 for _ in range(a)]
for i in range(1,a):
    for j in range(i):
        if arr[i]>arr[j]:
            dp_up[i]=max(dp_up[j]+1,dp_up[i]) 
        if arr_reverse[i]>arr_reverse[j]: #뒤에서부터 감소하는 개수를 세줘야 되므로
            dp_down[i]=max(dp_down[j]+1,dp_down[i])

arr.reverse()

res=0
for i in range(a):
    res=max(res,dp_up[i]+dp_down[a-i-1])
print(res-1) # -1은 중복되는 숫자 빼기
