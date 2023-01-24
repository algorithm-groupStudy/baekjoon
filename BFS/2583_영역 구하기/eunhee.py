from collections import deque
m, n, k = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(x, y):
    global arr
    queue = deque([(x, y)])
    arr[x][y] = 1
    area = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    queue.append((nx, ny))
                    area += 1
    return area


for i in range(k):
    dx, dy, ux, uy = map(int, input().split())

    for j in range(m-uy, m-dy):
        for k in range(dx, ux):
            arr[j][k] = 1

cnt = 0
area_arr = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            area = bfs(i, j)
            area_arr.append(area)
            cnt += 1

area_arr.sort()
print(cnt)
print(*area_arr)
