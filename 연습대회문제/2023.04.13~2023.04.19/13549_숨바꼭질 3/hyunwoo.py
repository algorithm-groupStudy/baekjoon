import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

# loc_subin, loc_sister = map(int,input().split())
# result = float('inf')
# print(f'{loc_subin} {loc_sister}')

# visited = [] 

# def bfs(start, turn):
#     global loc_sister, result
#     # record turn in result if turn is smaller than result
#     if start == loc_sister:
#         if result > turn:
#             result = turn
#         return
            
#     # backtracking 
#     if turn >= result:
#         return
    
#     if (start - 1) >= 0:
#         bfs(start-1, turn+1)
    
#     if (start + 1) <= 100000:
#         bfs(start+1, turn+1)
    
#     if 0 <= (2 * start) <= 100000:
#         bfs(start*2, turn)  
#     return


# bfs(loc_subin, 0)
# print(result)
# print('here')

from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if  0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)
MAX = 10 ** 5
dist = [0] * (MAX + 1)
n, k = map(int ,input().split())
bfs()