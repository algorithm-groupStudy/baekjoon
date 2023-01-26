3
n=int(input())
arr=sorted(list(map(int,input().split())))

left=0
right=n-1

res=abs(arr[right]+arr[left])
result=[arr[left],arr[right]]

while left<right:
    total=arr[left]+arr[right]
    if res>abs(total):
        res=abs(total)
        result=[arr[left],arr[right]]
    if total>=0:
        right-=1
    else:
        left+=1
    
print(*result)
    