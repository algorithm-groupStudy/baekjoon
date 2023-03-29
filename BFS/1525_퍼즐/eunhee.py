import sys
sys.stdin=open("test.txt")
from collections import deque

def bfs(g):
    queue=deque([g])
    # idx=g.index("0")
    visited[g]=0
    while queue:
        g_cur=queue.popleft()
        if g_cur=="123456780":
            return visited[g_cur]
        zero_idx = g_cur.index("0")
        g_curX = zero_idx // n
        g_curY= zero_idx % n
        for dx,dy in d:
            nx,ny = g_curX+dx,g_curY+dy
            if 0<=nx<n and 0<=ny<n:
                index = 3*nx+ny
                lst_g = list(g_cur)
                lst_g[index],lst_g[zero_idx] = lst_g[zero_idx],lst_g[index]
                new_g = ''.join(lst_g)
                if not visited.get(new_g):
                    visited[new_g] = visited[g_cur]+1
                    queue.append(new_g)
    return -1

    


n=3
d=[(0,1),(0,-1),(1,0),(-1,0)]
visited={}
lst=[list(input().split()) for _ in range(n)]
graph=""
for i in range(n):
    for j in range(n):
        graph+=lst[i][j]

print(bfs(graph))

