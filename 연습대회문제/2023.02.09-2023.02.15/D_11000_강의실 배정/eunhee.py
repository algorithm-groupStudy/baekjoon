# 다시풀 것
import heapq
n = int(input())
lst = []
for i in range(n):
    s, t = map(int, input().split())
    lst.append((s, t))
lst.sort(key=lambda x: x[0])
meeting = []
heapq.heappush(meeting, lst[0][1])

for i in range(1, n):
    if lst[i][0] >= meeting[0]:
        heapq.heappop(meeting)
        heapq.heappush(meeting, lst[i][1])
    else:
        heapq.heappush(meeting, lst[i][1])
print(len(meeting))