import sys
import heapq

input = sys.stdin.readline

heap = []
num_operation = int(input())
for operaion in range(num_operation):
    tmp = int(input())
    if tmp == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, tmp)
