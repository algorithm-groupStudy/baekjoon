import sys
sys.stdin = open("test.txt")
from collections import deque

def bfs(node):
    global visited
    queue=deque([node])
    visited[node]=True
    cnt=0
    while queue:
        x = queue.popleft()
        for j in country[x]:
            if not visited[j]:
                visited[j]=True
                queue.append(j)
                cnt+=1
    return cnt


t = int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    country = [[] for _ in range(n+1)]
    visited=[False for _ in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        country[a].append(b)
        country[b].append(a)
    res=0
    for i in range(1,n+1):
        if not visited[i]:
            res+=bfs(i)
    print(res)
