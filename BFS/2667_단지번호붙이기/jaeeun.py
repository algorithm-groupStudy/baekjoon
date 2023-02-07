from collections import deque 

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

def bfs(start, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = start
    graph[x][y] = 0
    cnt = 1 
    need_visit = deque([(x, y)])

    while need_visit:
        x, y = need_visit.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N: 
                if graph[nx][ny] == 1: 
                    need_visit.append((nx, ny))
                    graph[nx][ny] = 0
                    cnt += 1 

    return cnt 

res = []
for n in range(N):
    for m in range(N):
        if graph[n][m] == 1: 
            res.append(bfs((n, m), graph))

res.sort()

print(len(res))
for r in res:
    print(r)