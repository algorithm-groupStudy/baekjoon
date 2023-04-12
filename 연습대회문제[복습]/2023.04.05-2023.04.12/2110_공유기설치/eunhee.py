# 미 제출 코드 아직 완벽히 이해하지 못함
import sys
sys.stdin = open("test.txt")

N,C = map(int,input().split())
home=sorted(list(int(input()) for _ in range(N)))
start, end = 1, home[-1]-home[0]

res=0
while start<=end:
    mid = (start+end)//2
    cnt=1
    cur_home=home[0]
    for i in range(1,N):
        if home[i]-cur_home>=mid:
            cnt+=1
            cur_home=home[i]
    if cnt>=C:
        res = mid
        start=mid+1
    else:
        end =mid-1
print(res)