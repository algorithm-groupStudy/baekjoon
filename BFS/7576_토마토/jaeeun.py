from collections import deque 

def bfs(start, graph): 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    need_visit = deque(start)
    while need_visit:
        x, y = need_visit.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M: 
                if graph[nx][ny] == 0: 
                    graph[nx][ny] = graph[x][y] + 1
                    need_visit.append((nx, ny))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

start = []
for n in range(N):
    for m in range(M): 
        if arr[n][m] == 1: 
            start.append((n, m))

bfs(start, arr)

zero = False
max_num = 0 
for n in range(N): 
    for m in range(M):
        if arr[n][m] == 0: 
            zero = True
            break 
        else:
            if max_num < arr[n][m]: 
                max_num = arr[n][m]

if zero: 
    print(-1)
else: 
    print(max_num-1) 