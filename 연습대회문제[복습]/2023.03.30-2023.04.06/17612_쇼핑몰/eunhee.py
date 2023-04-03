import sys
import heapq
sys.stdin = open("test.txt")

n,k = map(int,input().split()) # n명 손님, k개의 계산대
queue = []
for _ in range(n):
    id,w = map(int,input().split())  # id값, w개의 물건
    queue.append((id,w))

counter = []
time=[0 for _ in range(k)]
res=[]
for i in range(k):
    heapq.heappush(counter,(0,i))

for i in range(n):
    t,idx = heapq.heappop(counter)
    time[idx]+=queue[i][1]
    heapq.heappush(counter,(time[idx],idx))
    res.append((time[idx],-idx,i))    
    # 제일 적은 시간 부터 빠져나옴, -idx인 이유는 time[idx] 가 같을 경우, idx값이 큰것부터 빠져나옴
res.sort()
total = 0
for i in range(n):
    total+=(i+1)*queue[res[i][-1]][0]
print(total)