from collections import deque


def bfs(x, y):
    global colorArr, visited
    queue = deque([(x, y)])
    visited[x][y] = False
    while queue:
        a, b = queue.popleft()
        for dx, dy in d:
            nx, ny = a+dx, b+dy
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny]:
                    continue
                if colorArr[nx][ny] == colorArr[a][b]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return 1


n = int(input())
colorArr = [list(str(input())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
cnt_not = 0
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt_not += bfs(i, j)


for i in range(n):
    for j in range(n):
        if colorArr[i][j] == "G":
            colorArr[i][j] = "R"

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += bfs(i, j)

print(cnt_not, cnt)
