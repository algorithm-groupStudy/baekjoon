<<<<<<< HEAD
# 
import sys
sys.stdin=open("test.txt")
from collections import deque

def bfs(cur_x,cur_y):
    queue = deque([(cur_x,cur_y)])
    visited[cur_x][cur_y]=0
    while queue:
        x,y=queue.popleft()
        print("x,y:",x,y)
        if (x,y) == (door[1][0],door[1][1]):
            return visited[x][y]
        for dx,dy in direction:
            nx,ny = dx+x,dy+y
            print(nx,ny)
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if home[nx][ny]=="*":
                    continue
                if home[nx][ny]==".":
                    visited[nx][ny]=visited[x][y]
                elif home[nx][ny]=="!":
                    print("???")
                    if abs(x-y)==abs(nx-ny) or abs(x+y)==abs(nx+ny):
                        visited[nx][ny] = visited[x][y]
                    else:
                        visited[nx][ny]=visited[x][y]+1
                    
                else:
                    visited[nx][ny]=visited[x][y]
                queue.append((nx,ny))



N = int(input())
home = []
door=[]
for i in range(N):
    lst = list(input())
    for j in range(N):
        if lst[j]=="#":
            door.append((i,j))
    home.append(lst)
visited=[[-1 for _ in range(N)] for _ in range(N)]
direction = [(1,0),(0,-1),(-1,0),(0,1)]
print(home,door)
print(bfs(door[0][0],door[0][1]))
for row in visited:
    print(row)
=======
import sys
sys.stdin = open("test.txt")
from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, dir):
    q.append([x, y, dir])
    c[x][y][dir] = 1
    ans = []
    while q:
        x, y, dir = q.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            # 방문을 하지 않은 길이던가, 
            # 방문하려는 길이 현재 좌표의 숫자보다 클때,
            # 작은것을 찾는 것이므로 큰것을 작은것으로 바꿔줌
            if not c[nx][ny][dir] or c[nx][ny][dir] > c[x][y][dir]:
                if a[nx][ny] != '*':
                    c[nx][ny][dir] = c[x][y][dir]
                    if nx == fx and ny == fy:
                        ans.append(c[nx][ny][dir])
                        continue
                    q.append([nx, ny, dir])

                    # 거울일때
                    if a[nx][ny] == '!':
                        turn(nx, ny, dir)    # 90도 방향 탐색

    print(min(ans)-1)

def turn(x, y, dir):
    ndir = [(dir+1) % 4, (dir+3) % 4] # 지금 방향에서 90도로 꺾은 방향 두개 탐색

    for d in ndir:
        # bfs 로직과 마찬가지로 방문하지 않았으면 바로 넣어주기
        # 아니면 지금 경로보다 더 숫자가 클 경우 더 작은 숫자로 바꿔주기
        if not c[x][y][d] or c[x][y][d] > c[x][y][dir] + 1:
            c[x][y][d] = c[x][y][dir] + 1    # 거울을 하나 더 설치한 거니까 +1
            q.append([x, y, d])

n = int(input())  
q = deque()
c = [[[0]*4 for _ in range(n)] for _ in range(n)]
# 각 칸마다 방향을 담아준다.

a, temp = [], []
# a : map리스트
# temp : 시작과 도착 문 x,y 좌표
for i in range(n):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        if row[j] == '#':
            temp.extend([i, j])

sx, sy, fx, fy = temp

# 시작지점의 문에서 초기 시작 방향 설정.
for i in range(4):
    nx = sx + dx[i]
    ny = sy + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] != '*':
            dir = i
            break

# 시작 지점 봐표와 dir: 초기 시작 방향 인자로 받음
bfs(sx, sy, dir)

>>>>>>> origin/main
