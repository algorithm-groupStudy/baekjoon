import heapq
import sys
input = sys.stdin.readline
sys.stdin = open("text.txt")

n = int(input())
res = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(res, num)
        continue
    if res:
        print(heapq.heappop(res))
    else:
        print(0)
