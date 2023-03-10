# 김민재
####################
##### BFS 풀이 #####
####################

import sys
input = sys.stdin.readline


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = [(x, y)]
    arr[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if arr[nx][ny] == 1:
                    queue.append((nx, ny))
                    arr[nx][ny] = 0


T = int(input())

for test_case in range(1, T+1):
    N, M, cnt = map(int, input().split())
    arr = [[0 for col in range(M)] for row in range(N)]
    ans = 0

    for i in range(1, cnt+1):
        x, y = map(int, input().split())
        arr[x][y] = 1           # arr[row][col], row: 행(가로)/col: 열(세로)

    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1:
                bfs(x, y)
                ans += 1
    print(ans)
