from collections import deque
t=int(input())

def bfs(x):
    global graph,visited,check
    queue=deque([x])
    visited[x]=True

    while queue:
        x=queue.popleft()
        for node in graph[x]:
            if visited[node]==False:
                visited[node]=True
                check[node]=not check[x]
                queue.append(node)
            elif visited[node]==True:
                if check[node]==check[x]:
                    return False

    return True



for tc in range(t):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    visited=[False for _ in range(v+1)]
    check=[False for _ in range(v+1)]

    for j in range(e):
        node1,node2=map(int,input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    flag=False
    for j in range(1,v+1):
        if visited[j]==False:
            if not bfs(j):
                flag=True
                break
    print("NO" if flag else "YES")
        