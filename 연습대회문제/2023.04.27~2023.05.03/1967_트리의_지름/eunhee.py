# 다시풀어보기
import sys
sys.setrecursionlimit(10**9)

def dfs(x, weight):
    for nx,nw in graph[x]:
        if visited[nx] == -1:
            visited[nx] = nw + weight
            dfs(nx, nw+weight)


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
for _ in range(n-1):
    a,b,weight = map(int,input().split())
    graph[a].append((b,weight))
    graph[b].append((a,weight))

visited[1] = 0
dfs(1, 0)
start_node = visited.index(max(visited)) # 첫번째 정점부터 제일 긴 끝점 찾기

visited = [-1 for _ in range(n+1)]
visited[start_node] = 0
dfs(start_node,0) # 찾은 제일 긴 끝점 부터 시작해서 제일 긴 끝점 찾기
print(max(visited))
