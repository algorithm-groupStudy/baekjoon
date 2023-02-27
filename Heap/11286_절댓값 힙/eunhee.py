import heapq
import sys
sys.stdin = open("test.txt")
input = sys.stdin.readline
n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            ab, res = heapq.heappop(heap)
            print(res)
        else:
            print(0)
