import sys
sys.stdin=open("test.txt")
from collections import deque

def bfs(node):
    queue=deque([node])
    visited[node]=1
    if node==G:
        return visited[node]-1
    while queue:
        x = queue.popleft()
        # if x==G:
        #     return visited[x]-1
        for i in [x+U, x-D]:
            if 0<i<=F and not visited[i]:
                visited[i]=visited[x]+1
                if i==G:
                    return visited[i]-1
                queue.append(i)

    return "use the stairs"
                

F,S,G,U,D = map(int,input().split())
visited=[0 for _ in range(F+1)]
print(bfs(S))
