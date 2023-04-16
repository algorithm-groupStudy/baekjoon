import sys
sys.stdin = open("test.txt")
from collections import deque

def bfs(node):
    queue=deque([node])
    visited[node]=True
    while queue:
        x = queue.popleft()
        if x==K:
            return path[x]
        for i in [x-1,x+1,2*x]:
            if 0<=i<=200000 and not visited[i]:
                if x*2==i:
                    path[i]=path[x]
                    queue.appendleft(i)
                else:
                    path[i]=path[x]+1
                    queue.append(i)
                visited[i]=True
                




N, K = map(int,input().split())
path=[0 for _ in range(200001)]
visited=[False for _ in range(200001)]
print(bfs(N))