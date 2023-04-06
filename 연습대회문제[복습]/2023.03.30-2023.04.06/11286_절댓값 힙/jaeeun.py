# BOJ 11286 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

N = int(input())

pos = []
neg = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if pos and neg:
            pos_p = heapq.heappop(pos)
            neg_p = heapq.heappop(neg)
            if neg_p <= pos_p:
                print(-neg_p)
                heapq.heappush(pos, pos_p)
            else:
                print(pos_p)
                heapq.heappush(neg, neg_p)
        elif pos:
            pos_p = heapq.heappop(pos)
            print(pos_p)
        elif neg:
            neg_p = heapq.heappop(neg)
            print(-neg_p)
        else:
            print(0)
    elif x < 0:
        heapq.heappush(neg, -x)
    else:
        heapq.heappush(pos, x) 