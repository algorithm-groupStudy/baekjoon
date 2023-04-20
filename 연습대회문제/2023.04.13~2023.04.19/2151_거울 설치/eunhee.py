import sys
sys.stdin = open("test.txt")
from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, dt):
    queue.append((x, y, dt))
    visited[x][y][dt] = 1
    ans = []
    while queue:
        x, y, dt = queue.popleft()
        nx = x + dx[dt]
        ny = y + dy[dt]
        if 0 <= nx < N and 0 <= ny < N:
            # 방문을 하지 않은 길이던가, 
            # 방문하려는 길이 현재 좌표의 숫자보다 클때,
            # 작은것을 찾는 것이므로 큰것을 작은것으로 바꿔줌
            if not visited[nx][ny][dt] or visited[nx][ny][dt] > visited[x][y][dt]:
                if home[nx][ny] != '*':
                    visited[nx][ny][dt] = visited[x][y][dt]
                    if nx == fx and ny == fy: #반대편 문에 도착했을 시, 거울을 설치한 횟수 리스트에 담기
                        ans.append(visited[nx][ny][dt])
                        continue
                    queue.append([nx, ny, dt])

                    # 거울일때
                    if home[nx][ny] == '!':
                        turn(nx, ny, dt)    # 90도 방향 탐색

    print(min(ans)-1)

def turn(x, y, dt):
    ndir = [(dt+1) % 4, (dt+3) % 4] # 지금 방향에서 90도로 꺾은 방향 두개 탐색

    for d in ndir:  
        # bfs 로직과 마찬가지로 방문하지 않았으면 바로 넣어주기
        # 아니면 지금 경로보다 더 숫자가 클 경우 더 작은 숫자로 바꿔주기
        if not visited[x][y][d] or visited[x][y][d] > visited[x][y][dt] + 1:
            visited[x][y][d] = visited[x][y][dt] + 1    # 거울을 하나 더 설치한 거니까 +1
            queue.append([x, y, d])

N = int(input())  
queue = deque([])
visited = [[[0]*4 for _ in range(N)] for _ in range(N)]
# 각 칸마다 방향을 담아준다.

home, doors = [], []
# a : map리스트
# temp : 시작과 도착 문 x,y 좌표
for i in range(N):
    row = list(input())
    home.append(row)
    for j in range(N):
        if row[j] == '#':
            doors.extend([i, j])

sx, sy, fx, fy = doors

# 시작지점의 문에서 초기 시작 방향 설정.
for i in range(4):
    nx = sx + dx[i]
    ny = sy + dy[i]
    if 0 <= nx < N and 0 <= ny < N:
        if home[nx][ny] != '*':
            init_d = i
            break

# 시작 지점 봐표와 dir: 초기 시작 방향 인자로 받음
bfs(sx, sy, init_d)

