import sys
sys.setrecursionlimit(10000)  # 재귀 깊이를 10000까지
t = int(input())
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(x, y):
    global arr
    if arr[x][y] == 0:
        return 0
    else:
        arr[x][y] = 0
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx, ny)
    return 1

for i in range(t):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0

    for j in range(n):
        for k in range(m):
            if arr[j][k] == 1:
                dfs(j,k)
                cnt = cnt+1
    print(cnt)
    