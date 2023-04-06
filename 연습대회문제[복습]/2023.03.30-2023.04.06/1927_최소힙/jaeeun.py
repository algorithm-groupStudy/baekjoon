# BOJ 1927 최소힙

import heapq
import sys
input = sys.stdin.readline

heap = []

N = int(input())
for _ in range(N):
    x = int(input())
    if not x:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
