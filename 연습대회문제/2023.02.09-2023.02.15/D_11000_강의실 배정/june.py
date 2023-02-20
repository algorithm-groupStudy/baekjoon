import heapq
N = int(input())
arr =[]
que = []
for i in range(N):
    a, b = map(int,input().split())
    arr.append((a,b))
arr.sort()
heapq.heappush(que, arr[0][1])
for i in arr:
    if i == arr[0]:
        pass
    elif i[0]>=que[0] :
        heapq.heappop(que)
        heapq.heappush(que,i[1])
    else:        
        heapq.heappush(que,i[1])
print(len(que))