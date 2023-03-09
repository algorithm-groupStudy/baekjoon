# BOJ 2644 촌수계산 

from collections import deque 

# BFS를 통해 시작점과 목표점 사이의 거리를 visited에 저장한다. 
def bfs(start, goal):
    visited = [-1 for _ in range(N+1)]
    q = deque([start])
    visited[start] += 1 
    while q: 
        now = q.popleft()
        for next_v in adj[now]: 
            if visited[next_v] == -1: 
                q.append(next_v)
                visited[next_v] = visited[now] + 1
              
    return visited[goal]

N = int(input())
adj = [[] for _ in range(N+1)]
S, G = map(int, input().split())
M = int(input())
# 인접리스트로 부모-자식 관계를 저장한다. 
for _ in range(M): 
    s, g = map(int, input().split())
    adj[s].append(g)
    adj[g].append(s)

print(bfs(S, G))