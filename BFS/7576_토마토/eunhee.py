from collections import deque


def bfs():
    global queue
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y]+1
                    queue.append((nx, ny))


def check_tomato():
    global tomato
    res = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                return -1
            res = max(tomato[i][j], res)
    return res-1


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
queue = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

bfs()
res = check_tomato()
print(res)
