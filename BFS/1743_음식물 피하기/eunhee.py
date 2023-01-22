from collections import deque
n, m, k = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):
    queue = deque([(x, y)])
    arr[x][y] = 0
    cnt = 1
    while queue:
        a, b = queue.popleft()
        for dx, dy in d:
            nx, ny = a+dx, b+dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1
    return cnt


for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            res = max(res, bfs(i, j))

print(res)
