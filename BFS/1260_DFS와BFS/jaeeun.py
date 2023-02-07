from collections import deque

N, M, V = map(int, input().split())
graph = [list() for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y) 
    graph[y-1].append(x)

graph = [sorted(l) for l in graph] 


def dfs(start, arr):
    visited = []
    need_visit = [start]
    while need_visit:
        pt = need_visit.pop()
        if pt not in visited:
            visited.append(pt)
            for i in range(len(arr[pt-1])-1, -1, -1):  # 역순 주의
                need_visit.append(arr[pt-1][i])

    return visited


def bfs(start, arr):
    visited = []
    need_visit = deque()
    need_visit.append(start)
    while need_visit:
        pt = need_visit.popleft()
        if pt not in visited:
            visited.append(pt)
            for i in range(len(arr[pt-1])):
                need_visit.append(arr[pt-1][i])
    return visited


res_dfs = dfs(V, graph)
res_bfs = bfs(V, graph)
print(*res_dfs)
print(*res_bfs)