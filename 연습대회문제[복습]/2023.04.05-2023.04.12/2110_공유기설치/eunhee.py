

N,C = map(int,input().split())
home= list(int(input()) for _ in range(N))
home.sort()

start,end=1,home[-1]-home[0]
res=0
while start<=end:
    mid = (start+end)//2
    current_home = home[0]
    cnt=1
    for i in range(1,N):
        if home[i]-current_home>=mid:
            cnt+=1
            current_home = home[i]
    if cnt>=C:
        res = mid
        start = mid+1
    else:
        end=mid-1

print(res)