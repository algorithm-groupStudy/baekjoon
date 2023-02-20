# BOJ 13975
# 파일합치기

import sys 
import heapq

T = int(input())
for tc in range(1, T + 1): 
    K = int(input())
    files = list(map(int, sys.stdin.readline().split()))
    total = 0 
    heapq.heapify(files)

    while len(files) > 1: 
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        total += a+b
        heapq.heappush(files, a+b)
     
    
    print(total)


