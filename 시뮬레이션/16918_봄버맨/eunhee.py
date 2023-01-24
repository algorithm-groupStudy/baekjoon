from collections import deque


def boom(x, y):
    global bomb
    bomb[x][y] = "."
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < r and 0 <= ny < c:
            bomb[nx][ny] = "."


r, c, n = map(int, input().split())
bomb = [list(str(input())) for _ in range(r)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
time = 1
bomb_d = []

while time < n:
    time += 1
    if time % 2 == 0:
        for i in range(r):
            for j in range(c):
                if bomb[i][j] == "O":
                    bomb_d.append((i, j))
                else:
                    bomb[i][j] = "O"

    else:
        for x, y in bomb_d:
            bomb[x][y] = "."
            boom(x, y)
            bomb_d = []

for i in range(r):
    print(*bomb[i], sep="")
