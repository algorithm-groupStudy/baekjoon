# BOJ 7569 토마토 

# 2차원 토마토 문제를 3차원으로 풀었다. 

from collections import deque 
import sys 
input = sys.stdin.readline


def bfs(start): 
    # 여섯 방향 (위, 아래 포함) 체크 
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    q = deque(start)
    while q: 
        cz, cx, cy = q.popleft() 
        for k in range(6): 
            nz = cz + dz[k]
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H: 
                if tomatoes[nz][nx][ny] == 0:
                    tomatoes[nz][nx][ny] = tomatoes[cz][cx][cy] + 1 
                    q.append((nz, nx, ny))
    

M, N, H = map(int, input().split())
tomatoes = [] 
for _ in range(H): 
    tomato = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(tomato)

start = []
for h in range(H): 
    for n in range(N): 
        for m in range(M): 
            if tomatoes[h][n][m] == 1:
                # 시작점을 먼저 모두 찾은 후 시작한다. 
                start.append((h, n, m))

bfs(start) 

res = True
total = 0 

for h in range(H):
    for n in range(N): 
        for m in range(M): 
            if tomatoes[h][n][m] == 0: 
                # 익지 않은 토마토가 남아있으면 -1을 출력한다. 
                res = False 
                break  
            if tomatoes[h][n][m] > total: 
                total = tomatoes[h][n][m]

if not res: 
    print(-1)
else:
    # 0일차에 이미 익어있는 토마토 1로 표시해두었으므로 -1을 해준다. 
    print(total-1)